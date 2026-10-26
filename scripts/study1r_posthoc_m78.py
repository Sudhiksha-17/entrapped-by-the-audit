"""Study 1R exploratory, post hoc, descriptive (human message 78; not preregistered; no frozen file changed). No API calls.

Episode records come from the frozen `build` of scripts/study1r_results.py on completed episodes (the D-116 wrapper's
staging), with the judge v2 screener labels, so pre, post, change, X, jump (X - pre), acceptance, audit strata and
engagement are the analysis' own values. Bootstraps: 10,000 resamples, seed 20261025, percentile 95% CIs.

1. X - pre per Offer arm; pre and headroom (100 - pre) per cell (all main-study arms of the cell).
2. Propensity: share of Silent episodes with post above $92.70, per cell (Wilson 95% CI).
3. 4.1-high Offer: inclusive acceptance vs X - pre: point-biserial correlation (bootstrap CI over episodes) and
   logistic slope (IRLS, Wald CI; the analysis' `logit_irls`).
4. T2a logistic regression scale and the correlation of cell (4.1-high = 1) with X - pre in its sample.
5. Reference for the before/after comparison of accepting episodes (scripts/study1r_price_by_acceptance.py): in
   4.1-high Offer episodes without confirmed acceptance and in 4.1-high Silent, a pseudo-acceptance round is drawn per
   episode (uniform over rounds 17-29: the accepters' first confirmed rounds with an after window lie in 17-29), and
   after minus before is computed exactly as for the accepters (3 rounds before, 3 after, round excluded, clipped at
   30); episodes and rounds resampled jointly 10,000 times. A second version draws the round from the accepters' own
   first confirmed rounds with an after window.
6. Labeler A vs Labeler B on the 40 validation items before adjudication (pass 1 vs pass 2 label files, as in
   results/study1r/labeling/validation/agreement.json), recoded to inclusive acceptance yes/no.
7. Miss audit: screener negatives per stratum and cell; the sampling rule (scripts/study1r_label_sets.py
   `verify_sets`); rule-of-three upper bounds.
8. Paired sensitivity for T1 and the Holm contrasts: change(a) - change(b) paired by replicate index (indices present
   in both arms), bootstrap CI over pairs. Same replicate index = same opening-book draw and paraphrase (PREREG
   sections 3-4).
9. Engagement in 4.1-high Offer: screener (judge v2 r1 gpt-4.1 label in ENGAGED_RESPONSES) and detector (codebook
   rules 1, 2 and 4) on public messages, rounds 11-30; episode and message counts.

Usage: python scripts/study1r_posthoc_m78.py <out_dir> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
       <judge_v2_dir>[,...] <val_labels_A> <val_key_A> <val_labels_B> <val_key_B>
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting import study1r_analysis as A  # noqa: E402
from sting.judge import seller_responses  # noqa: E402
from sting.judge_v2 import ENGAGED_RESPONSES  # noqa: E402
from sting.stage2_analysis import kappa_with_ci, wilson  # noqa: E402
from sting.stage2_measures import rounds_of, window_mean  # noqa: E402
from sting.study1r_gates import detector  # noqa: E402
from sting.study1r_measures import ACCEPT_INCLUSIVE  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
SEED, R = 20261025, 10_000
CELLS = ("mini-low", "4.1-low", "4.1-high")
ROUNDS = range(11, 31)
PAIRED = {"T1 primary: mini-low Offer minus Anchor": (("mini-low", "offer"), ("mini-low", "anchor")),
          **{k: (a, b) for k, (a, b, _) in A.HOLM_FAMILY.items()}}


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def boot_mean(v, rng) -> dict:
    v = np.asarray(v, dtype=float)
    b = v[rng.integers(0, v.size, size=(R, v.size))].mean(axis=1)
    return {"n": int(v.size), "mean": float(v.mean()), "ci": [float(np.quantile(b, .025)), float(np.quantile(b, .975))]}


def wil(k: int, n: int) -> dict:
    lo, hi = wilson(k, n)
    return {"k": k, "n": n, "rate": k / n, "ci": [float(lo), float(hi)]}


def collect(cy, logs, sheet, key, judge_dirs):
    wrap = load("study1r_results_completed.py", "wrap_m78")
    res = load("study1r_results.py", "res_m78")
    human, strata, protected = res.verify_labels(sheet, key)
    screener = res.load_labels(judge_dirs)
    with tempfile.TemporaryDirectory(prefix="s1r_m78_") as tmp:
        staged, excluded = wrap.stage(logs, Path(tmp))
        episodes = res.build([cy], staged, human, strata, screener, {}, False, protected)
        dirs = {p.name: p for log in staged for info in json.loads(log.read_text(encoding="utf-8"))["arms"].values()
                for p in Path(info["run_dir"]).iterdir() if p.is_dir()}
        extra = {}
        for e in episodes:
            if e["cell"] != "4.1-high" or e["arm"] not in ("offer", "silent"):
                continue
            rep = dirs[e["replicate_id"]]
            llm = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))["llm_seller_ids"]
            rounds = rounds_of(rep)
            x = {"asks": {r: window_mean(rounds, llm, range(r, r + 1)) for r in range(1, 31)}}
            if e["arm"] == "offer":
                resp = {s: seller_responses(rep / "upstream_logs" / f"{s}.md") for s in llm}
                text = {(s, r): str((resp[s].get(r) or {}).get("message_to_sellers") or "") for s in llm for r in ROUNDS}
                x["messages"] = {sr: {"nonempty": bool(t.strip()), "detector": detector(t, e["x"])["engaged"],
                                      "screener": (screener.get((e["replicate_id"], *sr)) or {}).get("response")}
                                 for sr, t in text.items()}
            extra[e["replicate_id"]] = x
    return episodes, extra, human, strata, [x["replicate_id"] for x in excluded]


def window(asks: dict, rr) -> float | None:
    v = [asks[r] for r in rr if asks.get(r) is not None]
    return sum(v) / len(v) if v else None


def before_after(asks: dict, r: int) -> float | None:
    after = range(r + 1, min(30, r + 3) + 1)
    if not len(after):
        return None
    b, a = window(asks, range(max(1, r - 3), r)), window(asks, after)
    return None if a is None or b is None else a - b


def analyse(episodes, extra, human, strata, val):
    rng = np.random.default_rng(SEED)
    E = lambda arm, cell: A.eps(episodes, arm, cell)  # noqa: E731
    out = {"label": "exploratory, post hoc, descriptive (not preregistered)"}
    # 1
    out["1_jump_per_offer_arm"] = {c: boot_mean([e["jump"] for e in E("offer", c)], rng) for c in CELLS}
    out["1_pre_and_headroom_per_cell"] = {}
    for c in CELLS:
        es = [e for e in episodes if e["cell"] == c and e["status"] == "completed" and e["pre"] is not None]
        out["1_pre_and_headroom_per_cell"][c] = {"arms": sorted({e["arm"] for e in es}),
                                                 "pre": boot_mean([e["pre"] for e in es], rng),
                                                 "headroom": boot_mean([100 - e["pre"] for e in es], rng)}
    # 2
    out["2_propensity_silent_92.70"] = {c: wil(sum(bool(e["propensity_92.70"]) for e in E("silent", c)),
                                               len(E("silent", c))) for c in CELLS}
    # 3
    o = E("offer", "4.1-high")
    y = np.array([1.0 if e["acc_inclusive"] else 0.0 for e in o])
    j = np.array([e["jump"] for e in o])
    idx = rng.integers(0, len(o), size=(R, len(o)))
    rs = [np.corrcoef(y[i], j[i])[0, 1] for i in idx if y[i].std() > 0 and j[i].std() > 0]
    fit = A.logit_irls(np.column_stack([np.ones(len(o)), j]), y)
    out["3_acceptance_vs_jump_4.1-high_offer"] = {
        "n": len(o), "accepting": int(y.sum()),
        "mean_jump_accepting": float(j[y == 1].mean()), "mean_jump_not": float(j[y == 0].mean()),
        "point_biserial_r": float(np.corrcoef(y, j)[0, 1]),
        "r_ci": [float(np.quantile(rs, .025)), float(np.quantile(rs, .975))], "r_valid_resamples": len(rs),
        "logit_slope": fit["beta"][1], "logit_slope_se": fit["se"][1],
        "logit_slope_ci": [fit["beta"][1] - 1.959964 * fit["se"][1], fit["beta"][1] + 1.959964 * fit["se"][1]],
        "converged": fit["converged"], "separation_suspected": fit["separation_suspected"]}
    # 4
    rows = [(1.0 if c == "4.1-high" else 0.0, e["jump"]) for c in ("4.1-low", "4.1-high") for e in E("offer", c)
            if e.get("acc_inclusive") is not None and e.get("jump") is not None]
    cell, jump = np.array([r[0] for r in rows]), np.array([r[1] for r in rows])
    out["4_t2a_logit"] = {"n": len(rows), "scale": "log-odds (logit link; IRLS maximum likelihood; Wald 95% CIs)",
                          "coding": "outcome inclusive acceptance (1/0); cell = 1 for 4.1-high, 0 for 4.1-low; "
                                    "jump = X - pre in dollars (slope = change in log-odds per $1)",
                          "corr_cell_jump": float(np.corrcoef(cell, jump)[0, 1]),
                          "mean_jump_4.1-low": float(jump[cell == 0].mean()),
                          "mean_jump_4.1-high": float(jump[cell == 1].mean())}
    # 5
    pba = load("study1r_price_by_acceptance.py", "pba_m78")
    acc_rounds = []
    acc_vals = []
    for e in o:
        if e["acc_inclusive"]:
            r0 = pba.first_acceptance(e["replicate_id"], human, strata)["first_confirmed_round"]
            v = before_after(extra[e["replicate_id"]]["asks"], r0)
            if v is not None:
                acc_rounds.append(r0)
                acc_vals.append(v)
    ref = {"accepters": {"n": len(acc_vals), "mean_after_minus_before": float(np.mean(acc_vals)),
                         "rounds": sorted(acc_rounds)}}
    groups = {"offer_not_accepting": [e for e in o if not e["acc_inclusive"]], "silent": E("silent", "4.1-high")}
    for g, es in groups.items():
        table = np.array([[before_after(extra[e["replicate_id"]]["asks"], r) for r in range(17, 30)] for e in es],
                         dtype=float)
        for name, pool in (("uniform_17_29", np.arange(17, 30)), ("accepters_rounds", np.array(acc_rounds))):
            ei = rng.integers(0, len(es), size=(R, len(es)))
            ri = pool[rng.integers(0, pool.size, size=(R, len(es)))] - 17
            m = np.nanmean(table[ei, ri], axis=1)
            ref[f"{g}__{name}"] = {"episodes": len(es), "mean": float(m.mean()),
                                   "interval_95": [float(np.quantile(m, .025)), float(np.quantile(m, .975))],
                                   "share_at_or_above_accepters": float((m >= ref["accepters"]["mean_after_minus_before"]).mean()),
                                   "missing_cells": int(np.isnan(table).sum())}
    out["5_before_after_reference"] = ref
    # 6
    la, ka, lb, kb = val
    ident = lambda k: (k["replicate_id"], k["seller"], k["round"])  # noqa: E731
    to_b = {ident(v): i for i, v in kb.items()}
    ids = sorted(ka)
    xa = [la[i]["response"] for i in ids]
    xb = [lb[to_b[ident(ka[i])]]["response"] for i in ids]
    ia = ["yes" if v in ACCEPT_INCLUSIVE else "no" for v in xa]
    ib = ["yes" if v in ACCEPT_INCLUSIVE else "no" for v in xb]
    out["6_validation_inclusive_agreement"] = {
        "n": len(ids), "check_response_kappa": kappa_with_ci(xa, xb)["kappa"],
        "table": {"A yes / B yes": sum(a == b == "yes" for a, b in zip(ia, ib)),
                  "A yes / B no": sum(a == "yes" and b == "no" for a, b in zip(ia, ib)),
                  "A no / B yes": sum(a == "no" and b == "yes" for a, b in zip(ia, ib)),
                  "A no / B no": sum(a == b == "no" for a, b in zip(ia, ib))},
        "base_rate_A": ia.count("yes") / len(ia), "base_rate_B": ib.count("yes") / len(ib),
        "raw_agreement": sum(a == b for a, b in zip(ia, ib)) / len(ia), "kappa": kappa_with_ci(ia, ib)}
    # 7
    miss = {}
    for c in ("4.1-low", "4.1-high"):
        es = [e for e in E("offer", c) if "audit" in e]
        miss[c] = {g: {"screener_negatives": sum(e["uncoded_negative"][g] + len(e["audit"][g]) for e in es),
                       "audited": sum(len(e["audit"][g]) for e in es),
                       "audited_accept": sum(sum(e["audit"][g]) for e in es)} for g in A.AUDIT_STRATA}
        miss[c]["verification"] = sum(e["verification_messages"] for e in es)
    tot = {g: {k: sum(miss[c][g][k] for c in miss) for k in ("screener_negatives", "audited", "audited_accept")}
           for g in A.AUDIT_STRATA}
    out["7_miss_audit"] = {"per_cell": miss, "pooled": tot,
                           "rule_of_three_upper": {g: 3 / tot[g]["audited"] for g in A.AUDIT_STRATA},
                           "rule_of_three_pooled_73": 3 / sum(tot[g]["audited"] for g in A.AUDIT_STRATA)}
    # 8
    paired = {}
    for name, (a, b) in PAIRED.items():
        da = {e["replicate_index"]: e["change"] for e in E(a[1], a[0]) if e["change"] is not None}
        db = {e["replicate_index"]: e["change"] for e in E(b[1], b[0]) if e["change"] is not None}
        common = sorted(set(da) & set(db))
        d = np.array([da[i] - db[i] for i in common])
        bm = d[np.random.default_rng(SEED).integers(0, d.size, size=(R, d.size))].mean(axis=1)
        lo, hi = float(np.quantile(bm, .025)), float(np.quantile(bm, .975))
        un = A.bootstrap_diff([da[i] for i in common], [db[i] for i in common])
        paired[name] = {"pairs": len(common), "indices": [min(common), max(common)], "paired_mean": float(d.mean()),
                        "paired_ci": [lo, hi], "excludes_zero": bool(lo > 0 or hi < 0),
                        "unpaired_same_episodes": {"estimate": un["estimate"], "ci": [un["ci_low"], un["ci_high"]]},
                        "corr_within_pair": float(np.corrcoef([da[i] for i in common], [db[i] for i in common])[0, 1])}
    out["8_paired_sensitivity"] = paired
    # 9
    msgs = [(e, sr, m) for e in o for sr, m in extra[e["replicate_id"]]["messages"].items()]
    scr = lambda m: m["screener"] in ENGAGED_RESPONSES  # noqa: E731
    ep = {e["replicate_id"]: {"screener": any(scr(m) for (e2, _, m) in msgs if e2 is e),
                              "detector": any(m["detector"] for (e2, _, m) in msgs if e2 is e)} for e in o}
    out["9_engagement_4.1-high_offer"] = {
        "episodes": len(o),
        "episodes_screener": sum(v["screener"] for v in ep.values()),
        "episodes_detector": sum(v["detector"] for v in ep.values()),
        "episodes_both": sum(v["screener"] and v["detector"] for v in ep.values()),
        "episodes_either": sum(v["screener"] or v["detector"] for v in ep.values()),
        "check_engaged_any_screener": sum(bool(e.get("engaged_any_screener")) for e in o),
        "check_engaged_any_detector": sum(bool(e.get("engaged_any_detector")) for e in o),
        "seller_rounds": len(msgs), "nonempty_messages": sum(m["nonempty"] for _, _, m in msgs),
        "screener_labelled": sum(m["screener"] is not None for _, _, m in msgs),
        "messages_screener_engaged": sum(scr(m) for _, _, m in msgs),
        "messages_detector_engaged": sum(m["detector"] for _, _, m in msgs),
        "messages_both": sum(scr(m) and m["detector"] for _, _, m in msgs),
        "screener_label_counts": {k: sum(m["screener"] == k for _, _, m in msgs)
                                  for k in sorted({m["screener"] for _, _, m in msgs if m["screener"]})}}
    return out


def main() -> None:
    a = sys.argv[1:]
    out_dir, cy = Path(a[0]), Path(a[1])
    logs = [Path(p) for p in a[2].split(",") if p]
    val_files = []
    for lab, key in ((a[6], a[7]), (a[8], a[9])):
        import csv
        with open(lab, newline="", encoding="utf-8") as f:
            val_files.append({r["item_id"]: r for r in csv.DictReader(f)})
        val_files.append(json.loads((Path(key) / "labeling_key.json").read_text(encoding="utf-8")))
    episodes, extra, human, strata, excluded = collect(cy, logs, Path(a[3]), Path(a[4]), [p for p in a[5].split(",") if p])
    res = analyse(episodes, extra, human, strata, val_files)
    res["excluded_episodes"] = excluded
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "posthoc_m78.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
