"""Plan B results (notes/EXPLORATORY_PLAN_B_C.md section B, committed 1e32de1; D-126; human messages 86 Part 5 and 91).
EXPLORATORY, post hoc. No API calls; reads the committed human coding (hashes in D-139) and the separate keys.

Measures, in the plan's order:
1. Label counts (honor, defect, mixed, not_mentioned; Labeler A) for accepting sellers and controls, per cell and pooled.
2. Mean change score (episode level: post rounds 11-30 minus pre rounds 6-9, LLM sellers; frozen Study 1R measures on
   completed episodes via the D-116 staging) and the behavioral acceptance flag (change >= 0.5 x (X - pre)) by label,
   for accepting sellers and controls, with N per label. Both sellers of an episode share its change score and flag.
3. Agreement on the overlapping items (Labeler B's 50% subset, matched to Labeler A's items by replicate id and
   seller): raw agreement and Cohen's kappa with a percentile bootstrap 95% CI over items (10,000 resamples, seed
   20261025; sting.stage2_analysis.kappa_with_ci), plus the 4 x 4 table.
No tests; descriptive only.

Usage: python scripts/study1r_plan_b_results.py <out_dir> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
sys.path.insert(0, str(REPO))
from sting.stage2_analysis import kappa_with_ci  # noqa: E402

LABELS = ("honor", "defect", "mixed", "not_mentioned")
GROUPS = ("accepting", "control")
CELLS = ("4.1-low", "4.1-high")
LAB = REPO / "results" / "study1r" / "labeling"
KEYS = REPO / "results" / "study1r" / "labeling_keys"


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def coded(name: str) -> dict[tuple[str, str], dict]:
    key = json.loads((KEYS / name / "labeling_key.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((LAB / name / "labels_template.csv").open(encoding="utf-8")))
    out = {}
    for r in rows:
        k = key[r["item_id"]]
        out[(k["replicate_id"], k["seller"])] = {**k, "item_id": r["item_id"], "label": r["response"]}
    return out


def mean_ci(v: list[float], rng: np.random.Generator) -> dict:
    a = np.asarray(v, float)
    if a.size == 0:
        return {"n": 0, "mean": None, "ci": [None, None]}
    b = a[rng.integers(0, a.size, (10_000, a.size))].mean(1)
    return {"n": int(a.size), "mean": float(a.mean()), "ci": [float(np.quantile(b, .025)), float(np.quantile(b, .975))]}


def main() -> None:
    out, cy = Path(sys.argv[1]), Path(sys.argv[2])
    logs = [Path(p) for p in sys.argv[3].split(",") if p]
    a, b = coded("plan_b"), coded("plan_b_labeler_b")
    wrap, res = load("study1r_results_completed.py", "w_pbr"), load("study1r_results.py", "r_pbr")
    human, strata, protected = res.verify_labels(Path(sys.argv[4]), Path(sys.argv[5]))
    with tempfile.TemporaryDirectory(prefix="pbr_") as tmp:
        staged, _ = wrap.stage(logs, Path(tmp))
        eps = {e["replicate_id"]: e for e in res.build([cy], staged, human, strata, {}, {}, False, protected)}
    rng = np.random.default_rng(20261025)
    counts = {}
    for g in GROUPS:
        for c in CELLS + ("pooled",):
            sel = [v for v in a.values() if v["group"] == g and (c == "pooled" or v["cell"] == c)]
            counts[f"{g}/{c}"] = {"n": len(sel), **{l: sum(v["label"] == l for v in sel) for l in LABELS}}
    by_label = {}
    for g in GROUPS:
        for l in LABELS:
            sel = [v for v in a.values() if v["group"] == g and v["label"] == l]
            ch = [eps[v["replicate_id"]]["change"] for v in sel]
            fl = [bool(eps[v["replicate_id"]]["behavioral_acceptance"]) for v in sel]
            by_label[f"{g}/{l}"] = {"n_sellers": len(sel), "n_episodes": len({v["replicate_id"] for v in sel}),
                                    "change": mean_ci(ch, rng), "flag_k": sum(fl), "flag_n": len(fl)}
    common = sorted(set(a) & set(b))
    la, lb = [a[k]["label"] for k in common], [b[k]["label"] for k in common]
    kap = kappa_with_ci(la, lb)
    table = {x: {y: sum(1 for p, q in zip(la, lb) if p == x and q == y) for y in LABELS} for x in LABELS}
    result = {"label": "exploratory, post hoc (plan 1e32de1; D-126; coding hashes D-139)",
              "items": {"labeler_a": len(a), "labeler_b": len(b), "overlap": len(common),
                        "b_items_not_in_a": len(set(b) - set(a))},
              "counts_labeler_a": counts, "change_and_flag_by_label_labeler_a": by_label,
              "agreement": {"n": len(common), "raw": sum(p == q for p, q in zip(la, lb)) / len(common),
                            "kappa": kap, "table_a_rows_b_columns": table,
                            "overlap_groups": dict(Counter(a[k]["group"] for k in common))}}
    out.mkdir(parents=True, exist_ok=True)
    (out / "plan_b.json").write_text(json.dumps(result, indent=2, default=float), encoding="utf-8")
    (out / "PLAN_B.md").write_text(report(result), encoding="utf-8")
    print(report(result))


def report(r: dict) -> str:
    L = ["# Plan B: private-plan sincerity (EXPLORATORY, post hoc, descriptive)", "",
         "Plan `notes/EXPLORATORY_PLAN_B_C.md` section B (committed `1e32de1` before any text was seen); D-126. Coding: "
         "Labeler A (34 items) and Labeler B (random 50% subset, 17 items), blind sheets; file hashes in D-139. No tests. "
         "Script `scripts/study1r_plan_b_results.py`. Facts only.", "",
         "## 1. Label counts (Labeler A)", "",
         "| Group / cell | N | honor | defect | mixed | not_mentioned |", "|---|---|---|---|---|---|"]
    for k, v in r["counts_labeler_a"].items():
        L.append(f"| {k} | {v['n']} | " + " | ".join(str(v[l]) for l in LABELS) + " |")
    L += ["", "## 2. Change score and behavioral flag by label (Labeler A)", "",
          "Change score: episode level (post rounds 11-30 minus pre rounds 6-9, LLM sellers), mean with percentile "
          "bootstrap 95% CI over sellers (10,000 resamples, seed 20261025). Both sellers of an episode share its "
          "change score and flag, so N sellers can exceed N episodes. Flag: change >= 0.5 x (X - pre).", "",
          "| Group / label | N sellers | N episodes | Mean change (95% CI) | Behavioral flag |", "|---|---|---|---|---|"]
    for k, v in r["change_and_flag_by_label_labeler_a"].items():
        c = v["change"]
        ch = "n/a" if c["mean"] is None else f"{c['mean']:+.3f} ({c['ci'][0]:+.3f}, {c['ci'][1]:+.3f})"
        L.append(f"| {k} | {v['n_sellers']} | {v['n_episodes']} | {ch} | {v['flag_k']}/{v['flag_n']} |")
    g = r["agreement"]
    k = g["kappa"]
    L += ["", "## 3. Agreement, Labeler A vs Labeler B (overlapping items)", "",
          f"Items: Labeler A {r['items']['labeler_a']}, Labeler B {r['items']['labeler_b']}, overlap {g['n']} "
          f"(matched by replicate id and seller; groups in the overlap {g['overlap_groups']}). Raw agreement "
          f"{g['raw']:.3f}; Cohen's kappa {k['kappa']:.3f} (95% CI {k['ci_low']:.3f}, {k['ci_high']:.3f}; percentile "
          "bootstrap over items, 10,000 resamples, seed 20261025).", "",
          "| Labeler A \\ Labeler B | " + " | ".join(LABELS) + " |", "|---|" + "---|" * len(LABELS)]
    for x, row in g["table_a_rows_b_columns"].items():
        L.append(f"| {x} | " + " | ".join(str(row[y]) for y in LABELS) + " |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
