"""Study 1R analysis (prereg_study1r/STUDY1R_SPEC.md version 2 with the revisions of human messages 40-52). Pure
functions over per-episode records; no API calls. Statistical primitives come from sting.stage2_analysis (percentile
bootstrap 10,000 resamples within arm, seed 20261025; permutation p-values; Holm; OLS with HC3; Fisher; Wilson).

Episode record keys (built by scripts/study1r_results.py): arm, cell, status, pre, post, change, x, jump (= x - pre),
paraphrase, behavioral_acceptance, propensity_91.80/92.70/94.50, acc_inclusive, acc_strict, acc_inclusive_11_12,
accept_by_seller {seller: bool}, test_suspicion_share, ack_rate, probe {seller: YES|NO|unparseable}, acc_v1, acc_v2
(optional), accept_by_round {round: bool} (optional); option A (human message 64; 4.1-low and 4.1-high Offer):
verification_messages, verification_uncoded, audit {stratum: [bool accepted]}, audit_accept, uncoded_negative
{stratum: int}; engagement: engaged_any_detector, first_engagement_round_detector, engaged_any_screener,
first_engagement_round_screener.
Every function tolerates missing arms and returns {"skipped": reason} instead of raising.
"""
from __future__ import annotations

from typing import Any, Optional

import numpy as np
from scipy import stats

from sting.stage2_analysis import RESAMPLES, SEED, bootstrap_diff, fisher_flag, holm, ols_hc3, permutation_p, wilson

CELLS = ("mini-low", "4.1-low", "4.1-high")


def eps(episodes: list[dict], arm: str, cell: str) -> list[dict]:
    return [e for e in episodes if e["arm"] == arm and e["cell"] == cell and e["status"] == "completed"]


def vals(es: list[dict], key: str) -> list[float]:
    return [float(e[key]) for e in es if e.get(key) is not None]


def flags(es: list[dict], key: str) -> list[float]:
    return [1.0 if e[key] else 0.0 for e in es if e.get(key) is not None]


def directional(r: dict, below: bool = False) -> dict:
    """Supported only if the 95% CI lies entirely above zero (entirely below with below=True); the other side is the
    opposite direction."""
    lo, hi = r["ci_low"], r["ci_high"]
    if below:
        r["verdict"] = "supported" if hi < 0 else "opposite direction" if lo > 0 else "not supported"
    else:
        r["verdict"] = "supported" if lo > 0 else "opposite direction" if hi < 0 else "not supported"
    return r


def contrast(episodes: list[dict], a: tuple[str, str], b: tuple[str, str], key: str = "change") -> dict:
    ya, yb = vals(eps(episodes, a[1], a[0]), key), vals(eps(episodes, b[1], b[0]), key)
    if not ya or not yb:
        return {"skipped": f"no data for {a if not ya else b}"}
    return bootstrap_diff(ya, yb)


# --- T1 ------------------------------------------------------------------------------------------------------------

def t1(episodes: list[dict]) -> dict:
    r = contrast(episodes, ("mini-low", "offer"), ("mini-low", "anchor"))
    return r if "skipped" in r else directional(r)


HOLM_FAMILY = {
    "mini-low Offer minus Sham": (("mini-low", "offer"), ("mini-low", "sham"), None),
    "mini-low Anchor minus Sham": (("mini-low", "anchor"), ("mini-low", "sham"), None),
    "mini-low Sham minus Silent": (("mini-low", "sham"), ("mini-low", "silent"), None),
    "4.1-low Offer minus Anchor (secondary T1)": (("4.1-low", "offer"), ("4.1-low", "anchor"), "above"),
    "4.1-high Offer minus Silent (disruption)": (("4.1-high", "offer"), ("4.1-high", "silent"), "below"),
}
# Human message 64: the Holm family is these 5 contrasts; disruption in mini-low and 4.1-low is descriptive
# (bootstrap CI, no verdict, no p-value).
DISRUPTION_DESCRIPTIVE = {
    "mini-low Offer minus Silent (disruption, descriptive)": (("mini-low", "offer"), ("mini-low", "silent")),
    "4.1-low Offer minus Silent (disruption, descriptive)": (("4.1-low", "offer"), ("4.1-low", "silent")),
}


def disruption_descriptive(episodes: list[dict]) -> dict:
    return {name: contrast(episodes, a, b) for name, (a, b) in DISRUPTION_DESCRIPTIVE.items()}


