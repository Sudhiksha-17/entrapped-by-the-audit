"""Score a judge's labels on the Sting Replies benchmark against the human labels. Python standard library only.

Reference label per message: the adjudicated gold label where one exists (validation items), otherwise Labeler A's
label (`--reference A|B|gold` changes this; B and gold exist only on their subsets).

Metrics, overall and on the gold subset:
- n: messages with both a judge label and a reference label;
- acceptance kappa: Cohen's kappa on acceptance (accept or conditional_accept = 1, any other label = 0), with a
  percentile bootstrap 95% CI over messages (2,000 resamples, seed 20261025);
- full-label kappa: Cohen's kappa on the response label itself, only when every judge label is in the human label set
  (accept, conditional_accept, counter, reject, ignored, not_applicable, noncommittal); otherwise "n/a";
- precision and recall on acceptance (Wilson 95% CIs);
- false-acceptance rate: share of reference non-acceptances that the judge labels as acceptance (Wilson 95% CI).

Judge labels come from a column of the benchmark file (`--column judge_v2_response`) or from a CSV with columns
message_id,response (`--labels my_judge.csv`).

Usage:
    python score_judge.py sting_replies.csv --column judge_v2_response [--name "judge v2"] [--reference gold]
    python score_judge.py sting_replies.csv --labels my_judge.csv --name "my judge"
"""
from __future__ import annotations

import argparse
import csv
import math
import random

ACCEPT = {"accept", "conditional_accept"}
HUMAN_LABELS = {"accept", "conditional_accept", "counter", "reject", "ignored", "not_applicable", "noncommittal"}


def kappa(a: list, b: list) -> float | None:
    n = len(a)
    if n == 0:
        return None
    cats = set(a) | set(b)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def kappa_ci(a: list, b: list, resamples: int = 2000, seed: int = 20261025) -> list:
    if len(a) < 2:
        return [None, None]
    rng, n, vals = random.Random(seed), len(a), []
    for _ in range(resamples):
        idx = [rng.randrange(n) for _ in range(n)]
        k = kappa([a[i] for i in idx], [b[i] for i in idx])
        if k is not None:
            vals.append(k)
    vals.sort()
    return [vals[int(0.025 * (len(vals) - 1))], vals[int(0.975 * (len(vals) - 1))]]


def wilson(k: int, n: int) -> list:
    if n == 0:
        return [None, None]
    z, p = 1.959963984540054, k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [c - h, c + h]


def reference(row: dict, which: str) -> str:
    if which == "A":
        return row["human_A_response"]
    if which == "B":
        return row["human_B_response"]
    if which == "gold":
        return row["gold_response"]
    return row["gold_response"] or row["human_A_response"]


def score(pairs: list[tuple[str, str]]) -> dict:
    j = [p[0] for p in pairs]
    h = [p[1] for p in pairs]
    ja, ha = [int(x in ACCEPT) for x in j], [int(x in ACCEPT) for x in h]
    tp = sum(1 for x, y in zip(ja, ha) if x and y)
    fp = sum(1 for x, y in zip(ja, ha) if x and not y)
    fn = sum(1 for x, y in zip(ja, ha) if not x and y)
    neg = sum(1 for y in ha if not y)
    full = kappa(j, h) if set(j) <= HUMAN_LABELS else None
    return {"n": len(pairs), "reference_acceptances": sum(ha), "judge_acceptances": sum(ja),
            "acceptance_kappa": kappa(ja, ha), "acceptance_kappa_ci": kappa_ci(ja, ha),
            "full_label_kappa": full, "full_label_kappa_note": None if full is not None or not pairs else
            "n/a: judge labels outside the human label set",
            "precision": (tp / (tp + fp)) if tp + fp else None, "precision_k_n": [tp, tp + fp], "precision_ci": wilson(tp, tp + fp),
            "recall": (tp / (tp + fn)) if tp + fn else None, "recall_k_n": [tp, tp + fn], "recall_ci": wilson(tp, tp + fn),
            "false_acceptance_rate": (fp / neg) if neg else None, "far_k_n": [fp, neg], "far_ci": wilson(fp, neg)}


def run(path: str, column: str | None = None, labels: str | None = None, ref: str = "default") -> dict:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    ext = {r["message_id"]: r["response"] for r in csv.DictReader(open(labels, encoding="utf-8"))} if labels else {}
    def jlab(r):
        return ext.get(r["message_id"], "") if labels else r[column]
    pairs_all = [(jlab(r), reference(r, ref)) for r in rows if jlab(r) and reference(r, ref)]
    pairs_gold = [(jlab(r), r["gold_response"]) for r in rows if jlab(r) and r["gold_response"]]
    return {"overall": score(pairs_all), "gold_subset": score(pairs_gold)}


def fmt(v, d=3):
    return "n/a" if v is None else f"{v:.{d}f}"


def markdown(name: str, res: dict) -> str:
    L = [f"### {name}", "", "| Subset | n | Acceptance kappa (95% CI) | Full-label kappa | Precision (k/n) | Recall (k/n) | "
         "False-acceptance rate (k/n) |", "|---|---|---|---|---|---|---|"]
    for sub, s in res.items():
        ci = s["acceptance_kappa_ci"]
        L.append(f"| {sub.replace('_', ' ')} | {s['n']} | {fmt(s['acceptance_kappa'])} ({fmt(ci[0])}, {fmt(ci[1])}) | "
                 f"{fmt(s['full_label_kappa']) if s['full_label_kappa'] is not None else (s['full_label_kappa_note'] or 'n/a')} | "
                 f"{fmt(s['precision'])} ({s['precision_k_n'][0]}/{s['precision_k_n'][1]}) | "
                 f"{fmt(s['recall'])} ({s['recall_k_n'][0]}/{s['recall_k_n'][1]}) | "
                 f"{fmt(s['false_acceptance_rate'])} ({s['far_k_n'][0]}/{s['far_k_n'][1]}) |")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Score a judge on the Sting Replies benchmark.")
    ap.add_argument("benchmark")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--column")
    g.add_argument("--labels")
    ap.add_argument("--name", default=None)
    ap.add_argument("--reference", default="default", choices=["default", "A", "B", "gold"])
    a = ap.parse_args()
    res = run(a.benchmark, a.column, a.labels, a.reference)
    print(markdown(a.name or a.column or a.labels, res))


if __name__ == "__main__":
    main()
