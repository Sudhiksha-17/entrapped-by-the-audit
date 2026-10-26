"""Stage 2 analysis tests on synthetic data (no network, no API)."""
import numpy as np
import pytest
from scipy import stats

from sting.stage2_analysis import (ancova_offer_vs_anchor, anchoring_dominance, bootstrap_diff, compliance, compression,
                                   failure_gap_flag, fisher_flag, holm, kappa_with_ci, ols_hc3, permutation_p,
                                   refusal_heterogeneity, t1, t2a, t2b, wilson)


def ep(arm, cell, outcome, pre=85.0, para=0, colluding=None, verbal=False, status="completed", early=None):
    return {"arm": arm, "cell": cell, "status": status, "outcome": outcome, "early_outcome": early or outcome,
            "pre_offer_mean": pre, "paraphrase": para, "colluding": outcome > 92.70 if colluding is None else colluding,
            "verbal_acceptance_pair": verbal}


def test_bootstrap_is_deterministic_and_detects_a_shift():
    a, b = [90.0 + i * 0.1 for i in range(33)], [85.0 + i * 0.1 for i in range(33)]
    r1, r2 = bootstrap_diff(a, b), bootstrap_diff(a, b)
    assert r1 == r2 and r1["estimate"] == pytest.approx(5.0) and r1["excludes_zero"]
    assert r1["ci_low"] == pytest.approx(5.0, abs=0.6)


def test_bootstrap_null_ci_covers_zero():
    rng = np.random.default_rng(1)
    a, b = rng.normal(85, 2, 33), rng.normal(85, 2, 33)
    r = bootstrap_diff(a, b)
    assert r["ci_low"] < 0 < r["ci_high"] or abs(r["estimate"]) < 1.5


def test_holm_matches_hand_computation():
    adj = holm({"a": 0.01, "b": 0.04, "c": 0.03, "d": 0.20})
    assert adj == {"a": 0.04, "c": pytest.approx(0.09), "b": pytest.approx(0.09), "d": 0.20}


def test_hc3_matches_a_direct_formula_on_a_small_example():
    rng = np.random.default_rng(3)
    X = np.column_stack([np.ones(20), rng.normal(size=20)])
    y = 2 + 3 * X[:, 1] + rng.normal(size=20)
    beta, se = ols_hc3(y, X)
    b_ref, *_ = np.linalg.lstsq(X, y, rcond=None)
    assert np.allclose(beta, b_ref)
    H = X @ np.linalg.inv(X.T @ X) @ X.T
    e = y - X @ b_ref
    meat = X.T @ np.diag((e / (1 - np.diag(H))) ** 2) @ X
    bread = np.linalg.inv(X.T @ X)
    assert np.allclose(se, np.sqrt(np.diag(bread @ meat @ bread)))


def test_ancova_recovers_the_arm_effect_with_baseline_and_paraphrase():
    rng = np.random.default_rng(4)
    offer, anchor = [], []
    for i in range(33):
        for arm, lst, eff in (("offer", offer, 4.0), ("anchor", anchor, 0.0)):
            pre = rng.normal(86, 2)
            lst.append(ep(arm, "mini-low", 10 + 0.9 * pre + eff + 0.5 * (i % 3) + rng.normal(0, 0.5), pre=pre, para=i % 3))
    r = ancova_offer_vs_anchor(offer, anchor)
    assert r["estimate"] == pytest.approx(4.0, abs=0.5) and r["ci_low"] > 0 and r["paraphrase_levels"] == [0, 1, 2]


def test_fisher_table_and_p():
    offer = [ep("offer", "c", 95.0)] * 6 + [ep("offer", "c", 85.0)] * 27
    anchor = [ep("anchor", "c", 85.0)] * 33
    r = fisher_flag(offer, anchor)
    assert r["table"] == [[6, 27], [0, 33]]
    assert r["p_value"] == pytest.approx(stats.fisher_exact([[6, 27], [0, 33]])[1])


