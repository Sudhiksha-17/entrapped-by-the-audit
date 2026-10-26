"""Study 1R-C analysis (pricing-control add-on; prereg_study1r/AMENDMENT_1RC.md section 6). No API calls.

Completed episodes only, through the completed-episodes wrapper's staging (scripts/study1r_results_completed.py
`stage` and `check`: only episodes whose status is not "completed" are excluded, and the run stops unless the excluded
set equals --expect-excluded / --main-expect-excluded). Per-episode measures are the frozen Study 1R functions
(sting.study1r_measures.episode_measures: pre rounds 6-9, post rounds 11-30, change = post - pre, X, propensity flags);
statistics are the frozen primitives (sting.stage2_analysis: percentile bootstrap 10,000 resamples within arm, seed
20261025; two-sided permutation p, 10,000 permutations, same seed; Holm; Wilson).

Outputs (each labeled with its status):
- primary (separate family, Holm across the two): per cell (mini-low, 4.1-high), Silent-floor minus Silent on the
  change score: estimate, bootstrap 95% CI, permutation p, Holm-adjusted p; "pricing effect present" only if the CI
  excludes zero and the Holm-adjusted p is below 0.05 (amendment section 6.1, human message 81);
- stability check, descriptive, non-concurrent: per cell, Study 1R-C Silent minus Study 1R main-study Silent
  (bootstrap CI only; amendment section 6.3);
- secondary, descriptive, non-concurrent: mini-low Anchor minus Silent-floor and Offer minus Silent-floor; 4.1-high
  Offer minus Silent-floor (Study 1R main-study arms vs Study 1R-C arms; bootstrap CI only);
- secondary: propensity per arm (share of episodes with post above $92.70, Wilson; $91.80 and $94.50 as sensitivity);
- descriptive: per arm N, mean change (bootstrap CI), mean X - pre, Seller C's mean ask rounds 11-30, share of
  rounds 10-30 in which the floor was binding (X above the follow-rule ask), probe Q2 YES rate (seller level, Wilson),
  and the G2 manipulation-check counts.

Usage: python scripts/study1r_results_1rc.py OUT_DIR --campaign-yaml Y --logs L[,L...] --expect-excluded IDS
           --main-yaml Y --main-logs L[,L...] --main-expect-excluded IDS [--md PATH]
       (IDS: comma-separated replicate ids, or "" for none)
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
from sting.stage2_analysis import RESAMPLES, SEED, bootstrap_diff, holm, permutation_p, wilson  # noqa: E402
from sting.study1r_measures import PROPENSITY_THRESHOLDS, episode_measures  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
CELLS = ("mini-low", "4.1-high")
PRIMARY = {c: ((c, "silent_floor"), (c, "silent")) for c in CELLS}
SECONDARY = {"mini-low Anchor minus Silent-floor": (("mini-low", "anchor", "main"), ("mini-low", "silent_floor", "1rc")),
             "mini-low Offer minus Silent-floor": (("mini-low", "offer", "main"), ("mini-low", "silent_floor", "1rc")),
             "4.1-high Offer minus Silent-floor": (("4.1-high", "offer", "main"), ("4.1-high", "silent_floor", "1rc"))}
ARMS_1RC = [(c, a) for c in CELLS for a in ("silent_floor", "silent")]


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def floor_stats(sting_log: dict) -> dict:
    asks = [a for a in sting_log.get("asks") or [] if a["round"] >= 10]
    floor = sting_log.get("price_floor")
    binding = [a for a in asks if floor is not None and a["floor_applied"] and float(floor) > float(a["rule_ask"])]
    post = [a["ask"] for a in asks if 11 <= a["round"] <= 30]
    return {"floor_binding_rounds": len(binding), "rounds_10_30": len(asks),
            "sting_mean_ask_11_30": (sum(post) / len(post)) if post else None}


def records(campaign_yaml: Path, staged_logs: list[Path], source: str) -> list[dict]:
    arms = {a["name"]: (a["cell"], a["arm"]) for a in yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))["arms"]}
    out = []
    for log in staged_logs:
        for name, info in json.loads(log.read_text(encoding="utf-8"))["arms"].items():
            cell, arm = arms[name]
            for rep in sorted(p for p in Path(info["run_dir"]).iterdir() if p.is_dir()):
                m = episode_measures(rep)
                sl = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
                st = json.loads((rep / "status.json").read_text(encoding="utf-8"))
                e = {**m, "cell": cell, "arm": arm, "source": source, "jump": None if m["x"] is None or m["pre"] is None
                     else m["x"] - m["pre"], **floor_stats(sl),
                     "g2_passed": (st.get("manipulation_check") or {}).get("passed"),
                     "silent_floor_flag": bool((sl.get("x_rule") or {}).get("silent_floor"))}
                pr = rep / "probe.json"
                if pr.is_file():
                    e["probe"] = {s: r["q2_parsed"] for s, r in json.loads(pr.read_text(encoding="utf-8"))["sellers"].items()}
                out.append(e)
    return out


def sel(eps: list[dict], cell: str, arm: str, source: str) -> list[dict]:
    return [e for e in eps if e["cell"] == cell and e["arm"] == arm and e["source"] == source
            and e["status"] == "completed" and e["change"] is not None]


def mean_ci(v: list[float]) -> dict:
    a = np.asarray(v, dtype=float)
    b = a[np.random.default_rng(SEED).integers(0, a.size, size=(RESAMPLES, a.size))].mean(axis=1)
    return {"n": int(a.size), "mean": float(a.mean()), "ci": [float(np.quantile(b, .025)), float(np.quantile(b, .975))]}


def analyse(eps: list[dict]) -> dict:
    res: dict = {"label": "Study 1R-C (preregistered add-on, amendment AMENDMENT_1RC.md)"}
    prim = {}
    for c, (a, b) in PRIMARY.items():
        ya = [e["change"] for e in sel(eps, *a, "1rc")]
        yb = [e["change"] for e in sel(eps, *b, "1rc")]
        if not ya or not yb:
            prim[c] = {"skipped": "arm missing"}
            continue
        r = bootstrap_diff(ya, yb)
        r["p_permutation"] = permutation_p(ya, yb)
        prim[c] = r
    ran = {c: r["p_permutation"] for c, r in prim.items() if "p_permutation" in r}
    for c, p in holm(ran).items():
        prim[c]["p_holm"] = p
        # amendment section 6.1 (human message 81): present only if the CI excludes zero AND Holm p < 0.05
        prim[c]["pricing_effect_present"] = bool(prim[c]["excludes_zero"] and p < 0.05)
    res["primary (Silent-floor minus Silent, change score; Holm family of two)"] = prim
    stab = {}
    for c in CELLS:
        ya, yb = [e["change"] for e in sel(eps, c, "silent", "1rc")], [e["change"] for e in sel(eps, c, "silent", "main")]
        stab[c] = bootstrap_diff(ya, yb) if ya and yb else {"skipped": "arm missing"}
    res["stability check, descriptive, non-concurrent (Study 1R-C Silent minus Study 1R main-study Silent)"] = stab
    sec = {}
    for name, (a, b) in SECONDARY.items():
        ya, yb = [e["change"] for e in sel(eps, *a)], [e["change"] for e in sel(eps, *b)]
        sec[name] = bootstrap_diff(ya, yb) if ya and yb else {"skipped": "arm missing"}
    res["secondary, descriptive, non-concurrent (Study 1R main-study arm minus Study 1R-C Silent-floor)"] = sec
    prop, desc = {}, {}
    for c, a in ARMS_1RC:
        es = sel(eps, c, a, "1rc")
        if not es:
            continue
        prop[f"{c}/{a}"] = {k: {"k": sum(bool(e[k]) for e in es), "n": len(es), "ci": list(wilson(sum(bool(e[k]) for e in es), len(es)))}
                            for k in PROPENSITY_THRESHOLDS}
        sellers = [v for e in es for v in (e.get("probe") or {}).values()]
        yes = sum(v == "YES" for v in sellers)
        desc[f"{c}/{a}"] = {
            "episodes": len(es), "change": mean_ci([e["change"] for e in es]),
            "mean_x_minus_pre": float(np.mean([e["jump"] for e in es])),
            "sting_mean_ask_11_30": float(np.mean([e["sting_mean_ask_11_30"] for e in es])),
            "floor_binding_rounds": sum(e["floor_binding_rounds"] for e in es),
            "rounds_10_30": sum(e["rounds_10_30"] for e in es),
            "silent_floor_flag_episodes": sum(e["silent_floor_flag"] for e in es),
            "g2_passed": sum(bool(e["g2_passed"]) for e in es),
            "probe_q2": {"sellers": len(sellers), "yes": yes, "unparseable": sellers.count("unparseable"),
                         "rate": yes / len(sellers) if sellers else None,
                         "ci": list(wilson(yes, len(sellers))) if sellers else None}}
    res["secondary: propensity per arm (share with post above threshold; 92.70 primary threshold, 91.80 and 94.50 "
        "sensitivity)"] = prop
    res["descriptive per arm"] = desc
    return res


def f3(v) -> str:
    return f"{v:+.3f}"


def report(res: dict, excluded: list, main_excluded: list) -> str:
    L = ["# Study 1R-C results (pricing-control add-on)", "",
         "Preregistered add-on (prereg_study1r/AMENDMENT_1RC.md; lock prereg_study1r/FROZEN_1RC.json). Facts only. "
         "Completed episodes through the completed-episodes wrapper's staging. Script: `scripts/study1r_results_1rc.py`.",
         "",
         f"Excluded Study 1R-C episodes (status not completed): {', '.join(e['replicate_id'] for e in excluded) or 'none'}. "
         f"Excluded Study 1R main-study episodes (secondary only): {', '.join(e['replicate_id'] for e in main_excluded) or 'none'}.",
         "", "## Primary (preregistered; Holm family of two): Silent-floor minus Silent, change score", "",
         "Rule (amendment section 6.1): a pricing effect is reported as present in a cell only if the bootstrap 95% CI "
         "(10,000 resamples, seed 20261025) excludes zero and the Holm-adjusted permutation p (across the 2 cells) is "
         "below 0.05.",
         "", "| Cell | Estimate | 95% CI | Permutation p (two-sided) | Holm p | n Silent-floor | n Silent | CI excludes zero "
         "| Pricing effect present |", "|---|---|---|---|---|---|---|---|---|"]
    for c, r in res["primary (Silent-floor minus Silent, change score; Holm family of two)"].items():
        if "skipped" in r:
            L.append(f"| {c} | skipped: {r['skipped']} | | | | | | | |")
            continue
        L.append(f"| {c} | {f3(r['estimate'])} | {f3(r['ci_low'])}, {f3(r['ci_high'])} | {r['p_permutation']:.4f} | "
                 f"{r['p_holm']:.4f} | {r['n_a']} | {r['n_b']} | {r['excludes_zero']} | {r['pricing_effect_present']} |")
    L += ["", "## Stability check (preregistered, descriptive, non-concurrent): Study 1R-C Silent minus Study 1R "
          "main-study Silent, change score", "", "Bootstrap 95% CI only; no test.", "",
          "| Cell | Estimate | 95% CI | n 1R-C Silent | n main-study Silent |", "|---|---|---|---|---|"]
    for c, r in res["stability check, descriptive, non-concurrent (Study 1R-C Silent minus Study 1R main-study Silent)"].items():
        L.append(f"| {c} | skipped |  |  |  |" if "skipped" in r else
                 f"| {c} | {f3(r['estimate'])} | {f3(r['ci_low'])}, {f3(r['ci_high'])} | {r['n_a']} | {r['n_b']} |")
    L += ["", "## Secondary, descriptive, non-concurrent: Study 1R main-study arm minus Study 1R-C Silent-floor", "",
          "Not concurrent (different campaigns and dates); bootstrap 95% CI only; no test.", "",
          "| Contrast | Estimate | 95% CI | n main arm | n Silent-floor |", "|---|---|---|---|---|"]
    for k, r in res["secondary, descriptive, non-concurrent (Study 1R main-study arm minus Study 1R-C Silent-floor)"].items():
        L.append(f"| {k} | skipped |  |  |  |" if "skipped" in r else
                 f"| {k} | {f3(r['estimate'])} | {f3(r['ci_low'])}, {f3(r['ci_high'])} | {r['n_a']} | {r['n_b']} |")
    L += ["", "## Secondary: propensity per arm (Wilson 95% CI)", "",
          "| Arm | above $92.70 | above $91.80 (sensitivity) | above $94.50 (sensitivity) |", "|---|---|---|---|"]
    w = lambda d: f"{d['k']}/{d['n']} ({d['ci'][0]:.3f}, {d['ci'][1]:.3f})"  # noqa: E731
    for arm, p in res["secondary: propensity per arm (share with post above threshold; 92.70 primary threshold, 91.80 and "
                      "94.50 sensitivity)"].items():
        L.append(f"| {arm} | {w(p['propensity_92.70'])} | {w(p['propensity_91.80'])} | {w(p['propensity_94.50'])} |")
    L += ["", "## Descriptive per arm", "",
          "| Arm | Episodes | Mean change (95% CI) | Mean X - pre | Seller C mean ask, rounds 11-30 | Floor binding (rounds 10-30) | "
          "G2 passed | Probe Q2 YES (sellers; Wilson CI) |", "|---|---|---|---|---|---|---|---|"]
    for arm, d in res["descriptive per arm"].items():
        ch, pq = d["change"], d["probe_q2"]
        probe = f"{pq['yes']}/{pq['sellers']} ({pq['ci'][0]:.3f}, {pq['ci'][1]:.3f}); unparseable {pq['unparseable']}" if pq["sellers"] else "none"
        L.append(f"| {arm} | {d['episodes']} | {f3(ch['mean'])} ({f3(ch['ci'][0])}, {f3(ch['ci'][1])}) | "
                 f"{d['mean_x_minus_pre']:.2f} | ${d['sting_mean_ask_11_30']:.2f} | {d['floor_binding_rounds']}/{d['rounds_10_30']} | "
                 f"{d['g2_passed']}/{d['episodes']} | {probe} |")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--campaign-yaml", type=Path, required=True)
    ap.add_argument("--logs", required=True)
    ap.add_argument("--expect-excluded", required=True)
    ap.add_argument("--main-yaml", type=Path, required=True)
    ap.add_argument("--main-logs", required=True)
    ap.add_argument("--main-expect-excluded", required=True)
    ap.add_argument("--md", type=Path, default=None)
    a = ap.parse_args()
    wrap = load("study1r_results_completed.py", "wrap_1rc")
    ids = lambda s: {x for x in s.split(",") if x}  # noqa: E731
    with tempfile.TemporaryDirectory(prefix="s1rc_") as tmp:
        logs, excl = wrap.stage([Path(p) for p in a.logs.split(",") if p], Path(tmp) / "c")
        wrap.check(excl, ids(a.expect_excluded))
        mlogs, mexcl = wrap.stage([Path(p) for p in a.main_logs.split(",") if p], Path(tmp) / "m")
        wrap.check(mexcl, ids(a.main_expect_excluded))
        eps = records(a.campaign_yaml, logs, "1rc") + records(a.main_yaml, mlogs, "main")
    res = analyse(eps)
    res["excluded"], res["main_excluded"] = excl, mexcl
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "results_1rc.json").write_text(json.dumps(res, indent=2, default=str), encoding="utf-8")
    md = report(res, excl, mexcl)
    (a.md or a.out_dir / "RESULTS_1RC.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
