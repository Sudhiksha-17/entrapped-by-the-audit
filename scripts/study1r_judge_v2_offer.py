"""Study 1R judge v2 run: prompt r1 with gpt-4.1, public view, on every Offer-arm public message in rounds 11-30 (one
judge run per Offer arm-run). In 4.1-low and 4.1-high it is the option A screener (human message 64): its accept and
conditional_accept labels select the verification set the entrant codes; it is not the verbal measure (no judge passed
G3). In every Offer arm it feeds the exploratory headline figure's v2-read acceptance. No private-view judge.

Usage: python scripts/study1r_judge_v2_offer.py <campaign.yaml> <campaign.json>[,...] [--estimate-only] [--approve-cost]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from study1r_validation import candidate_cfg  # noqa: E402

from sting.judge_v2 import estimate_v2, items_v2, run_judge_v2  # noqa: E402

CANDIDATE = "gpt-4.1"


def offer_runs(campaign_yaml: Path, logs: list[Path]) -> list[Path]:
    arms = {a["name"]: a for a in yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))["arms"]}
    return [Path(info["run_dir"]) for log in logs
            for name, info in json.loads(log.read_text(encoding="utf-8"))["arms"].items() if arms[name]["arm"] == "offer"]


def main() -> None:
    runs = offer_runs(Path(sys.argv[1]), [Path(p) for p in sys.argv[2].split(",")])
    cfg = candidate_cfg(CANDIDATE)
    if "--estimate-only" in sys.argv:
        items = [i for r in runs for i in items_v2(r, "public")]
        print(f"{len(runs)} Offer arm-runs, {len(items)} public messages; estimated ${estimate_v2(items, cfg):.2f}")
        return
    for r in runs:
        s = run_judge_v2(r, "public", cfg, f"Study 1R exploratory judge v2 comparison ({CANDIDATE}), {r.name}",
                         approve_cost="--approve-cost" in sys.argv)
        print(s["run_dir"], s["ok"], s["invalid"])


if __name__ == "__main__":
    main()
