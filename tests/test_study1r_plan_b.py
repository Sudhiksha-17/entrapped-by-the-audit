"""Exploratory plan B selection (notes/EXPLORATORY_PLAN_B_C.md): accepting sellers, matched controls, fallback.
Synthetic data only; no model calls."""
import importlib.util

import pytest

from sting.paths import REPO_ROOT

spec = importlib.util.spec_from_file_location("pbs", REPO_ROOT / "scripts" / "study1r_plan_b_sheet.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)


def test_selection_matches_closest_mention_once_and_falls_back():
    eps = [{"replicate_id": "acc", "cell": "4.1-high", "acc_inclusive": True, "llm": ["A", "B"]},
           {"replicate_id": "n1", "cell": "4.1-high", "acc_inclusive": False, "llm": ["A", "B"]},
           {"replicate_id": "low", "cell": "4.1-low", "acc_inclusive": True, "llm": ["A", "B"]},
           {"replicate_id": "n2", "cell": "4.1-low", "acc_inclusive": False, "llm": ["A", "B"]}]
    strata = {("acc", "A", 20): "verification", ("acc", "A", 15): "verification", ("acc", "B", 29): "verification",
              ("low", "B", 30): "verification"}
    human = {("acc", "A", 20): {"response": "conditional_accept"}, ("acc", "A", 15): {"response": "ignored"},
             ("acc", "B", 29): {"response": "accept"}, ("low", "B", 30): {"response": "accept"}}
    mention = {("n1", "A"): [12], ("n1", "B"): [19, 28]}           # no mention in the 4.1-low pool -> fallback
    units, summary = P.select(eps, human, strata, mention)
    acc = [u for u in units if u["group"] == "accepting"]
    ctl = {u["matched_to"]: u for u in units if u["group"] == "control"}
    assert [(u["replicate_id"], u["seller"], u["rounds"]) for u in acc] == [
        ("acc", "A", [20, 21, 22]), ("acc", "B", [29, 30]), ("low", "B", [30])]
    assert (ctl["acc|A"]["replicate_id"], ctl["acc|A"]["seller"], ctl["acc|A"]["round_distance"]) == ("n1", "B", 1)
    assert (ctl["acc|B"]["seller"], ctl["acc|B"]["round_distance"], ctl["acc|B"]["rounds"]) == ("A", 17, [29, 30])
    assert ctl["low|B"]["fallback"] and ctl["low|B"]["replicate_id"] == "n2"
    assert summary["fallback_controls"] == 1 and summary["accepting_sellers"] == 3
