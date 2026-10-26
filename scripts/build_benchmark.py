"""Build the "Sting Replies" benchmark in release/benchmark/ (human message 93, item 4). No new labeling; no API calls.

One row per human-labeled seller public message:
- dev: the 30 judge-development items (pilot episodes; Labeler A);
- validation: the 40 validation items (pilot episodes; Labeler A pass 1, Labeler B pass 2, adjudicated gold);
- main_verification, main_audit_flagged, main_audit_unflagged: the coded items of the main-study verify sheet
  (Labeler A; Labeler B on its 32 verification items). Verification messages dropped uncoded by the hidden stopping
  rule are not included (no human label).
Only chosen label values are copied (response, awareness). No coder free text: the note, note_A, note_B, reason
and unresolved columns are never read into the output.

Judge labels (response) are joined by (episode, seller, round): judge v1 all fields (Study 1 judge, gpt-4.1-mini;
runs `..._v1_comparison_validation_f0fd9b`, `..._v1_comparison_offer_6250d4`; none for dev), judge v1 public only
(runs `..._v1_public_validation_a4b0fa` and the public-only Offer run; none for dev), judge v2 (prompt r1, gpt-4.1,
public view; dev run `..._dev_gpt-4.1_7b5396`, validation run `..._validation_gpt-4.1_652a99`, main study: the 27
screener runs). An invalid judge output is left empty.

Writes release/benchmark/sting_replies.csv, README.md (datasheet with counts), score_judge.py (copied from
scripts/benchmark/score_judge.py) and LICENSE (CC BY 4.0 notice).

Usage: python scripts/build_benchmark.py <v1_public_offer_run_dir>
"""
from __future__ import annotations

import csv
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LAB, KEYS, JUDGE = REPO / "results/study1r/labeling", REPO / "results/study1r/labeling_keys", REPO / "runs/judge"
OUT = REPO / "release" / "benchmark"
GROUP = {"mini-low": "mini", "4.1-low": "volume", "4.1-high": "CEO"}
COLUMNS = ["message_id", "source", "group", "arm", "round", "episode_id", "seller", "sting_message", "seller_message",
           "human_A_response", "human_A_awareness", "human_B_response", "human_B_awareness", "gold_response",
           "gold_awareness", "judge_v1_allfields_response", "judge_v1_public_response", "judge_v2_response"]
SCREENER = re.compile(r"judgev2-public_\d{8}T\d{6}Z_study1r_(mini-low|4\.1-low|4\.1-high)_offer_")


def sheet(name: str) -> dict[tuple, dict]:
    key = json.loads((KEYS / name / "labeling_key.json").read_text(encoding="utf-8"))
    items = {i["item_id"]: i for i in json.loads((LAB / name / "labeling_sheet.json").read_text(encoding="utf-8"))}
    labels = {r["item_id"]: r for r in csv.DictReader((LAB / name / "labels_template.csv").open(encoding="utf-8"))}
    out = {}
    for iid, k in key.items():
        lab = labels[iid]
        out[(k["replicate_id"], k["seller"], int(k["round"]))] = {
            "item_id": iid, "cell": k["cell"], "arm": k["condition"], "stratum": k.get("stratum"),
            "sting_message": items[iid]["sting_message"],
            "seller_message": items[iid]["fields"].get("message_to_sellers") or "",
            "response": lab["response"], "awareness": lab["awareness"]}       # chosen values only
    return out


def judge(dirs: list[Path]) -> dict[tuple, str]:
    out = {}
    for d in dirs:
        for line in (d / "labels.jsonl").read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r.get("status") == "ok":
                out[(r["replicate_id"], r["seller"], int(r["round"]))] = r["response"]
    return out


def one(pattern: str) -> Path:
    found = sorted(JUDGE.glob(pattern))
    if len(found) != 1:
        raise SystemExit(f"expected one judge run for {pattern}, found {[p.name for p in found]}")
    return found[0]