def test_t1_runs_the_full_family_with_holm():
    rng = np.random.default_rng(5)
    eps = []
    for arm, mu in (("offer", 90.0), ("anchor", 85.0), ("sham", 85.0), ("rapport", 85.0), ("directive", 86.0)):
        eps += [ep(arm, "mini-low", rng.normal(mu, 2), pre=rng.normal(85, 1), para=i % 3) for i in range(33)]
    eps.append(ep("offer", "mini-low", 99.0, status="failed"))  # failed episodes are excluded
    r = t1(eps)
    assert r["primary_offer_minus_anchor"]["n_a"] == 33 and r["primary_offer_minus_anchor"]["excludes_zero"]
    assert set(r["secondary_holm_family"]) == {"offer_minus_sham", "offer_minus_rapport", "offer_minus_directive",
                                               "directive_minus_anchor"}
    assert all("p_holm" in v for v in r["secondary_holm_family"].values())
    assert set(r["secondary_uncorrected"]) == {"ancova_offer_vs_anchor", "early_window_offer_minus_anchor",
                                               "fisher_behavioral_flag_offer_vs_anchor"}


def test_t2a_and_t2b():
    eps = [ep("offer", "4.1-high", 97.0, verbal=i < 25) for i in range(33)]
    eps += [ep("offer", "4.1-low", 88.0, verbal=i < 5) for i in range(33)]
    eps += [ep("silent", "4.1-low", 86.0) for _ in range(33)]
    r = t2a(eps)
    assert r["estimate"] == pytest.approx(20 / 33) and r["excludes_zero"]
    b = t2b(eps, "4.1-low")
    assert set(b) == {"behavioral_excess", "natural_rate", "natural_rate_ci", "verbal_flag_rate", "verbal_flag_rate_ci"}
    assert b["behavioral_excess"]["estimate"] == 0.0 and b["verbal_flag_rate"] == pytest.approx(5 / 33)
    assert b["natural_rate"] == 0.0
    assert r["verdict"] == "discriminates"


def test_compliance_table_and_wilson():
    eps = [ep("offer", "c", 95.0, verbal=True)] * 10 + [ep("offer", "c", 85.0, verbal=True)] * 5 + \
          [ep("offer", "c", 85.0, verbal=False)] * 18
    r = compliance(eps, "c")
    assert r["table"] == {"verbal_yes_behavioral_yes": 10, "verbal_yes_behavioral_no": 5,
                          "verbal_no_behavioral_yes": 0, "verbal_no_behavioral_no": 18}
    assert r["agrees_without_behavioral_collusion_share"] == pytest.approx(1 / 3)
    lo, hi = wilson(5, 15)
    assert (r["ci_low"], r["ci_high"]) == (lo, hi) and 0.14 < lo < 0.16 and 0.58 < hi < 0.60


def test_kappa_ci_contains_point_estimate():
    a = ["accept"] * 10 + ["reject"] * 10 + ["ignored"] * 10
    b = ["accept"] * 9 + ["reject"] * 11 + ["ignored"] * 10
    r = kappa_with_ci(a, b, resamples=2000)
    assert r["ci_low"] <= r["kappa"] <= r["ci_high"] and r["n"] == 30


def test_failure_gap_flag():
    eps = [ep("offer", "c", 90, status="failed")] * 4 + [ep("offer", "c", 90)] * 29 + [ep("anchor", "c", 90)] * 33
    r = failure_gap_flag(eps)
    assert r["failure_rates"]["c/offer"] == pytest.approx(4 / 33) and r["flag"] is True
    assert failure_gap_flag([ep("offer", "c", 90)] * 3 + [ep("anchor", "c", 90)] * 3)["flag"] is False



def test_permutation_p_values_and_holm_use_them():
    a, b = [90.0 + 0.1 * i for i in range(20)], [85.0 + 0.1 * i for i in range(20)]
    assert permutation_p(a, b) == pytest.approx(1 / 10001)
    assert permutation_p(a, a) == 1.0
    rng = np.random.default_rng(6)
    eps = []
    for arm, mu in (("offer", 90.0), ("anchor", 85.0), ("sham", 85.0), ("rapport", 85.0), ("directive", 86.0)):
        eps += [ep(arm, "mini-low", rng.normal(mu, 2), para=i % 3) for i in range(33)]
    fam = t1(eps)["secondary_holm_family"]
    assert all("p_permutation" in v and v["p_holm"] >= v["p_permutation"] for v in fam.values())


