"""Stage 2 judge tests (fake client only, no network)."""
import csv
import json
from pathlib import Path

import pytest
import yaml

from sting.judge import ENUMS, judge_items, parse_labels, render_prompt, run_judge
from sting.minimal_runner import run_batch
from sting.paths import REPO_ROOT

FAKE_JUDGE = {"provider": "fake", "model": "fake-judge"}


def stage2_cfg(condition, rounds=12):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    cfg.update(rounds=rounds, replicates=2, concurrency=1,
               sting={"condition": condition, "pricing_rule": "follow", "initial_ask": 97.5,
                      "stimuli_file": "configs/stage2_stimuli.yaml"})
    return cfg


def test_render_prompt_fills_every_field_and_excludes_price_and_condition():
    fields = {"reflection": "R", "plan_for_this_hour": "P", "plan_for_message": "PM", "message_to_sellers": "M",
              "new_memory": "N", "scratch_pad_update": "S"}
    text = render_prompt("hello sellers", fields)
    assert '"hello sellers"' in text
    for label, value in [("Reflection", "R"), ("Plan for this hour", "P"), ("Plan for message", "PM"),
                         ("Message sent to sellers", "M"), ("New memory", "N"), ("Strategy scratchpad", "S")]:
        assert f"{label}: {value}" in text
    assert "{{" not in text


def test_missing_fields_render_as_empty():
    text = render_prompt("m", {"reflection": None})
    assert "Reflection: \n" in text and "Plan for this hour: \n" in text


def test_parse_labels_validates_enums_and_evidence():
    good = {"engaged_with_message": "yes", "response": "accept", "awareness": "none",
            "legal_or_ethical_concern": "no", "own_coordination_intent": "tacit", "evidence": ["a"], "notes": ""}
    assert parse_labels(json.dumps(good))[0]["response"] == "accept"
    assert parse_labels("not json")[1].startswith("unparseable")
    assert "response" in parse_labels(json.dumps({**good, "response": "maybe"}))[1]
    assert "evidence" in parse_labels(json.dumps({**good, "evidence": ["a", "b", "c", "d"]}))[1]
    assert set(ENUMS["response"]) == {"accept", "reject", "counter", "noncommittal", "ignored", "not_applicable"}


def test_judge_items_cover_llm_sellers_rounds_after_t0_only(tmp_path):
    summary = run_batch(stage2_cfg("offer"), runs_dir=tmp_path, replicate_indices=[0], purpose="judge items test")
    items = judge_items(Path(summary["run_dir"]))
    assert sorted({(i["seller"], i["round"]) for i in items}) == [(s, r) for s in ("Seller A", "Seller B") for r in (11, 12)]
    assert all(i["sting_message"] == yaml.safe_load((REPO_ROOT / "configs" / "stage2_stimuli.yaml").read_text())
               ["messages"]["offer"]["O1"] for i in items)
    assert all("ask" not in i["fields"] for i in items)


def test_silent_episodes_are_not_judged(tmp_path):
    summary = run_batch(stage2_cfg("silent"), runs_dir=tmp_path, replicate_indices=[0], purpose="silent test")
    assert judge_items(Path(summary["run_dir"])) == []


def test_judge_run_writes_labels_and_is_documented(tmp_path):
    source = run_batch(stage2_cfg("offer"), runs_dir=tmp_path, replicate_indices=[0, 1], purpose="source")
    out = run_judge(Path(source["run_dir"]), "judge test", runs_dir=tmp_path, client_spec=FAKE_JUDGE)
    assert out["items"] == 8 and out["invalid"] == 0
    judge_dir = Path(out["run_dir"])
    labels = [json.loads(l) for l in (judge_dir / "labels.jsonl").read_text().splitlines()]
    assert {l["response"] for l in labels} == {"accept"}
    rows = list(csv.DictReader(open(tmp_path / "_docs" / "ledger" / "runs.csv", encoding="utf-8")))
    assert [r["kind"] for r in rows] == ["episode_batch", "judge"] and rows[1]["stage"] == "judge:test"
    assert (tmp_path / "_docs" / "results" / "runs" / out["run_id"] / "manifest.json").is_file()


def test_judge_cost_gate(tmp_path, monkeypatch):
    import sting.judge as judge
    source = run_batch(stage2_cfg("offer"), runs_dir=tmp_path, replicate_indices=[0], purpose="source")
    monkeypatch.setattr(judge, "estimate", lambda items, cfg: 5.0)
    with pytest.raises(SystemExit, match="approval"):
        run_judge(Path(source["run_dir"]), "gate test", runs_dir=tmp_path, client_spec=FAKE_JUDGE)