def holm_family(episodes: list[dict]) -> dict:
    out = {}
    for name, (a, b, rule) in HOLM_FAMILY.items():
        r = contrast(episodes, a, b)
        if "skipped" not in r:
            r["p_permutation"] = permutation_p(vals(eps(episodes, a[1], a[0]), "change"),
                                               vals(eps(episodes, b[1], b[0]), "change"))
            if rule:
                directional(r, below=(rule == "below"))
        out[name] = r
    ran = {k: v["p_permutation"] for k, v in out.items() if "p_permutation" in v}
    for k, p in holm(ran).items():
        out[k]["p_holm"] = p
    return out


def ancova(episodes: list[dict]) -> dict:
    rows = [(1.0, e) for e in eps(episodes, "offer", "mini-low")] + [(0.0, e) for e in eps(episodes, "anchor", "mini-low")]
    rows = [(t, e) for t, e in rows if e.get("post") is not None and e.get("pre") is not None]
    if len({t for t, _ in rows}) < 2:
        return {"skipped": "needs mini-low Offer and Anchor"}
    y = np.array([e["post"] for _, e in rows])
    levels = sorted({e["paraphrase"] for _, e in rows})
    X = np.column_stack([np.ones(len(rows)), [t for t, _ in rows], [e["pre"] for _, e in rows]]
                        + [[1.0 if e["paraphrase"] == p else 0.0 for _, e in rows] for p in levels[1:]])
    beta, se = ols_hc3(y, X)
    z = stats.norm.ppf(0.975)
    return {"offer_coef": float(beta[1]), "se_hc3": float(se[1]), "ci_low": float(beta[1] - z * se[1]),
            "ci_high": float(beta[1] + z * se[1]), "pre_coef": float(beta[2]), "n": len(rows)}


def fisher_offer_anchor(episodes: list[dict]) -> dict:
    o, a = eps(episodes, "offer", "mini-low"), eps(episodes, "anchor", "mini-low")
    if not o or not a:
        return {"skipped": "needs mini-low Offer and Anchor"}
    return fisher_flag(o, a, key="behavioral_acceptance")


# --- T2a, T2b, compliance, calibration ------------------------------------------------------------------------------

def t2a(episodes: list[dict], key: str = "acc_inclusive", high: str = "4.1-high", low: str = "4.1-low") -> dict:
    h, l = flags(eps(episodes, "offer", high), key), flags(eps(episodes, "offer", low), key)
    if not h or not l:
        return {"skipped": f"needs Offer arms in {high} and {low} with {key}"}
    return directional({**bootstrap_diff(h, l), "measure": key})


AUDIT_STRATA = ("audit_flagged", "audit_unflagged")


def _audit(episodes: list[dict]) -> dict[str, np.ndarray]:
    o = [e for c in ("4.1-low", "4.1-high") for e in eps(episodes, "offer", c) if "audit" in e]
    return {g: np.array([float(x) for e in o for x in e["audit"][g]]) for g in AUDIT_STRATA}


def miss_rates(episodes: list[dict]) -> dict:
    """Option A miss audit: per stratum of screener negatives (pooled over the 4.1-low and 4.1-high Offer arms), the
    share of audited messages the human coded accept or conditional_accept (Wilson 95% CI); the population-weighted
    miss rate over all screener negatives (bootstrap 95% CI over audited messages within stratum); the expected number
    of missed acceptance messages among the uncoded; and the screener's verification precision (share of the
    verification set human-confirmed)."""
    o = [e for c in ("4.1-low", "4.1-high") for e in eps(episodes, "offer", c) if "audit" in e]
    if not o:
        return {"skipped": "needs option A coding in the 4.1 Offer arms"}
    au = _audit(episodes)
    pop = {g: sum(e["uncoded_negative"][g] + len(e["audit"][g]) for e in o) for g in AUDIT_STRATA}
    out: dict[str, Any] = {"strata": {}}
    for g in AUDIT_STRATA:
        k, n = int(au[g].sum()), int(au[g].size)
        out["strata"][g] = {"audited": n, "accepted": k, "rate": (k / n) if n else None,
                            "ci": wilson(k, n) if n else None, "screener_negatives": pop[g],
                            "uncoded": pop[g] - n}
    tot = sum(pop.values())
    rate = lambda r: sum(r[g] * pop[g] for g in AUDIT_STRATA) / tot if tot else None  # noqa: E731
    point = {g: (au[g].mean() if au[g].size else 0.0) for g in AUDIT_STRATA}
    rng = np.random.default_rng(SEED)
    boot = {g: (au[g][rng.integers(0, au[g].size, size=(RESAMPLES, au[g].size))].mean(axis=1) if au[g].size
                else np.zeros(RESAMPLES)) for g in AUDIT_STRATA}
    w = rate(boot)
    out["weighted_miss_rate"] = {"rate": rate(point), "ci": None if w is None else [float(np.quantile(w, 0.025)),
                                                                                   float(np.quantile(w, 0.975))]}
    out["expected_missed_acceptance_messages"] = sum(point[g] * out["strata"][g]["uncoded"] for g in AUDIT_STRATA)
    vn = sum(e["verification_messages"] - e["verification_uncoded"] for e in o)
    vk = sum(1 for e in o if e.get("acc_inclusive"))
    out["verification"] = {"messages": sum(e["verification_messages"] for e in o),
                           "uncoded": sum(e["verification_uncoded"] for e in o), "coded": vn,
                           "accepting_episodes": vk}
    out["audit_accepting_episodes_not_in_primary"] = sum(1 for e in o if e.get("audit_accept") and not e.get("acc_inclusive"))
    return out


