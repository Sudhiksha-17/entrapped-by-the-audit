"""Exploratory plan C (notes/EXPLORATORY_PLAN_B_C.md section C): accepter choice, window measures, raised split.
Synthetic data only; no model calls."""
import importlib.util

from sting.paths import REPO_ROOT

spec = importlib.util.spec_from_file_location("pcs", REPO_ROOT / "scripts" / "study1r_plan_c.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)


def _round(n, a, b, trades=()):
    return {"round_number": n, "seller_asks": {"Seller A": a, "Seller B": b, "Seller C": 99.0},
            "trades": [{"seller_id": s, "price": p} for s, p in trades]}


def test_accepter_tie_goes_to_seller_a_and_earlier_round_wins():
    assert P.pick_accepter({"Seller B": 20, "Seller A": 20}) == ("Seller A", True)
    assert P.pick_accepter({"Seller A": 25, "Seller B": 20}) == ("Seller B", True)
    assert P.pick_accepter({"Seller B": 28}) == ("Seller B", False)


def test_window_measures_and_raised_split():
    rounds = [_round(25, 96.0, 97.0), _round(26, 96.0, None), _round(27, 96.0, 96.0),
              _round(28, 98.0, 97.0, [("Seller A", 98.0), ("Seller B", 97.0), ("Seller B", 97.5)]),
              _round(29, 99.0, 99.0), _round(30, None, 95.0, [("Seller B", 95.0)])]
    m = P.episode_measures(rounds, ["Seller A", "Seller B"], "Seller A", 28)
    assert (m["accepter_id"], m["partner_id"], m["window"]) == ("Seller A", "Seller B", [28, 30])
    assert m["accepter"] == {"mean_ask": 98.5, "trades": 1, "profit": 18.0}
    assert m["partner"]["trades"] == 3 and abs(m["partner"]["profit"] - 49.5) < 1e-9
    assert m["rounds_both_posted"] == 2 and m["share_partner_below"] == 0.5     # round 30: accepter did not post
    assert m["accepter_ask_before"] == 96.0 and m["raised_toward_x"] is True
