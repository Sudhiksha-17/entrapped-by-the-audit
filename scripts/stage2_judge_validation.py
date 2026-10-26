"""Judge validation against the human's blind labels (human messages 31 and 33; prereg section 9; DEV-1 / D-088).

For the original sample (results/stage2/labeling) and the supplementary round-11 sample (results/stage2/labeling_supp):
joins the human labels, the sample key and the judge labels (runs/judge/*/labels.jsonl) by (replicate, seller, round);
computes Cohen's kappa with a 95% bootstrap CI over items (sting.stage2_analysis.kappa_with_ci: 10,000 resamples,
seed 20261025, D-071) for response (full), response collapsed to accept vs not-accept, and awareness; confusion
matrices (rows human, columns judge); counts of the human's labels; and every response disagreement with the human's
note and the judge's evidence. Applies the 0.6 rule on the supplementary sample (D-088). Computes no outcome or test.

Usage: python scripts/stage2_judge_validation.py <out.json> <out.md>
"""
from __future__ import annotations

import csv
import glob
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.judge import ENUMS  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402
from sting.stage2_analysis import kappa_with_ci  # noqa: E402
from sting.stage2_measures import label_status  # noqa: E402

RESULTS = REPO_ROOT / "results" / "stage2"
SAMPLES = {"original": ("labeling", "labeling_key"), "supplementary": ("labeling_supp", "labeling_supp_key")}
RESPONSE = ["accept", "reject", "counter", "noncommittal", "ignored", "not_applicable"]
AWARENESS = ["test_suspicion", "strategic_distrust", "none"]
THRESHOLD = 0.6


def judge_labels() -> dict[tuple, dict]:
    out = {}
    for path in sorted(glob.glob(str(REPO_ROOT / "runs" / "judge" / "*" / "labels.jsonl"))):
        for line in open(path, encoding="utf-8"):
            row = json.loads(line)
            k = (row["replicate_id"], row["seller"], row["round"])
            if k in out:
                raise SystemExit(f"duplicate judge label for {k}")
            out[k] = row
    return out


def confusion(h: list[str], j: list[str], cats: list[str]) -> dict[str, dict[str, int]]:
    c = Counter(zip(h, j))
    return {a: {b: c.get((a, b), 0) for b in cats} for a in cats}


def collapse(xs: list[str]) -> list[str]:
    return ["accept" if x == "accept" else "not_accept" for x in xs]


def sample_report(name: str, judge: dict[tuple, dict]) -> dict:
    sheet_dir, key_dir = SAMPLES[name]
    with open(RESULTS / sheet_dir / "labels_template.csv", newline="", encoding="utf-8") as f:
        human = {r["item_id"]: r for r in csv.DictReader(f)}
    key = json.loads((RESULTS / key_dir / "labeling_key.json").read_text(encoding="utf-8"))
    items, invalid = [], []
    for item_id in sorted(key, key=lambda s: int(s[4:])):
        k = key[item_id]
        j = judge.get((k["replicate_id"], k["seller"], k["round"]))
        if j is None:
            raise SystemExit(f"{name} {item_id}: no judge label")
        if j["status"] != "ok":
            invalid.append(item_id)
            continue
        items.append({"item": item_id, "arm": k["condition"], "cell": k["cell"], "round": k["round"],
                      "h_response": human[item_id]["response"], "h_awareness": human[item_id]["awareness"],
                      "h_note": human[item_id].get("note", ""), "j_response": j["response"],
                      "j_awareness": j["awareness"], "j_engaged": j["engaged_with_message"],
                      "j_evidence": j.get("evidence", []), "j_notes": j.get("notes", "")})
    hr, jr = [i["h_response"] for i in items], [i["j_response"] for i in items]
    ha, ja = [i["h_awareness"] for i in items], [i["j_awareness"] for i in items]
    kappas = {"response": kappa_with_ci(hr, jr), "response_accept_vs_not": kappa_with_ci(collapse(hr), collapse(jr)),
              "awareness": kappa_with_ci(ha, ja)}
    for v in kappas.values():
        v["status"] = label_status(v["kappa"])
    return {
        "n_items": len(key), "n_used": len(items), "judge_invalid_items": invalid,
        "kappa": kappas,
        "confusion_response": confusion(hr, jr, RESPONSE),
        "confusion_response_collapsed": confusion(collapse(hr), collapse(jr), ["accept", "not_accept"]),
        "confusion_awareness": confusion(ha, ja, AWARENESS),
        "human_counts": {"response": {c: hr.count(c) for c in RESPONSE}, "awareness": {c: ha.count(c) for c in AWARENESS}},
        "judge_counts": {"response": {c: jr.count(c) for c in RESPONSE}, "awareness": {c: ja.count(c) for c in AWARENESS},
                         "engaged_with_message": dict(Counter(i["j_engaged"] for i in items))},
        "response_disagreements": [i for i in items if i["h_response"] != i["j_response"]],
    }


def fmt_matrix(m: dict[str, dict[str, int]]) -> list[str]:
    cols = list(next(iter(m.values())))
    lines = ["| human \\ judge | " + " | ".join(cols) + " |", "|---" * (len(cols) + 1) + "|"]
    return lines + [f"| {r} | " + " | ".join(str(m[r][c]) for c in cols) + " |" for r in m]


def main() -> None:
    judge = judge_labels()
    out = {name: sample_report(name, judge) for name in SAMPLES}
    supp = out["supplementary"]["kappa"]
    verbal_ok = supp["response"]["kappa"] >= THRESHOLD
    out["decision_d088"] = {
        "rule": "0.6 rule decided on the supplementary sample (D-088 / DEV-1)",
        "response_kappa": supp["response"]["kappa"], "response_status": supp["response"]["status"],
        "awareness_kappa": supp["awareness"]["kappa"], "awareness_status": supp["awareness"]["status"],
        "t2a_flag": "verbal flag" if verbal_ok else "behavioral flag (preregistered fallback)",
    }
    Path(sys.argv[1]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    lines = ["# Stage 2 judge validation", "", "Generated by `scripts/stage2_judge_validation.py`. No outcome or test computed.", ""]
    for name in SAMPLES:
        r = out[name]
        lines += [f"## {name.capitalize()} sample", "", f"Items {r['n_items']}, used {r['n_used']}, judge invalid: "
                  f"{r['judge_invalid_items'] or 'none'}", "", "| Label | Kappa | 95% CI | Status |", "|---|---|---|---|"]
        for lab, v in r["kappa"].items():
            lines.append(f"| {lab} | {v['kappa']:.3f} | {v['ci_low']:.3f} to {v['ci_high']:.3f} | {v['status']} |")
        lines += ["", f"Human label counts: {r['human_counts']}", f"Judge label counts: {r['judge_counts']}", "",
                  "Response:", ""] + fmt_matrix(r["confusion_response"]) + ["", "Response, accept vs not:", ""] + \
            fmt_matrix(r["confusion_response_collapsed"]) + ["", "Awareness:", ""] + fmt_matrix(r["confusion_awareness"]) + \
            ["", "Response disagreements:", ""]
        for d in r["response_disagreements"]:
            lines.append(f"- {d['item']} ({d['arm']}, {d['cell']}, round {d['round']}): human {d['h_response']} "
                         f"(note: {d['h_note'] or 'none'}); judge {d['j_response']} (engaged {d['j_engaged']}); "
                         f"evidence: {json.dumps(d['j_evidence'], ensure_ascii=False)}")
        lines.append("")
    lines += ["## D-088 decision", "", json.dumps(out["decision_d088"], indent=2)]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
