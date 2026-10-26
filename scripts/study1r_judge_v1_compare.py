"""Study 1R judge v1 comparison (exploratory; human message 51, 3e). Runs the frozen Study 1 judge (sting/judge.py,
sting/prompts/judge_prompt.jinja2, configs/judge.yaml: gpt-4.1-mini, temperature 0) on Study 1R seller-rounds, exactly
as in Study 1: all six seller text fields and the sting message the seller saw that round.

  estimate  <campaign.yaml> <campaign.json>[,...]          cost estimate for all Offer-arm seller-rounds 11-30
  run       <campaign.yaml> <campaign.json>[,...] [--approve-cost]
  run-validation <key_dir> <runs_root> [--approve-cost]    the 40 validation items; refuses unless the validation
                                                            adjudication file exists (after the validation labeling is adjudicated)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.judge import estimate, load_judge_config, run_judge  # noqa: E402
from sting.judge_v2 import items_v2  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402


def merge_views(run_dir: Path) -> list[dict]:
    pub = {(i["replicate_id"], i["seller"], i["round"]): i for i in items_v2(run_dir, "public")}
    out = []
    for i in items_v2(run_dir, "private"):
        k = (i["replicate_id"], i["seller"], i["round"])
        out.append({"replicate_id": k[0], "seller": k[1], "round": k[2], "sting_message": i["sting_message"],
                    "fields": {**i["fields"], **pub[k]["fields"]}})
    return out


def offer_items(campaign_yaml: Path, logs: list[Path]) -> list[dict]:
    arms = {a["name"]: a for a in yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))["arms"]}
    items = []
    for log in logs:
        for name, info in json.loads(log.read_text(encoding="utf-8"))["arms"].items():
            if arms[name]["arm"] == "offer":
                items += merge_views(Path(info["run_dir"]))
    return items


def validation_items(key_dir: Path, runs_root: Path) -> list[dict]:
    if not (REPO_ROOT / "results" / "study1r" / "labeling" / "validation" / "adjudication.csv").is_file():
        raise SystemExit("validation labeling not adjudicated yet; the v1 comparison on validation items runs after G3")
    key = json.loads((key_dir / "labeling_key.json").read_text(encoding="utf-8"))
    wanted = {(k["replicate_id"], k["seller"], k["round"]) for k in key.values()}
    runs = {p.parent for k in key.values() for p in runs_root.glob(f"*/{k['replicate_id']}")}
    return [i for r in runs for i in merge_views(r) if (i["replicate_id"], i["seller"], i["round"]) in wanted]


def main() -> None:
    cmd, approve = sys.argv[1], "--approve-cost" in sys.argv
    if cmd in ("estimate", "run"):
        items = offer_items(Path(sys.argv[2]), [Path(p) for p in sys.argv[3].split(",")])
        label, stage = "study1r_v1_comparison_offer", "study1r"
    elif cmd == "run-validation":
        items, label, stage = validation_items(Path(sys.argv[2]), Path(sys.argv[3])), "study1r_v1_comparison_validation", "study1r_pilot"
    else:
        raise SystemExit("command must be estimate, run or run-validation")
    if cmd == "estimate":
        print(f"{len(items)} items; estimated ${estimate(items, load_judge_config()):.4f}")
        return
    print(json.dumps(run_judge(None, f"Study 1R judge v1 comparison ({label})", approve_cost=approve, items=items,
                               items_label=label, items_stage=stage), indent=2, default=str))


if __name__ == "__main__":
    main()
