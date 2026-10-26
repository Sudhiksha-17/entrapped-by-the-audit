"""Study 1R-D analysis (prereg_study1r/AMENDMENT_1RD.md section 6). No API calls.

Completed episodes only, through the completed-episodes wrapper's staging (scripts/study1r_results_completed.py `stage`
and `check`; the run stops unless the excluded set equals --expect-excluded / --rc-expect-excluded). Per-episode records
and descriptive helpers are those of the frozen Study 1R-C analysis (scripts/study1r_results_1rc.py: `records`, `sel`,
`mean_ci`, built on the frozen sting.study1r_measures.episode_measures); statistics are the frozen primitives
(sting.stage2_analysis: percentile bootstrap 10,000 resamples within arm, seed 20261025; two-sided permutation p, 10,000
permutations; Holm; Wilson).

Outputs (each labeled with its status):
- primary, Cell A (mini-low): Offer-floor minus Silent-floor; "words effect present" only if the CI excludes zero;
- primary, Cell B (if run): Offer-floor minus Silent-floor (words) and Silent-floor minus Silent (price), Holm within
  Cell B; present only if the CI excludes zero and the Holm p is below 0.05;
- secondary: propensity per arm (Wilson); Cell B Silent baseline; stability of Cell A Silent-floor against Study 1R-C
  mini-low Silent-floor (cross-run, non-concurrent, bootstrap CI only); descriptive per arm.

Usage: python scripts/study1r_results_1rd.py OUT_DIR --campaign-yaml Y --logs L[,L...] --expect-excluded IDS
           --rc-yaml Y --rc-logs L[,L...] --rc-expect-excluded IDS [--md PATH]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import numpy as np
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.stage2_analysis import bootstrap_diff, holm, permutation_p, wilson  # noqa: E402
from sting.study1r_measures import PROPENSITY_THRESHOLDS  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
CELL_A = "mini-low"


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


RC = load("study1r_results_1rc.py", "rc_for_1rd")


def test(eps: list[dict], a: tuple, b: tuple) -> dict:
    ya = [e["change"] for e in RC.sel(eps, *a)]
    yb = [e["change"] for e in RC.sel(eps, *b)]
    if not ya or not yb:
        return {"skipped": "arm missing"}
    r = bootstrap_diff(ya, yb)
    r["p_permutation"] = permutation_p(ya, yb)
    return r


def analyse(eps: list[dict], cells: list[str]) -> dict:
    res: dict = {"label": "Study 1R-D (preregistered add-on, amendment AMENDMENT_1RD.md)"}
    a = test(eps, (CELL_A, "offer_floor", "1rd"), (CELL_A, "silent_floor", "1rd"))
    if "skipped" not in a:
        a["words_effect_present"] = bool(a["excludes_zero"])
    res["primary, Cell A (mini-low): Offer-floor minus Silent-floor (words effect)"] = a
    for cb in [c for c in cells if c != CELL_A]:
        fam = {"Offer-floor minus Silent-floor (words effect)": test(eps, (cb, "offer_floor", "1rd"), (cb, "silent_floor", "1rd")),
               "Silent-floor minus Silent (price effect)": test(eps, (cb, "silent_floor", "1rd"), (cb, "silent", "1rd"))}
        ran = {k: r["p_permutation"] for k, r in fam.items() if "p_permutation" in r}
        for k, p in holm(ran).items():
            fam[k]["p_holm"] = p
            fam[k]["effect_present"] = bool(fam[k]["excludes_zero"] and p < 0.05)
        res[f"primary, Cell B ({cb}; Holm family of two)"] = fam
    ya = [e["change"] for e in RC.sel(eps, CELL_A, "silent_floor", "1rd")]
    yb = [e["change"] for e in RC.sel(eps, CELL_A, "silent_floor", "1rc")]
    res["stability, descriptive, non-concurrent (Study 1R-D Cell A Silent-floor minus Study 1R-C mini-low Silent-floor)"] = \
        bootstrap_diff(ya, yb) if ya and yb else {"skipped": "arm missing"}
    prop, desc = {}, {}
    for c in cells:
        for arm in ("offer_floor", "silent_floor", "silent"):
            es = RC.sel(eps, c, arm, "1rd")
            if not es:
                continue
            prop[f"{c}/{arm}"] = {k: {"k": sum(bool(e[k]) for e in es), "n": len(es),
                                      "ci": list(wilson(sum(bool(e[k]) for e in es), len(es)))} for k in PROPENSITY_THRESHOLDS}
            sellers = [v for e in es for v in (e.get("probe") or {}).values()]
            yes = sum(v == "YES" for v in sellers)
            desc[f"{c}/{arm}"] = {
                "episodes": len(es), "change": RC.mean_ci([e["change"] for e in es]),
                "mean_post": float(np.mean([e["post"] for e in es])),
                "mean_x_minus_pre": float(np.mean([e["jump"] for e in es])),
                "sting_mean_ask_11_30": float(np.mean([e["sting_mean_ask_11_30"] for e in es])),
                "floor_binding_rounds": sum(e["floor_binding_rounds"] for e in es),
                "rounds_10_30": sum(e["rounds_10_30"] for e in es), "g2_passed": sum(bool(e["g2_passed"]) for e in es),
                "probe_q2": {"sellers": len(sellers), "yes": yes, "unparseable": sellers.count("unparseable"),
                             "rate": yes / len(sellers) if sellers else None,
                             "ci": list(wilson(yes, len(sellers))) if sellers else None}}
    res["secondary: propensity per arm"] = prop
    res["descriptive per arm (Cell B Silent = the Cell B Silent baseline)"] = desc
    return res


def f3(v) -> str:
    return f"{v:+.3f}"


def row(name: str, r: dict, extra: str = "") -> str:
    if "skipped" in r:
        return f"| {name} | skipped: {r['skipped']} | | | | | | |"
    holm_p = f"{r['p_holm']:.4f}" if "p_holm" in r else "n/a"
    present = r.get("words_effect_present", r.get("effect_present"))
    return (f"| {name} | {f3(r['estimate'])} | {f3(r['ci_low'])}, {f3(r['ci_high'])} | {r['p_permutation']:.4f} | {holm_p} "
            f"| {r['n_a']} vs {r['n_b']} | {r['excludes_zero']} | {present} |")


def report(res: dict, excluded: list, rc_excluded: list) -> str:
    L = ["# Study 1R-D results (words with pricing held fixed)", "",
         "Preregistered add-on (prereg_study1r/AMENDMENT_1RD.md; lock prereg_study1r/FROZEN_1RD.json). Facts only. "
         "Completed episodes through the completed-episodes wrapper's staging. Script: `scripts/study1r_results_1rd.py`.", "",
         f"Excluded Study 1R-D episodes (status not completed): {', '.join(e['replicate_id'] for e in excluded) or 'none'}. "
         f"Excluded Study 1R-C episodes (stability only): {', '.join(e['replicate_id'] for e in rc_excluded) or 'none'}.", "",
         "## Primary (change score; bootstrap 95% CI, 10,000 resamples, seed 20261025; two-sided permutation p)", "",
         "Rule (amendment section 6): Cell A, an effect is present only if the CI excludes zero; Cell B, only if the CI "
         "excludes zero and the Holm-adjusted p (within Cell B) is below 0.05.", "",
         "| Test | Estimate | 95% CI | Permutation p | Holm p | n | CI excludes zero | Effect present |",
         "|---|---|---|---|---|---|---|---|",
         row("Cell A (mini-low): Offer-floor minus Silent-floor", res["primary, Cell A (mini-low): Offer-floor minus Silent-floor (words effect)"])]
    for k, fam in res.items():
        if k.startswith("primary, Cell B"):
            for name, r in fam.items():
                L.append(row(f"{k.split('(')[1].split(';')[0]}: {name}", r))
    s = res["stability, descriptive, non-concurrent (Study 1R-D Cell A Silent-floor minus Study 1R-C mini-low Silent-floor)"]
    L += ["", "## Stability (descriptive, non-concurrent): Cell A Silent-floor minus Study 1R-C mini-low Silent-floor", "",
          "skipped" if "skipped" in s else f"{f3(s['estimate'])} (95% CI {f3(s['ci_low'])}, {f3(s['ci_high'])}), n {s['n_a']} vs {s['n_b']}.",
          "", "## Secondary: propensity per arm (Wilson 95% CI)", "",
          "| Arm | above $92.70 | above $91.80 | above $94.50 |", "|---|---|---|---|"]
    w = lambda d: f"{d['k']}/{d['n']} ({d['ci'][0]:.3f}, {d['ci'][1]:.3f})"  # noqa: E731
    for arm, p in res["secondary: propensity per arm"].items():
        L.append(f"| {arm} | {w(p['propensity_92.70'])} | {w(p['propensity_91.80'])} | {w(p['propensity_94.50'])} |")
    L += ["", "## Descriptive per arm (the Cell B Silent row is the Cell B Silent baseline)", "",
          "| Arm | Episodes | Mean change (95% CI) | Mean post | Mean X - pre | Seller C mean ask, rounds 11-30 | Floor binding | "
          "G2 passed | Probe Q2 YES (sellers; Wilson) |", "|---|---|---|---|---|---|---|---|---|"]
    for arm, d in res["descriptive per arm (Cell B Silent = the Cell B Silent baseline)"].items():
        ch, pq = d["change"], d["probe_q2"]
        probe = f"{pq['yes']}/{pq['sellers']} ({pq['ci'][0]:.3f}, {pq['ci'][1]:.3f})" if pq["sellers"] else "none"
        L.append(f"| {arm} | {d['episodes']} | {f3(ch['mean'])} ({f3(ch['ci'][0])}, {f3(ch['ci'][1])}) | ${d['mean_post']:.2f} | "
                 f"{d['mean_x_minus_pre']:.2f} | ${d['sting_mean_ask_11_30']:.2f} | {d['floor_binding_rounds']}/{d['rounds_10_30']} | "
                 f"{d['g2_passed']}/{d['episodes']} | {probe} |")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir", type=Path)
    for k in ("--campaign-yaml", "--rc-yaml"):
        ap.add_argument(k, type=Path, required=True)
    for k in ("--logs", "--expect-excluded", "--rc-logs", "--rc-expect-excluded"):
        ap.add_argument(k, required=True)
    ap.add_argument("--md", type=Path, default=None)
    a = ap.parse_args()
    wrap = load("study1r_results_completed.py", "wrap_1rd")
    ids = lambda s: {x for x in s.split(",") if x}  # noqa: E731
    cells = list(dict.fromkeys(x["cell"] for x in yaml.safe_load(a.campaign_yaml.read_text(encoding="utf-8"))["arms"]))
    with tempfile.TemporaryDirectory(prefix="s1rd_") as tmp:
        logs, excl = wrap.stage([Path(p) for p in a.logs.split(",") if p], Path(tmp) / "d")
        wrap.check(excl, ids(a.expect_excluded))
        rlogs, rexcl = wrap.stage([Path(p) for p in a.rc_logs.split(",") if p], Path(tmp) / "c")
        wrap.check(rexcl, ids(a.rc_expect_excluded))
        eps = RC.records(a.campaign_yaml, logs, "1rd") + RC.records(a.rc_yaml, rlogs, "1rc")
    res = analyse(eps, cells)
    res["excluded"], res["rc_excluded"] = excl, rexcl
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "results_1rd.json").write_text(json.dumps(res, indent=2, default=str), encoding="utf-8")
    md = report(res, excl, rexcl)
    (a.md or a.out_dir / "RESULTS_1RD.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