def main() -> None:
    v1_public_offer = Path(sys.argv[1])
    v1_all = judge([one("*_judge_study1r_v1_comparison_validation_f0fd9b"), one("*_judge_study1r_v1_comparison_offer_6250d4")])
    v1_pub = judge([one("*_judge_study1r_v1_public_validation_a4b0fa"), v1_public_offer])
    v2 = judge([one("*_judgev2-public_study1r_dev_gpt-4.1_7b5396"), one("*_judgev2-public_study1r_validation_gpt-4.1_652a99")]
               + [d for d in sorted(JUDGE.iterdir()) if SCREENER.search(d.name)])
    gold = {r["item_id"]: r for r in csv.DictReader((LAB / "validation" / "adjudication.csv").open(encoding="utf-8"))}
    rows = []
    dev = sheet("dev")
    for k, v in sorted(dev.items()):
        rows.append(("dev", k, v, None, None))
    va, vb = sheet("validation"), sheet("validation_pass2")
    for k, v in sorted(va.items()):
        g = gold[v["item_id"]]
        rows.append(("validation", k, v, vb[k], {"response": g["response"], "awareness": g["awareness"]}))
    ma, mb = sheet("main/verify"), sheet("main/verify_B")
    for k, v in sorted(ma.items()):
        if not v["response"]:
            continue                                   # dropped by the stopping rule: no human label
        src = "main_verification" if v["stratum"] == "verification" else f"main_{v['stratum']}"
        rows.append((src, k, v, mb.get(k), None))
    order = {"dev": 0, "validation": 1, "main_verification": 2, "main_audit_flagged": 3, "main_audit_unflagged": 4}
    rows.sort(key=lambda r: (order[r[0]], r[1]))
    out_rows = []
    for n, (src, k, a, b, g) in enumerate(rows, 1):
        out_rows.append({
            "message_id": f"SR{n:04d}", "source": src, "group": GROUP[a["cell"]], "arm": a["arm"], "round": k[2],
            "episode_id": k[0], "seller": k[1], "sting_message": a["sting_message"], "seller_message": a["seller_message"],
            "human_A_response": a["response"], "human_A_awareness": a["awareness"],
            "human_B_response": b["response"] if b else "", "human_B_awareness": b["awareness"] if b else "",
            "gold_response": g["response"] if g else "", "gold_awareness": g["awareness"] if g else "",
            "judge_v1_allfields_response": v1_all.get(k, ""), "judge_v1_public_response": v1_pub.get(k, ""),
            "judge_v2_response": v2.get(k, "")})
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "sting_replies.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(out_rows)
    shutil.copyfile(REPO / "scripts" / "benchmark" / "score_judge.py", OUT / "score_judge.py")
    (OUT / "LICENSE").write_text(
        "The Sting Replies benchmark data (sting_replies.csv, README.md, BASELINES.md) are licensed under the Creative "
        "Commons Attribution 4.0 International License (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/\n"
        "score_judge.py is licensed under the MIT License (see the repository LICENSE).\n", encoding="utf-8")
    stats = {"n": len(out_rows),
             "by_source": dict(Counter(r["source"] for r in out_rows)),
             "by_group": dict(Counter(r["group"] for r in out_rows)),
             "by_arm": dict(Counter(r["arm"] for r in out_rows)),
             "human_A_response": dict(Counter(r["human_A_response"] for r in out_rows)),
             "human_B_response": dict(Counter(r["human_B_response"] for r in out_rows if r["human_B_response"])),
             "gold_response": dict(Counter(r["gold_response"] for r in out_rows if r["gold_response"])),
             "with_B": sum(bool(r["human_B_response"]) for r in out_rows),
             "with_gold": sum(bool(r["gold_response"]) for r in out_rows),
             "judge_coverage": {c: sum(bool(r[c]) for r in out_rows) for c in COLUMNS if c.startswith("judge_")},
             "group_by_source": {s: dict(Counter(r["group"] for r in out_rows if r["source"] == s))
                                 for s in order}}
    (OUT / "benchmark_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(json.dumps(stats, indent=1))


if __name__ == "__main__":
    main()
