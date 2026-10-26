"""Tests for sting.minimal_runner, using the fake client only (no network)."""
import json
import re
from pathlib import Path

import pytest
import yaml

from sting.minimal_runner import agent_names, market_draws, run_batch
from sting.paths import REPO_ROOT, UPSTREAM_ROOT


def fake_cfg(**overrides):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake.yaml").read_text(encoding="utf-8"))
    cfg.update(overrides)
    return cfg


def round_blocks(auction_results: Path) -> list[dict]:
    text = auction_results.read_text(encoding="utf-8")
    return [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````", text, flags=re.S)]


def test_episode_logs_every_ask_bid_trade_and_message(tmp_path):
    summary = run_batch(fake_cfg(replicates=1, concurrency=1), runs_dir=tmp_path)
    assert summary["completed"] == 1 and summary["failed"] == 0
    run_dir = Path(summary["run_dir"])
    rep_dir = next(p for p in run_dir.iterdir() if p.is_dir())
    rounds = round_blocks(rep_dir / "upstream_logs" / "auction_results.md")
    assert [r["round_number"] for r in rounds] == [1, 2, 3]
    for r in rounds:
        assert set(r["seller_asks"]) == {"Seller A", "Seller B", "Seller C"}
        assert set(r["buyer_bids"]) == {"Buyer A", "Buyer B", "Buyer C"}
        assert set(r["seller_messages"]) == {"Seller A", "Seller B", "Seller C"}
        assert "trades" in r
    status = json.loads((rep_dir / "status.json").read_text())
    assert status["status"] == "completed" and status["rounds_completed"] == 3
    assert status["usage_by_role"]["seller"]["calls"] == 9 and status["usage_by_role"]["buyer"]["calls"] == 9
    assert len((rep_dir / "calls.jsonl").read_text().splitlines()) == 18


def test_outputs_stay_out_of_third_party(tmp_path):
    before = {p for p in UPSTREAM_ROOT.rglob("*") if ".git" not in p.parts}
    run_batch(fake_cfg(replicates=1, concurrency=1), runs_dir=tmp_path)
    after = {p for p in UPSTREAM_ROOT.rglob("*") if ".git" not in p.parts}
    assert after - before == set() or all("__pycache__" in p.parts for p in after - before)


def test_failed_episode_is_marked_partial_log_kept_and_batch_continues(tmp_path):
    cfg = fake_cfg(replicates=2, concurrency=1)
    failing = {"provider": "fake", "model": "fake-model", "fail_on_round": 2}
    cfg["sellers"] = [failing] + cfg["sellers"][1:]
    summary = run_batch(cfg, runs_dir=tmp_path)
    assert summary["failed"] == 2 and summary["completed"] == 0
    for rep_dir in (p for p in Path(summary["run_dir"]).iterdir() if p.is_dir()):
        status = json.loads((rep_dir / "status.json").read_text())
        assert status["status"] == "failed" and status["rounds_completed"] == 1
        assert "scripted fake failure" in status["error"]
        assert [r["round_number"] for r in round_blocks(rep_dir / "upstream_logs" / "auction_results.md")] == [1]


def test_replicate_ids_unique_and_existing_run_dir_not_reused(tmp_path):
    a = run_batch(fake_cfg(), runs_dir=tmp_path)
    b = run_batch(fake_cfg(), runs_dir=tmp_path)
    assert a["run_id"] != b["run_id"]
    rep_ids = [p.name for s in (a, b) for p in Path(s["run_dir"]).iterdir() if p.is_dir()]
    assert len(rep_ids) == len(set(rep_ids)) == 4


def test_market_draws_depend_only_on_replicate_index():
    cfg = fake_cfg()
    assert market_draws(cfg, 0) == market_draws(cfg, 0)
    assert market_draws(cfg, 0) != market_draws(cfg, 1)
    d = market_draws(cfg, 0)
    assert all(96.25 <= a <= 98.75 for a in d["initial_asks"])
    assert all(81.25 <= b <= 83.75 for b in d["initial_bids"])


def test_names_are_fixed_and_neutral():
    assert agent_names(3, "Seller") == ["Seller A", "Seller B", "Seller C"]


def test_initial_book_is_recorded(tmp_path):
    summary = run_batch(fake_cfg(replicates=1, concurrency=1), runs_dir=tmp_path)
    rep_dir = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    setup = json.loads((rep_dir / "market_setup.json").read_text())
    assert setup["initial_asks"] == dict(zip(["Seller A", "Seller B", "Seller C"],
                                             market_draws(fake_cfg(), 0)["initial_asks"]))


def test_cost_gate_blocks_expensive_batches(tmp_path):
    with pytest.raises(SystemExit, match="human approval required"):
        run_batch(fake_cfg(estimated_cost_per_episode_usd=1.5), runs_dir=tmp_path)
    assert not any(tmp_path.iterdir())


def test_parse_cap_marks_episode_failed_with_reason_and_counts(tmp_path):
    cfg = fake_cfg(replicates=1, concurrency=1)
    bad = {"provider": "fake", "model": "fake-model", "bad_json_on_round": 2}
    cfg["sellers"] = [bad] + cfg["sellers"][1:]
    summary = run_batch(cfg, runs_dir=tmp_path)
    assert summary["failures_by_reason"] == {"parse_cap": 1}
    assert summary["parse_failures_total"] == 3
    rep_dir = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    status = json.loads((rep_dir / "status.json").read_text())
    assert status["failure_reason"] == "parse_cap" and status["rounds_completed"] == 1
    assert status["usage_by_role"]["seller"]["parse_failures"] == 3


def test_failure_reason_for_api_failure(tmp_path):
    cfg = fake_cfg(replicates=1, concurrency=1)
    cfg["buyers"] = [{"provider": "fake", "model": "fake-model", "fail_on_round": 1}] + cfg["buyers"][1:]
    summary = run_batch(cfg, runs_dir=tmp_path)
    assert summary["failures_by_reason"] == {"api_failure": 1}


def test_estimate_only_makes_no_run(tmp_path):
    out = run_batch(fake_cfg(estimated_cost_per_episode_usd=5.0), runs_dir=tmp_path, estimate_only=True)
    assert out["estimated_cost_usd"] == 10.0 and out["replicate_indices"] == [0, 1]
    assert not any(tmp_path.iterdir())


def test_replicate_indices_select_episodes_and_keep_draws(tmp_path):
    pilot = run_batch(fake_cfg(replicates=3, concurrency=1), runs_dir=tmp_path, replicate_indices=[0])
    rest = run_batch(fake_cfg(replicates=3, concurrency=2), runs_dir=tmp_path, replicate_indices=[1, 2])
    assert pilot["replicates"] == 1 and rest["replicates"] == 2
    names = sorted(p.name[-4:] for p in Path(rest["run_dir"]).iterdir() if p.is_dir())
    assert names == ["r001", "r002"]
    rep1 = next(p for p in Path(rest["run_dir"]).iterdir() if p.name.endswith("r001"))
    setup = json.loads((rep1 / "market_setup.json").read_text())
    assert setup["replicate_index"] == 1
    assert list(setup["initial_asks"].values()) == market_draws(fake_cfg(), 1)["initial_asks"]


def test_config_requires_run_type(tmp_path):
    cfg = fake_cfg()
    del cfg["run_type"]
    with pytest.raises(ValueError, match="run_type"):
        run_batch(cfg, runs_dir=tmp_path)


def test_confirmatory_refuses_uncommitted_changes(tmp_path, monkeypatch):
    import sting.docs
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [" M sting/clients.py"])
    with pytest.raises(SystemExit, match="Confirmatory run refused"):
        run_batch(fake_cfg(run_type="confirmatory", budget={"group": "t", "cap_usd": 1.0}), runs_dir=tmp_path)
    assert not any(tmp_path.iterdir())


