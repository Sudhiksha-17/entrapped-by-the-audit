"""Part 2(c) hand-check agreement (human messages 86 and 95; I-072). Exploratory, post hoc. No API calls.

The 30 sentences drawn at random (seed 20261025) from the classified private-note sentences mentioning Seller C, with
the keyword classification (`price_related`, `message_related`) and the human's marks (`your_price_related`,
`your_message_related`; committed file, hash in D-142). Per type: raw agreement, Cohen's kappa with a percentile
bootstrap 95% CI over sentences (sting.stage2_analysis.kappa_with_ci: 10,000 resamples, seed 20261025), the 2 x 2
table, and the keyword rule's precision and recall against the human marks (Wilson 95% CIs).

Usage: python scripts/final_part2_handcheck.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from sting.stage2_analysis import kappa_with_ci, wilson  # noqa: E402

D = REPO / "results" / "study1r" / "exploratory" / "final_part2" / "handcheck"


def main() -> None:
    rows = list(csv.DictReader((D / "HANDCHECK_SENTENCES.csv").open(encoding="utf-8")))
    out = {"label": "exploratory, post hoc (Part 2(c) hand-check; D-142)", "n": len(rows), "types": {}}
    for t in ("price", "message"):
        k = [r[f"{t}_related"] == "True" for r in rows]
        h = [r[f"your_{t}_related"] == "True" for r in rows]
        tp = sum(a and b for a, b in zip(k, h))
        fp = sum(a and not b for a, b in zip(k, h))
        fn = sum(not a and b for a, b in zip(k, h))
        tn = sum(not a and not b for a, b in zip(k, h))
        kap = kappa_with_ci([str(x) for x in k], [str(x) for x in h])
        out["types"][t] = {"raw_agreement": (tp + tn) / len(rows), "kappa": kap,
                           "table": {"keyword_yes_human_yes": tp, "keyword_yes_human_no": fp,
                                     "keyword_no_human_yes": fn, "keyword_no_human_no": tn},
                           "precision": {"k": tp, "n": tp + fp, "value": tp / (tp + fp) if tp + fp else None,
                                         "ci": list(wilson(tp, tp + fp)) if tp + fp else None},
                           "recall": {"k": tp, "n": tp + fn, "value": tp / (tp + fn) if tp + fn else None,
                                      "ci": list(wilson(tp, tp + fn)) if tp + fn else None},
                           "keyword_yes": tp + fp, "human_yes": tp + fn}
    (D / "handcheck_agreement.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    f = lambda v: "n/a" if v is None else f"{v:.3f}"  # noqa: E731
    L = ["# Part 2(c) hand-check agreement (exploratory, post hoc)", "",
         f"30 sentences (random, seed 20261025) from the {''}classified private-note sentences mentioning Seller C; keyword "
         "classification vs the human's marks (committed file, hash in D-142; marked blind to the classification with "
         "`scripts/handcheck_tool.py`). Kappa: percentile bootstrap 95% CI over sentences (10,000 resamples, seed "
         "20261025). Precision and recall of the keyword rule against the human marks: Wilson 95% CIs. Script "
         "`scripts/final_part2_handcheck.py`.", "",
         "| Type | Raw agreement | Kappa (95% CI) | Keyword yes / human yes | Keyword yes, human no | Keyword no, human yes | "
         "Precision (k/n, 95% CI) | Recall (k/n, 95% CI) |", "|---|---|---|---|---|---|---|---|"]
    for t, v in out["types"].items():
        kp, p, r, tb = v["kappa"], v["precision"], v["recall"], v["table"]
        pci = "" if p["ci"] is None else f", {f(p['ci'][0])}-{f(p['ci'][1])}"
        rci = "" if r["ci"] is None else f", {f(r['ci'][0])}-{f(r['ci'][1])}"
        L.append(f"| {t}-related | {v['raw_agreement']:.3f} | {kp['kappa']:.3f} ({kp['ci_low']:.3f}, {kp['ci_high']:.3f}) | "
                 f"{v['keyword_yes']} / {v['human_yes']} | {tb['keyword_yes_human_no']} | {tb['keyword_no_human_yes']} | "
                 f"{f(p['value'])} ({p['k']}/{p['n']}{pci}) | {f(r['value'])} ({r['k']}/{r['n']}{rci}) |")
    (D / "HANDCHECK_AGREEMENT.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