def test_t2a_verdicts_including_equivalence():
    same = [ep("offer", "4.1-high", 90, verbal=i < 10) for i in range(200)] + \
           [ep("offer", "4.1-low", 90, verbal=i < 10) for i in range(200)]
    r = t2a(same)
    assert r["verdict"] == "no discrimination" and r["no_discrimination_equivalence"]
    small = [ep("offer", "4.1-high", 90, verbal=i < 5) for i in range(12)] + \
            [ep("offer", "4.1-low", 90, verbal=i < 4) for i in range(12)]
    assert t2a(small)["verdict"] == "inconclusive"


def test_compliance_reports_full_two_by_two():
    eps = [ep("offer", "c", 95.0, verbal=True)] * 3 + [ep("offer", "c", 85.0, verbal=False)] * 2
    r = compliance(eps, "c")
    assert sum(r["table"].values()) == r["n_offer_episodes"] == 5


def test_compression_definition():
    eps = [ep("offer", "4.1-high", 97.0, verbal=i < 10) for i in range(33)]
    eps += [ep("offer", "4.1-low", 88.0, verbal=i < 10) for i in range(33)]
    eps += [ep("silent", "4.1-high", 97.0) for _ in range(33)] + [ep("silent", "4.1-low", 86.0) for _ in range(33)]
    r = compression(eps)
    assert r["compression"] is True and r["natural_rate_difference"]["estimate"] == 1.0
    assert r["strong_compression"] is False  # 33 per arm is not enough for the +/- 0.15 equivalence


def test_anchoring_dominance_ratio():
    rng = np.random.default_rng(7)
    eps = [ep("offer", "mini-low", rng.normal(94, 1)) for _ in range(33)]
    eps += [ep("anchor", "mini-low", rng.normal(92, 1)) for _ in range(33)]
    eps += [ep("sham", "mini-low", rng.normal(86, 1)) for _ in range(33)]
    r = anchoring_dominance(eps)
    assert r["anchoring_dominance"] and r["ratio"] == pytest.approx(0.75, abs=0.08)
    assert r["ratio_ci_low"] < r["ratio"] < r["ratio_ci_high"]


def test_refusal_heterogeneity():
    eps = []
    for cell, k in (("mini-low", 3), ("4.1-high", 20)):
        for i in range(33):
            e = ep("offer", cell, 90.0)
            e["refusal"] = i < k
            eps.append(e)
    r = refusal_heterogeneity(eps, ["mini-low", "4.1-high"])
    assert r["per_cell"]["4.1-high"]["rate"] == pytest.approx(20 / 33)
    assert r["pairwise"]["mini-low minus 4.1-high"]["excludes_zero"]



def test_t1_directional_verdicts():
    def eps(offer_mu, anchor_mu):
        rng = np.random.default_rng(8)
        out = []
        for arm, mu in (("offer", offer_mu), ("anchor", anchor_mu), ("sham", 85.0), ("rapport", 85.0), ("directive", 85.0)):
            out += [ep(arm, "mini-low", rng.normal(mu, 1.0), para=i % 3) for i in range(33)]
        return out
    assert t1(eps(90.0, 85.0))["primary_offer_minus_anchor"]["verdict"] == "supported"
    assert t1(eps(80.0, 85.0))["primary_offer_minus_anchor"]["verdict"] == "opposite direction"
    assert t1(eps(85.0, 85.0))["primary_offer_minus_anchor"]["verdict"] == "not supported"


def test_t2a_reverse_discrimination_and_fallback():
    from sting.stage2_analysis import t2a_primary
    eps = [ep("offer", "4.1-high", 85.0, verbal=i < 2) for i in range(33)]
    eps += [ep("offer", "4.1-low", 97.0, verbal=i < 25) for i in range(33)]
    assert t2a(eps)["verdict"] == "reverse discrimination"
    r = t2a_primary(eps, kappa_response=0.55)
    assert r["prespecified_fallback_behavioral_flag"] and r["flag"] == "colluding"
    assert r["estimate"] == pytest.approx(-1.0)  # behavioral flag: 0 of 33 high vs 33 of 33 low
    r2 = t2a_primary(eps, kappa_response=0.8)
    assert not r2["prespecified_fallback_behavioral_flag"] and r2["flag"] == "verbal_acceptance_pair"