def t2a_miss_corrected(episodes: list[dict], high: str = "4.1-high", low: str = "4.1-low") -> dict:
    """T2a sensitivity corrected for the estimated miss rate (option A). Per episode: 1 if a human-confirmed acceptance
    exists (verification set or audit), else the probability that at least one uncoded screener-negative message is an
    acceptance, 1 - prod over strata (1 - p_stratum)^(uncoded messages in that stratum), with p from the audit
    (messages assumed independent). Cell rate = mean over episodes; CI = percentile bootstrap resampling episodes
    within arm and audited messages within stratum jointly (10,000 resamples, seed 20261025)."""
    eh = [e for e in eps(episodes, "offer", high) if "audit" in e]
    el = [e for e in eps(episodes, "offer", low) if "audit" in e]
    if not eh or not el:
        return {"skipped": f"needs option A coding in the Offer arms of {high} and {low}"}
    au = _audit(episodes)

    def arrays(es):
        base = np.array([bool(e.get("acc_inclusive") or e.get("audit_accept")) for e in es])
        nf = np.array([e["uncoded_negative"]["audit_flagged"] for e in es], dtype=float)
        nu = np.array([e["uncoded_negative"]["audit_unflagged"] for e in es], dtype=float)
        return base, nf, nu

    def value(arr, pf, pu, idx=None):
        base, nf, nu = arr if idx is None else (arr[0][idx], arr[1][idx], arr[2][idx])
        pf, pu = np.asarray(pf)[..., None] if idx is not None else pf, np.asarray(pu)[..., None] if idx is not None else pu
        return np.where(base, 1.0, 1.0 - (1.0 - pf) ** nf * (1.0 - pu) ** nu).mean(axis=-1)

    H, L = arrays(eh), arrays(el)
    pf0 = au["audit_flagged"].mean() if au["audit_flagged"].size else 0.0
    pu0 = au["audit_unflagged"].mean() if au["audit_unflagged"].size else 0.0
    est = float(value(H, pf0, pu0) - value(L, pf0, pu0))
    rng = np.random.default_rng(SEED)
    bs = {g: (au[g][rng.integers(0, au[g].size, size=(RESAMPLES, au[g].size))].mean(axis=1) if au[g].size
              else np.zeros(RESAMPLES)) for g in AUDIT_STRATA}
    ih = rng.integers(0, len(eh), size=(RESAMPLES, len(eh)))
    il = rng.integers(0, len(el), size=(RESAMPLES, len(el)))
    d = value(H, bs["audit_flagged"], bs["audit_unflagged"], ih) - value(L, bs["audit_flagged"], bs["audit_unflagged"], il)
    lo, hi = float(np.quantile(d, 0.025)), float(np.quantile(d, 0.975))
    r = {"estimate": est, "ci_low": lo, "ci_high": hi, "excludes_zero": bool(lo > 0 or hi < 0),
         "rate_high": float(value(H, pf0, pu0)), "rate_low": float(value(L, pf0, pu0)), "n_high": len(eh),
         "n_low": len(el), "p_audit_flagged": float(pf0), "p_audit_unflagged": float(pu0),
         "measure": "inclusive acceptance corrected for the estimated miss rate"}
    return directional(r)


