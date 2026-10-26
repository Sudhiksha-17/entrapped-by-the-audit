"""Budget cap and failed-episode replacement tests (fake client only, no network)."""
import json
from pathlib import Path

import pytest
import yaml

import sting.docs
from sting.judge import run_judge
from sting.minimal_runner import run_batch, spent_in_budget_group
from sting.paths import REPO_ROOT


def cfg(**kw):
    c = yaml.safe_load((REPO_ROOT / "configs" / "test_fake.yaml").read_text(encoding="utf-8"))
    c.update(replicates=1, concurrency=1, **kw)
    return c


def test_confirmatory_needs_a_budget(tmp_path, monkeypatch):
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [])
    with pytest.raises(ValueError, match="budget"):
        run_batch(cfg(run_type="confirmatory"), runs_dir=tmp_path)


def test_budget_refuses_a_batch_that_would_exceed_the_cap(tmp_path):
    c = cfg(estimated_cost_per_episode_usd=0.6, budget={"group": "g1", "cap_usd": 1.0})
    with pytest.raises(SystemExit, match="Budget cap refused"):
        run_batch(dict(c, replicates=2), runs_dir=tmp_path)
    assert not any(p.name != "_docs" for p in tmp_path.iterdir())


def test_budget_counts_spend_already_on_disk(tmp_path, monkeypatch):
    c = cfg(estimated_cost_per_episode_usd=0.1, budget={"group": "g2", "cap_usd": 1.0})
    run_batch(c, runs_dir=tmp_path)
    assert spent_in_budget_group("g2", tmp_path) == 0.0  # fake client reports no cost
    import sting.minimal_runner as mr
    monkeypatch.setattr(mr, "spent_in_budget_group", lambda group, runs_dir: 0.95)
    with pytest.raises(SystemExit, match=r"spent \$0\.9500"):
        run_batch(c, runs_dir=tmp_path)


def test_budget_guard_skips_episodes_that_would_exceed_the_cap(tmp_path, monkeypatch):
    import sting.minimal_runner as mr
    calls = {"n": 0}

    def fake_spent(group, runs_dir):  # pre-launch 0; first episode sees 0.85 (0.85 + 0.1 <= 1); later 0.95
        calls["n"] += 1
        return {1: 0.0, 2: 0.85}.get(calls["n"], 0.95)
    monkeypatch.setattr(mr, "spent_in_budget_group", fake_spent)
    c = cfg(estimated_cost_per_episode_usd=0.1, budget={"group": "g3", "cap_usd": 1.0})
    c["replicates"] = 3
    summary = run_batch(c, runs_dir=tmp_path)
    assert summary["completed"] == 1 and len(summary["not_started_budget_cap"]) == 2


def test_failed_episode_replaced_with_new_id_that_references_it(tmp_path):
    bad = cfg()
    bad["sellers"] = [{"provider": "fake", "model": "fake-model", "fail_on_round": 2}] + bad["sellers"][1:]
    first = run_batch(bad, runs_dir=tmp_path, replicate_indices=[1])
    failed_id = first["failed_replicates"][0]["replicate_id"]
    second = run_batch(cfg(), runs_dir=tmp_path, replaces=[failed_id])
    assert second["completed"] == 1
    (new_id, ref), = second["replacements"].items()
    assert ref == failed_id and new_id.endswith("_r001_repl1") and new_id != failed_id
    rep = Path(second["run_dir"]) / new_id
    assert json.loads((rep / "status.json").read_text())["replaces"] == failed_id
    setup = json.loads((rep / "market_setup.json").read_text())
    assert setup["replaces"] == failed_id and setup["replicate_index"] == 1
    # the failed replicate's files are untouched
    assert json.loads((Path(first["run_dir"]) / failed_id / "status.json").read_text())["status"] == "failed"


def test_completed_or_foreign_replicates_cannot_be_replaced(tmp_path):
    ok = run_batch(cfg(), runs_dir=tmp_path)
    ok_id = next(p.name for p in Path(ok["run_dir"]).iterdir() if p.is_dir())
    with pytest.raises(ValueError, match="only failed"):
        run_batch(cfg(), runs_dir=tmp_path, replaces=[ok_id])
    with pytest.raises(ValueError, match="not found"):
        run_batch(cfg(), runs_dir=tmp_path, replaces=["no_such_id"])
    with pytest.raises(ValueError, match="either"):
        run_batch(cfg(), runs_dir=tmp_path, replaces=[ok_id], replicate_indices=[0])


def test_judge_respects_the_source_budget(tmp_path, monkeypatch):
    c = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    c.update(rounds=12, replicates=1, budget={"group": "g4", "cap_usd": 1.0},
             sting={"condition": "offer", "pricing_rule": "follow", "initial_ask": 97.5,
                    "stimuli_file": "configs/stage2_stimuli.yaml"})
    source = run_batch(c, runs_dir=tmp_path)
    import sting.minimal_runner as mr
    monkeypatch.setattr(mr, "spent_in_budget_group", lambda group, runs_dir: 0.999)
    import sting.judge as judge
    monkeypatch.setattr(judge, "estimate", lambda items, cfg: 0.01)
    with pytest.raises(SystemExit, match="Budget cap refused"):
        run_judge(Path(source["run_dir"]), "budget test", runs_dir=tmp_path,
                  client_spec={"provider": "fake", "model": "fake-judge"})
