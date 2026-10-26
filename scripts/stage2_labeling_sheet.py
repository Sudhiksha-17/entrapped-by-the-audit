"""Stage 2 blind labeling sheet for judge validation (human message 25; prereg section 9).

Pools every post-t0 seller-round of the LLM sellers in completed message-arm episodes (sting.judge.judge_items)
across the given campaign invocations, draws 30 with sting.stage2_measures.stratified_sample (defaults as frozen:
strata by arm and cell, Offer strata draw half their quota from rounds 11-15, seed "judge-validation"), and
shuffles them with blind_labeling_sheet (arm, cell, replicate, seller, round and model hidden). The key goes to a
separate directory. Read-only on runs; no API calls; does not run the judge; never reads asks, bids, prices,
trades or flags. It prints only pool and sample counts per stratum, never item text.

Usage: python scripts/stage2_labeling_sheet.py <sheet_dir> <key_dir> <campaign.yaml> <campaign.json> [...]
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import yaml  # noqa: E402

from sting.judge import ENUMS, SELLER_FIELDS, judge_items  # noqa: E402
from sting.stage2_measures import blind_labeling_sheet, stratified_sample  # noqa: E402

N_ITEMS = 30
LABELS = ("response", "awareness")


def pool(campaign_yaml: Path, campaign_logs: list[Path]) -> list[dict]:
    arms = {a["name"]: a for a in yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))["arms"]}
    items = []
    for log_path in campaign_logs:
        log = json.loads(log_path.read_text(encoding="utf-8"))
        for name, info in log["arms"].items():
            if arms[name]["arm"] == "silent":
                continue
            run_dir = Path(info["run_dir"])
            cfg = json.loads((run_dir / "run_config.json").read_text(encoding="utf-8"))["config"]
            completed = {p.name for p in run_dir.iterdir() if p.is_dir() and json.loads(
                (p / "status.json").read_text(encoding="utf-8"))["status"] == "completed"}
            for it in judge_items(run_dir):
                if it["replicate_id"] in completed:
                    items.append({**it, "condition": arms[name]["arm"], "cell": arms[name]["cell"], "arm": name,
                                  "model": cfg["sellers"][0]["model"]})
    return items


def write_sheet(sheet: list[dict], key: dict, sheet_dir: Path, key_dir: Path) -> None:
    """Sheet (md, json), blank labels template and the key (in its own directory)."""
    if sheet_dir.resolve() == key_dir.resolve():
        raise SystemExit("sheet and key must be in separate directories")
    sheet_dir.mkdir(parents=True, exist_ok=True)
    key_dir.mkdir(parents=True, exist_ok=True)
    (sheet_dir / "labeling_sheet.json").write_text(json.dumps(sheet, indent=2), encoding="utf-8")
    with (sheet_dir / "labels_template.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["item_id", *LABELS])
        for s in sheet:
            w.writerow([s["item_id"], "", ""])
    lines = ["# Stage 2 judge validation: blind labeling sheet", "",
             f"{len(sheet)} seller-rounds, shuffled; arm, cell, model, replicate, seller and round are hidden (key "
             "stored separately; do not open it before labeling). The sting's message can still reveal the arm.", "",
             "Label each item in `labels_template.csv`:"]
    lines += [f"- `{lab}`: one of {', '.join(sorted(ENUMS[lab]))}" for lab in LABELS]
    for s in sheet:
        lines += ["", "---", "", f"## {s['item_id']}", ""]
        if s.get("episode"):  # Study 1R human-coding backup: opaque episode id (episode mode of sting.label_tool)
            lines += ["**Episode:**", "", s["episode"], ""]
        lines += ["**Sting message:**", "", f"> {s['sting_message']}", ""]
        for k in SELLER_FIELDS:
            if k in s["fields"]:  # Study 1R public view: message_to_sellers only (Study 1 items carry all six)
                lines += [f"**{k}:**", "", str(s["fields"].get(k) or ""), ""]
    (sheet_dir / "LABELING_SHEET.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (key_dir / "labeling_key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    (key_dir / "README.md").write_text(
        "# Labeling key\n\nMaps sheet item ids to hidden attributes. Do not open before hand-labeling is finished.\n",
        encoding="utf-8")


def main() -> None:
    sheet_dir, key_dir, campaign_yaml = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    logs = [Path(p) for p in sys.argv[4:]]
    items = pool(campaign_yaml, logs)
    sample = stratified_sample(items, N_ITEMS)
    sheet, key = blind_labeling_sheet(sample)
    write_sheet(sheet, key, sheet_dir, key_dir)
    meta = {"n_items": len(sheet), "pool_per_stratum": {f"{c}|{cell}": n for (c, cell), n in sorted(
        Counter((i["condition"], i["cell"]) for i in items).items())},
        "sample_per_stratum": {f"{c}|{cell}": n for (c, cell), n in sorted(
            Counter((i["condition"], i["cell"]) for i in sample).items())},
        "sample_in_rounds_11_15_offer": sum(1 for i in sample if i["condition"] == "offer" and 11 <= i["round"] <= 15),
        "campaign_logs": [str(p) for p in logs], "sampling": "stratified_sample defaults (n=30, "
        "first_exposure_share=0.5, rounds 11-15, seed judge-validation); order seed judge-validation-order"}
    (sheet_dir / "sampling.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