def logit_irls(X: np.ndarray, y: np.ndarray, max_iter: int = 100, tol: float = 1e-10) -> dict:
    beta = np.zeros(X.shape[1])
    converged = False
    for _ in range(max_iter):
        p = 1 / (1 + np.exp(-np.clip(X @ beta, -35, 35)))
        w = np.clip(p * (1 - p), 1e-12, None)
        z = X @ beta + (y - p) / w
        new = np.linalg.pinv(X.T @ (X * w[:, None])) @ (X.T @ (w * z))
        if np.max(np.abs(new - beta)) < tol:
            beta, converged = new, True
            break
        beta = new
    p = 1 / (1 + np.exp(-np.clip(X @ beta, -35, 35)))
    cov = np.linalg.pinv(X.T @ (X * np.clip(p * (1 - p), 1e-12, None)[:, None]))
    se = np.sqrt(np.diag(cov))
    separation = (not converged) or bool(np.max(np.abs(beta)) > 15)
    return {"beta": beta.tolist(), "se": se.tolist(), "converged": converged, "separation_suspected": separation}


def t2a_jump_logit(episodes: list[dict], key: str = "acc_inclusive") -> dict:
    """Secondary (human message 51, 3a): logistic regression of inclusive acceptance on cell (4.1-high = 1) and jump
    (X - pre), Offer arms of 4.1-low and 4.1-high; Wald 95% CIs."""
    rows = [(1.0 if c == "4.1-high" else 0.0, e) for c in ("4.1-low", "4.1-high") for e in eps(episodes, "offer", c)
            if e.get(key) is not None and e.get("jump") is not None]
    if len({c for c, _ in rows}) < 2:
        return {"skipped": "needs Offer arms in 4.1-low and 4.1-high"}
    X = np.column_stack([np.ones(len(rows)), [c for c, _ in rows], [e["jump"] for _, e in rows]])
    y = np.array([1.0 if e[key] else 0.0 for _, e in rows])
    fit = logit_irls(X, y)
    z = stats.norm.ppf(0.975)
    names = ["intercept", "cell_4.1-high", "jump"]
    return {"n": len(rows), "converged": fit["converged"], "separation_suspected": fit["separation_suspected"],
            "coefficients": {n: {"estimate": b, "se": s, "ci_low": b - z * s, "ci_high": b + z * s}
                             for n, b, s in zip(names, fit["beta"], fit["se"])}}


def t2b(episodes: list[dict], cell: str) -> dict:
    o, s = flags(eps(episodes, "offer", cell), "behavioral_acceptance"), flags(eps(episodes, "silent", cell), "behavioral_acceptance")
    if not o or not s:
        return {"skipped": f"needs Offer and Silent in {cell}"}
    k = int(sum(s))
    return {"excess": bootstrap_diff(o, s), "natural_rate": k / len(s), "natural_rate_ci": wilson(k, len(s))}


def compliance(episodes: list[dict], cell: str, key: str = "acc_inclusive") -> dict:
    o = [e for e in eps(episodes, "offer", cell) if e.get(key) is not None and e.get("behavioral_acceptance") is not None]
    if not o:
        return {"skipped": f"no Offer episodes with verbal labels in {cell}"}
    v, b = [bool(e[key]) for e in o], [bool(e["behavioral_acceptance"]) for e in o]
    t = {"V+B+": sum(x and y for x, y in zip(v, b)), "V+B-": sum(x and not y for x, y in zip(v, b)),
         "V-B+": sum(not x and y for x, y in zip(v, b)), "V-B-": sum(not x and not y for x, y in zip(v, b))}
    nv = t["V+B+"] + t["V+B-"]
    lo, hi = wilson(t["V+B-"], nv)
    return {"table": t, "n": len(o), "accepts_without_behavioral_movement": (t["V+B-"] / nv) if nv else None,
            "ci_low": lo, "ci_high": hi}


def calibration(episodes: list[dict]) -> dict:
    out = {}
    for c in CELLS:
        s, o = eps(episodes, "silent", c), eps(episodes, "offer", c)
        row: dict[str, Any] = {"silent_n": len(s), "offer_n": len(o)}
        for t in ("propensity_91.80", "propensity_92.70", "propensity_94.50"):
            f = flags(s, t)
            row[t] = (sum(f) / len(f)) if f else None
        p = vals(s, "post")
        row["silent_mean_post"] = (sum(p) / len(p)) if p else None
        for k in ("acc_inclusive", "behavioral_acceptance"):
            f = flags(o, k)
            row[f"offer_{k}"] = (sum(f) / len(f)) if f else None
        out[c] = row
    return out


# --- probe ------------------------------------------------------------------------------------------------------------

