"""Exploratory price levels by confirmed acceptance (human message 76): first confirmed acceptance with dropped
verification messages, and the bootstrap summary. Synthetic data only; no model calls."""
import importlib.util

import pytest

from sting.paths import REPO_ROOT

spec = importlib.util.spec_from_file_location("pba", REPO_ROOT / "scripts" / "study1r_price_by_acceptance.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)


def test_first_acceptance_reports_dropped_earlier_verification():
    strata = {("e", "A", 12): "verification", ("e", "B", 14): "verification", ("e", "A", 20): "verification",
              ("e", "B", 22): "verification", ("e", "A", 15): "audit_unflagged", ("f", "A", 11): "verification"}
    human = {("e", "A", 12): {"response": "ignored"}, ("e", "A", 20): {"response": "conditional_accept"},
             ("e", "A", 15): {"response": "accept"}, ("f", "A", 11): {"response": "accept"}}
    fa = P.first_acceptance("e", human, strata)
    # the audit acceptance in round 15 is not a confirmed acceptance; round 14 was dropped uncoded, round 22 is later
    assert fa == {"first_confirmed_round": 20, "earliest_verification_round": 12,
                  "dropped_verification_rounds_before_first": [14]}
    assert P.first_acceptance("g", human, strata)["first_confirmed_round"] is None


def test_summary_mean_and_ci():
    import numpy as np
    s = P.summary([1.0, 2.0, 3.0], np.random.default_rng(0))
    assert s["n"] == 3 and s["mean"] == pytest.approx(2.0) and 1.0 <= s["ci"][0] <= 2.0 <= s["ci"][1] <= 3.0


M = importlib.util.module_from_spec(importlib.util.spec_from_file_location("m78", REPO_ROOT / "scripts" / "study1r_posthoc_m78.py"))
M.__spec__.loader.exec_module(M)


def test_before_after_matches_accepter_rule():
    asks = {r: float(r) for r in range(1, 31)}
    asks[25] = None                                   # rounds without an LLM ask are dropped from the window
    assert M.before_after(asks, 20) == pytest.approx(22.0 - 18.0)   # rounds 21-23 vs 17-19
    assert M.before_after(asks, 29) == pytest.approx(30.0 - 27.0)   # after window clipped to round 30
    assert M.before_after(asks, 30) is None                         # no after window
    assert M.before_after(asks, 24) == pytest.approx((26 + 27) / 2 - 22.0)


N9 = importlib.util.module_from_spec(importlib.util.spec_from_file_location("n9", REPO_ROOT / "scripts" / "study1r_reference_n9.py"))
N9.__spec__.loader.exec_module(N9)


def test_reference_n9_draws_nine_episodes_per_resample():
    import numpy as np
    table = np.zeros((21, 13))
    table[0, :] = 9.0                                    # one extreme episode
    out = N9.reference(table, np.random.default_rng(0), accepters=0.393)
    assert out["episodes_per_resample"] == 9 and out["resamples"] == 10_000 and out["episodes_in_group"] == 21
    # a resample mean reaches 1.0 (>= 0.393) exactly when the extreme episode is drawn at least once among 9
    assert out["share_at_or_above_accepters"] == pytest.approx(1 - (20 / 21) ** 9, abs=0.015)