def test_confirmatory_runs_when_clean_and_pilot_runs_when_dirty(tmp_path, monkeypatch):
    import sting.docs
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [])
    assert run_batch(fake_cfg(run_type="confirmatory", replicates=1, budget={"group": "t", "cap_usd": 1.0}),
                     runs_dir=tmp_path)["completed"] == 1
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [" M sting/clients.py"])
    assert run_batch(fake_cfg(run_type="pilot", replicates=1), runs_dir=tmp_path)["completed"] == 1



def test_repeated_replicate_indices_share_draws_with_unique_ids(tmp_path):
    summary = run_batch(fake_cfg(replicates=2, concurrency=2), runs_dir=tmp_path, replicate_indices=[0, 0, 1, 1])
    assert summary["replicates"] == 4 and summary["completed"] == 4
    reps = sorted(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    names = sorted(p.name[len(summary["run_id"]) + 1:] for p in reps)
    assert names == ["r000_d1", "r000_d2", "r001_d1", "r001_d2"]
    setups = {n: json.loads((Path(summary["run_dir"]) / f"{summary['run_id']}_{n}" / "market_setup.json").read_text())
              for n in names}
    assert setups["r000_d1"]["initial_asks"] == setups["r000_d2"]["initial_asks"]
    assert setups["r000_d1"]["initial_asks"] != setups["r001_d1"]["initial_asks"]



def test_model_identity_flags(tmp_path):
    from sting.minimal_runner import model_identity_flags
    run = tmp_path / "run"; (run / "rep").mkdir(parents=True)
    (run / "run_config.json").write_text(json.dumps({"model_snapshots_at_start": {"m": {"canonical_slug": "m-2025-04-14"}}}))
    calls = [{"provider": "openrouter", "requested_model": "m", "returned_model": "m", "error": None},
             {"provider": "openrouter", "requested_model": "m", "returned_model": "m-other", "error": None}]
    (run / "rep" / "calls.jsonl").write_text(chr(10).join(json.dumps(c) for c in calls))
    r = model_identity_flags(run, {"m": {"canonical_slug": "m-2025-06-01"}})
    assert r["model_identity_flag"] and r["returned_model_mismatches"] == {"m -> m-other": 1}
    assert r["snapshot_changed_during_run"] == {"m": {"start": "m-2025-04-14", "end": "m-2025-06-01"}}
    (run / "rep" / "calls.jsonl").write_text(json.dumps(calls[0]))
    assert model_identity_flags(run, {"m": {"canonical_slug": "m-2025-04-14"}})["model_identity_flag"] is False