def seller_rows(es: list[dict]) -> list[tuple[dict, str, str]]:
    return [(e, s, a) for e in es for s, a in (e.get("probe") or {}).items()]


def probe_measures(episodes: list[dict], arms: list[tuple[str, str]]) -> dict:
    """Awareness rate = share of sellers answering YES (seller-level; unparseable answers count in the denominator and
    are reported), Wilson CI; Offer minus Silent per cell (bootstrap over sellers within arm); aware acceptance."""
    per_arm = {}
    for cell, arm in arms:
        rows = seller_rows(eps(episodes, arm, cell))
        if not rows:
            continue
        k = sum(a == "YES" for _, _, a in rows)
        per_arm[f"{cell}/{arm}"] = {"sellers": len(rows), "yes": k, "unparseable": sum(a == "unparseable" for _, _, a in rows),
                                    "rate": k / len(rows), "ci": wilson(k, len(rows))}
    diffs, aware = {}, {}
    for c in CELLS:
        o, s = seller_rows(eps(episodes, "offer", c)), seller_rows(eps(episodes, "silent", c))
        if o and s:
            diffs[c] = bootstrap_diff([1.0 if a == "YES" else 0.0 for _, _, a in o], [1.0 if a == "YES" else 0.0 for _, _, a in s])
        if o:
            both = sum(1 for e, sid, a in o if a == "YES" and (e.get("accept_by_seller") or {}).get(sid))
            oe = eps(episodes, "offer", c)
            ep = sum(1 for e in oe if any(e.get("probe", {}).get(sid) == "YES" and (e.get("accept_by_seller") or {}).get(sid)
                                          for sid in (e.get("accept_by_seller") or {})))
            aware[c] = {"sellers": len(o), "aware_acceptance": both, "share": both / len(o),
                        "episodes": len(oe), "aware_accepting_episodes": ep}
    return {"per_arm": per_arm, "offer_minus_silent": diffs, "aware_acceptance": aware}


# --- exploratory and pre-enumerated ----------------------------------------------------------------------------------

def exploratory(episodes: list[dict], arms: list[tuple[str, str]]) -> dict:
    out: dict[str, Any] = {"public_private_gap": {}, "test_suspicion": {}, "ack_rate": {}, "acceptance_by_round": {}}
    for c in CELLS:
        o = [e for e in eps(episodes, "offer", c) if e.get("acc_inclusive") is not None and e.get("acc_private_inclusive") is not None]
        if o:
            out["public_private_gap"][c] = {
                "n": len(o), "public_not_private": sum(e["acc_inclusive"] and not e["acc_private_inclusive"] for e in o),
                "private_not_public": sum(e["acc_private_inclusive"] and not e["acc_inclusive"] for e in o)}
        rounds: dict[int, list[bool]] = {}
        for e in eps(episodes, "offer", c):
            for r, v in (e.get("accept_by_round") or {}).items():
                rounds.setdefault(int(r), []).append(bool(v))
        if rounds:
            out["acceptance_by_round"][c] = {r: sum(v) / len(v) for r, v in sorted(rounds.items())}
    for cell, arm in arms:
        es = eps(episodes, arm, cell)
        ts = vals(es, "test_suspicion_share")
        if ts:
            out["test_suspicion"][f"{cell}/{arm}"] = sum(ts) / len(ts)
        ack = vals(es, "ack_rate")
        if ack:
            out["ack_rate"][f"{cell}/{arm}"] = sum(ack) / len(ack)
    return out


def anchoring_dominance(episodes: list[dict]) -> dict:
    y = {a: np.array(vals(eps(episodes, a, "mini-low"), "change")) for a in ("offer", "anchor", "sham")}
    if any(v.size == 0 for v in y.values()):
        return {"skipped": "needs mini-low Offer, Anchor and Sham"}
    os_ = bootstrap_diff(y["offer"], y["sham"])
    denom = y["offer"].mean() - y["sham"].mean()
    ratio = (y["anchor"].mean() - y["sham"].mean()) / denom if denom != 0 else None
    rng = np.random.default_rng(SEED)
    m = {a: v[rng.integers(0, v.size, size=(RESAMPLES, v.size))].mean(axis=1) for a, v in y.items()}
    d = m["offer"] - m["sham"]
    keep = d != 0
    r = (m["anchor"][keep] - m["sham"][keep]) / d[keep]
    lo, hi = (np.quantile(r, [0.025, 0.975]) if r.size else (None, None))
    return {"offer_minus_sham": os_, "ratio": ratio, "ratio_ci": [None if lo is None else float(lo),
                                                                  None if hi is None else float(hi)],
            "anchoring_dominance": bool(os_["excludes_zero"] and ratio is not None and ratio >= 0.5)}


