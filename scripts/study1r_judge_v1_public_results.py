"""Exploratory robustness check results (human message 93, item 3): judge v1 on public messages only vs all fields.

Per group (mini, volume, CEO), the share of completed Offer episodes counted as accepting under the frozen headline
rule (an episode counts if any seller-round, rounds 11-30, is labeled `accept` by judge v1), with Wilson 95% CIs,
for the all-fields run (`..._v1_comparison_offer_6250d4`) and the public-only run; and on the 40 validation items,
Cohen's kappa against the adjudicated gold (full response label and acceptance: judge `accept` vs gold accept or
conditional_accept), with bootstrap 95% CIs (sting.stage2_analysis.kappa_with_ci). Completed episodes via the D-116
staging. No API calls.

Usage: python scripts/study1r_judge_v1_public_results.py <out_dir> <campaign.yaml> <campaign.json>[,...]
           <all_fields_offer_run> <public_offer_run> <all_fields_validation_run> <public_validation_run>
"""
from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
sys.path.insert(0, str(REPO))
from sting.stage2_analysis import kappa_with_ci, wilson  # noqa: E402

GROUP = {"mini-low": "mini group (gpt-4.1-mini, default)", "4.1-low": "volume group (gpt-4.1, volume prompt)",
         "4.1-high": "CEO group (gpt-4.1, CEO prompt)"}


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def labels(run: Path) -> dict:
    out, invalid = {}, 0
    for line in (run / "labels.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        if r.get("status") == "ok":
            out[(r["replicate_id"], r["seller"], int(r["round"]))] = r["response"]
        else:
            invalid += 1
    return {"labels": out, "invalid": invalid}


def main() -> None:
    out, cy = Path(sys.argv[1]), Path(sys.argv[2])
    logs = [Path(p) for p in sys.argv[3].split(",") if p]
    runs = {"all_fields": Path(sys.argv[4]), "public_only": Path(sys.argv[5])}
    vruns = {"all_fields": Path(sys.argv[6]), "public_only": Path(sys.argv[7])}
    wrap, res = load("study1r_results_completed.py", "w_v1p"), load("study1r_results.py", "r_v1p")
    with tempfile.TemporaryDirectory(prefix="v1p_") as tmp:
        staged, excluded = wrap.stage(logs, Path(tmp))
        eps = [e for e in res.build([cy], staged, {}, {}, {}, {}, False, frozenset()) if e["arm"] == "offer"]
    lab = {k: labels(p) for k, p in runs.items()}
    result = {"label": "exploratory, post hoc (robustness check; human message 93)",
              "invalid_outputs": {k: v["invalid"] for k, v in lab.items()}, "groups": {}, "validation": {}}
    for cell, name in GROUP.items():
        ce = [e["replicate_id"] for e in eps if e["cell"] == cell]
        row = {"n": len(ce)}
        for view, L in lab.items():
            acc = {rid for (rid, s, r), v in L["labels"].items() if v == "accept" and 11 <= r <= 30}
            k = sum(rid in acc for rid in ce)
            lo, hi = wilson(k, len(ce))
            row[view] = {"k": k, "share": k / len(ce), "ci": [lo, hi]}
        result["groups"][name] = row
    key = json.loads((REPO / "results/study1r/labeling_keys/validation/labeling_key.json").read_text(encoding="utf-8"))
    gold = {r["item_id"]: r["response"] for r in
            csv.DictReader((REPO / "results/study1r/labeling/validation/adjudication.csv").open(encoding="utf-8"))}
    g = {(k["replicate_id"], k["seller"], int(k["round"])): gold[i] for i, k in key.items()}
    for view, run in vruns.items():
        L = labels(run)
        ks = [k for k in g if k in L["labels"]]
        j, h = [L["labels"][k] for k in ks], [g[k] for k in ks]
        result["validation"][view] = {
            "n": len(ks), "invalid": L["invalid"], "full_label": kappa_with_ci(j, h),
            "acceptance": kappa_with_ci([str(x == "accept") for x in j], [str(x in ("accept", "conditional_accept")) for x in h]),
            "judge_accept": sum(x == "accept" for x in j), "gold_acceptances": sum(x in ("accept", "conditional_accept") for x in h)}
    out.mkdir(parents=True, exist_ok=True)
    (out / "v1_public.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    w = lambda d: f"{d['k']}/{n} = {d['share']:.3f} ({d['ci'][0]:.3f}, {d['ci'][1]:.3f})"  # noqa: E731
    Lm = ["# Judge v1 on public messages only (EXPLORATORY robustness check)", "",
          "Human message 93, item 3. Frozen Study 1 judge (prompt, gpt-4.1-mini, temperature 0); only the input fields "
          "changed (public message only; the five private fields empty). Completed Offer episodes; an episode counts "
          "as accepting if any seller-round in rounds 11-30 is labeled `accept`. Wilson 95% CIs. Script "
          "`scripts/study1r_judge_v1_public_results.py`. Facts only.", "",
          f"Invalid judge outputs: all fields {result['invalid_outputs']['all_fields']}, public only "
          f"{result['invalid_outputs']['public_only']} (of 5,040 seller-rounds each).", "",
          "| Group | N Offer episodes | All fields | Public message only |", "|---|---|---|---|"]
    for name, row in result["groups"].items():
        n = row["n"]
        Lm.append(f"| {name} | {n} | {w(row['all_fields'])} | {w(row['public_only'])} |")
    Lm += ["", "## Validation items (40), against the adjudicated gold", "",
           "Kappa with percentile bootstrap 95% CI over items. Judge v1's label set has no not_applicable and no "
           "conditional_accept; the gold has 10 not_applicable items (Sham).", "",
           "| View | n | Invalid | Full-label kappa (95% CI) | Acceptance kappa (95% CI) | Judge accept | Gold acceptances |",
           "|---|---|---|---|---|---|---|"]
    for view, v in result["validation"].items():
        f, a = v["full_label"], v["acceptance"]
        Lm.append(f"| {view.replace('_', ' ')} | {v['n']} | {v['invalid']} | {f['kappa']:.3f} ({f['ci_low']:.3f}, "
                  f"{f['ci_high']:.3f}) | {a['kappa']:.3f} ({a['ci_low']:.3f}, {a['ci_high']:.3f}) | "
                  f"{v['judge_accept']} | {v['gold_acceptances']} |")
    (out / "V1_PUBLIC.md").write_text("\n".join(Lm) + "\n", encoding="utf-8")
    print("\n".join(Lm))


if __name__ == "__main__":
    main()
