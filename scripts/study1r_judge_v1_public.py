"""Exploratory robustness check (human message 93, item 3): the frozen Study 1 judge (judge v1; sting/judge.py,
sting/prompts/judge_prompt.jinja2, configs/judge.yaml: gpt-4.1-mini, temperature 0) rerun on PUBLIC MESSAGES ONLY.

Only the input fields change: each item keeps the sting message the seller saw and passes only `message_to_sellers`;
the five private fields (reflection, plan_for_this_hour, plan_for_message, new_memory, scratch_pad_update) render as
empty strings, as the frozen template does for a missing field. Items, prompt, model, config and parser are the
frozen ones (item lists from scripts/study1r_judge_v1_compare.py: every Offer-arm seller-round 11-30 of the Study 1R
main campaign logs, and the 40 validation items).

  estimate        <campaign.yaml> <campaign.json>[,...] <key_dir> <runs_root>
  run             <campaign.yaml> <campaign.json>[,...] [--approve-cost]
  run-validation  <key_dir> <runs_root> [--approve-cost]
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS.parent))
from sting.judge import estimate, load_judge_config, run_judge  # noqa: E402


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


V1 = load("study1r_judge_v1_compare.py", "v1cmp")


def public_only(items: list[dict]) -> list[dict]:
    return [{**i, "fields": {"message_to_sellers": i["fields"].get("message_to_sellers")}} for i in items]


def main() -> None:
    cmd, approve = sys.argv[1], "--approve-cost" in sys.argv
    if cmd == "estimate":
        offer = public_only(V1.offer_items(Path(sys.argv[2]), [Path(p) for p in sys.argv[3].split(",")]))
        val = public_only(V1.validation_items(Path(sys.argv[4]), Path(sys.argv[5])))
        cfg = load_judge_config()
        print(json.dumps({"offer_items": len(offer), "offer_estimate_usd": round(estimate(offer, cfg), 4),
                          "validation_items": len(val), "validation_estimate_usd": round(estimate(val, cfg), 4)}))
        return
    if cmd == "run":
        items = public_only(V1.offer_items(Path(sys.argv[2]), [Path(p) for p in sys.argv[3].split(",")]))
        label, stage = "study1r_v1_public_offer", "study1r"
    elif cmd == "run-validation":
        items = public_only(V1.validation_items(Path(sys.argv[2]), Path(sys.argv[3])))
        label, stage = "study1r_v1_public_validation", "study1r_pilot"
    else:
        raise SystemExit("command must be estimate, run or run-validation")
    print(json.dumps(run_judge(None, f"Exploratory robustness: judge v1 on public messages only ({label}; human message 93)",
                               approve_cost=approve, items=items, items_label=label, items_stage=stage),
                     indent=2, default=str))


if __name__ == "__main__":
    main()