def pre_enumerated(episodes: list[dict]) -> dict:
    t = t2a(episodes)
    s_hi, s_lo = flags(eps(episodes, "silent", "4.1-high"), "propensity_92.70"), flags(eps(episodes, "silent", "4.1-low"), "propensity_92.70")
    prop = bootstrap_diff(s_hi, s_lo) if s_hi and s_lo else {"skipped": "needs Silent in 4.1-high and 4.1-low"}
    comp = None
    if "skipped" not in t and "skipped" not in prop:
        comp = bool(t["ci_low"] <= 0 <= t["ci_high"] and prop["excludes_zero"])
    ignoring = {}
    for c in CELLS:
        for key, basis in (("engaged_any_screener", "judge v2 screener"), ("engaged_any_detector", "detector")):
            o = [e for e in eps(episodes, "offer", c) if e.get(key) is not None]
            if o:
                k = sum(not e[key] for e in o)
                ignoring[f"{c} ({basis})"] = {"n": len(o), "never_engaged": k, "share": k / len(o), "ci": wilson(k, len(o))}
    return {"compression": {"t2a": t, "propensity_difference_silent": prop, "compression": comp},
            "anchoring_dominance": anchoring_dominance(episodes),
            "says_yes_does_not_act": {c: compliance(episodes, c) for c in CELLS},
            "ignoring": ignoring}


def first_engagement(episodes: list[dict]) -> dict:
    """Kaplan-Meier style first-engagement curve per cell, Offer arms: detector-based in every cell, and judge v2
    screener-based where screener labels exist (each labeled; under option A engagement is not human-coded)."""
    from sting.study1r_measures import engagement_curve
    out = {}
    for c in CELLS:
        o = eps(episodes, "offer", c)
        for key, basis in (("first_engagement_round_detector", "detector"), ("first_engagement_round_screener", "judge v2 screener")):
            if o and all(key in e for e in o):
                out[f"{c} ({basis})"] = {"basis": basis, "curve": engagement_curve([e[key] for e in o])}
    return out


def v1_comparison(episodes: list[dict]) -> dict:
    """Headline figure per cell (Offer arms; human message 63): v1-read acceptance (frozen Study 1 judge, "accept" in
    rounds 11-30), v2-read inclusive acceptance (judge v2 r1, gpt-4.1, exploratory), human-coded inclusive acceptance
    (backup cells only; the T2a measure), and the behavioral flag rate."""
    out = {}
    for c in CELLS:
        o = eps(episodes, "offer", c)
        if not o:
            continue
        row = {}
        for k, name in (("acc_v1", "v1_read"), ("acc_v2", "v2_read"), ("acc_inclusive", "human_coded"),
                        ("behavioral_acceptance", "behavioral_flag")):
            f = flags(o, k)
            row[name] = {"k": int(sum(f)), "n": len(f), "rate": (sum(f) / len(f)) if f else None,
                         "ci": wilson(int(sum(f)), len(f)) if f else None}
        out[c] = row
    return out


def addon_a(episodes: list[dict]) -> dict:
    """Study 1R-A: Competitive minus Silent on the change score in 4.1-high (supported only if the CI lies entirely
    below zero); propensity (share above $92.70) per arm with Wilson CIs."""
    r = contrast(episodes, ("4.1-high", "competitive"), ("4.1-high", "silent"))
    out = {"disruption": r if "skipped" in r else directional(r, below=True), "propensity": {}}
    for arm in ("competitive", "silent"):
        f = flags(eps(episodes, arm, "4.1-high"), "propensity_92.70")
        if f:
            k = int(sum(f))
            out["propensity"][arm] = {"k": k, "n": len(f), "rate": k / len(f), "ci": wilson(k, len(f))}
    return out


def alt_coding_summary(episodes: list[dict]) -> dict:
    """Alternative coding (human message 62): per cell, human-coded Offer messages coded ignored that address Seller C
    and urge a price change (counter under the alternative coding). Acceptance (inclusive or strict), and so T2a,
    cannot change under this coding; under option A engagement is not human-coded, so the count is the whole effect."""
    out = {}
    for c in CELLS:
        o = [e for e in eps(episodes, "offer", c) if "reclassified_alt" in e]
        if o:
            out[c] = {"episodes": len(o), "reclassified_messages": sum(e["reclassified_alt"] for e in o)}
    return out
