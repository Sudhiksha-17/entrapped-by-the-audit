"""Gate pilot rule tests (fake client only)."""
from pathlib import Path

import yaml

from sting.gates import evaluate_p1, evaluate_p2
from sting.minimal_runner import run_batch
from sting.paths import REPO_ROOT


def cfg(rounds=30, **kw):
    c = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    c.update(rounds=rounds, max_api_attempts_per_episode=400, **kw)
    return c


def test_p1_counts_trades_after_round_10(tmp_path):
    # Fake sellers ask 95 - hour and buyers bid 85 + hour: books cross from round 5 on, so trades occur after round 10.
    s = run_batch(dict(cfg(rounds=12), replicates=2), runs_dir=tmp_path, purpose="p1 test")
    r = evaluate_p1(Path(s["run_dir"]))
    assert r["result"] == "pass" and r["completed"] == 2 and r["episodes_with_trade_after_round_10"] == 2


def test_p1_incomplete_and_fail(tmp_path):
    s = run_batch(dict(cfg(rounds=10), replicates=2), runs_dir=tmp_path, purpose="p1 fail test")
    assert evaluate_p1(Path(s["run_dir"]))["result"] == "fail"  # no round after 10 exists
    s1 = run_batch(dict(cfg(rounds=12), replicates=1), runs_dir=tmp_path, purpose="p1 incomplete")
    assert evaluate_p1(Path(s1["run_dir"]))["result"] == "incomplete"


def test_p2_uses_mean_llm_ask_rounds_11_30(tmp_path):
    s = run_batch(dict(cfg(), replicates=3), runs_dir=tmp_path, purpose="p2 test")
    r = evaluate_p2(Path(s["run_dir"]))
    assert r["result"] == "pass" and r["episodes_below_90"] == 3  # fake mean ask over 11-30 is 74.5
    assert evaluate_p2(Path(s["run_dir"]), threshold=70.0)["result"] == "fail"
