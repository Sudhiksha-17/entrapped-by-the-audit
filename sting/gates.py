"""Gate pilot decision rules (prereg/stage2_spec.md section 5), applied to finished pilot run directories.

P1 (X = $98 clears): pass if at least one trade after round 10 in at least 1 of 2 episodes.
P2 (volume cell is low): pass if the mean LLM-seller ask over rounds 11-30 is below $90 in at least 2 of 3 episodes.
Only completed episodes count; failed episodes are reported (a gate with fewer completed episodes than planned is
reported as incomplete, not as pass or fail).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from sting.stage2_measures import price_measures


def _episodes(run_dirs) -> list[dict[str, Any]]:
    dirs = [run_dirs] if isinstance(run_dirs, (str, Path)) else list(run_dirs)
    return [price_measures(p) for d in dirs for p in sorted(Path(d).iterdir())
            if p.is_dir() and (p / "status.json").is_file()]


def evaluate_p1(run_dir, planned: int = 2) -> dict[str, Any]:
    eps = _episodes(run_dir)
    done = [e for e in eps if e["status"] == "completed"]
    hits = [e for e in done if e["trades_after_round_10"] > 0]
    result = "incomplete" if len(done) < planned else ("pass" if len(hits) >= 1 else "fail")
    return {"gate": "P1", "result": result, "completed": len(done), "planned": planned,
            "episodes_with_trade_after_round_10": len(hits),
            "trades_after_round_10": {e["replicate_id"]: e["trades_after_round_10"] for e in eps}}


def evaluate_p2(run_dir, planned: int = 3, threshold: float = 90.0) -> dict[str, Any]:
    eps = _episodes(run_dir)
    done = [e for e in eps if e["status"] == "completed"]
    low = [e for e in done if e["outcome"] is not None and e["outcome"] < threshold]
    result = "incomplete" if len(done) < planned else ("pass" if len(low) >= 2 else "fail")
    return {"gate": "P2", "result": result, "completed": len(done), "planned": planned,
            "episodes_below_90": len(low), "outcomes": {e["replicate_id"]: e["outcome"] for e in eps}}
