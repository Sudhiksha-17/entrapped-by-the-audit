"""Study 1R-D (human message 86): per-arm G2 dispatch, consecutive-API-failure stop, configs, freeze file list.
Fake model client only; no real API calls."""
import importlib.util
import json

import pytest
import yaml

import sting.minimal_runner as mr
import sting.stage2_runner as sr
from sting import study1r_checks, study1rc, study1rd
from sting.paths import REPO_ROOT
from sting.study1r_checks import load_record

X_RULE = {"round": 10, "pre_rounds": [6, 9], "fraction": 0.5, "target": 100.0, "cap": 99.99}


@pytest.fixture
def installed(monkeypatch, tmp_path):
    monkeypatch.setattr(mr, "StingSeller", mr.StingSeller)
    monkeypatch.setattr(study1r_checks, "g2_checks", study1r_checks.g2_checks)
    monkeypatch.setattr(study1rc, "_FROZEN_G2", None)
    monkeypatch.setattr(sr, "run_episode", sr.run_episode)
    return study1rd.install(stop_dir=tmp_path / "stops")


def cfg(arm):
    c = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    condition = "offer" if arm == "offer_floor" else "silent"
    sting = {"condition": condition, "pricing_rule": "follow", "initial_ask": 97.5,
             "x_rule": dict(X_RULE, silent_floor=True) if arm == "silent_floor" else dict(X_RULE)}
    if condition == "offer":
        sting.update(stimuli_file="configs/study1r_stimuli.yaml", t0=10, post_until=29)
    c.update(stage="study1rdtest", run_type="exploratory", run_name=f"t1rd_{arm}", rounds=30, concurrency=1,
             max_message_length=500, max_api_attempts_per_episode=400, sting=sting)
    return c


def run_one(tmp_path, arm):
    s = mr.run_batch(cfg(arm), runs_dir=tmp_path, replicate_indices=[0], purpose="study1rd test")
    run_dir = next(p for p in (tmp_path / "study1rdtest").iterdir() if p.name == s["run_id"])
    return next(p for p in run_dir.iterdir() if p.is_dir())


def test_offer_floor_uses_frozen_message_checks_and_floor(tmp_path, installed):
    rep = run_one(tmp_path, "offer_floor")
    st = json.loads((rep / "status.json").read_text())
    assert st["status"] == "completed"
    mc = st["manipulation_check"]
    assert mc["passed"] and not mc["missing_posts"] and not mc["missing_in_prompts"] and not mc["followup_mismatch_rounds"]
    assert mc["rounds_checked"] == list(range(11, 31))
    log = load_record(rep)
    x = log["x"]["x"]
    assert log["condition"] == "offer" and log["price_floor"] == x and log["floor_from_round"] == 10
    assert all(a["ask"] == round(max(x, a["rule_ask"]), 2) for a in log["asks"] if a["round"] >= 10)


def test_silent_floor_and_silent_use_1rc_checks(tmp_path, installed):
    for arm in ("silent_floor", "silent"):
        st = json.loads((run_one(tmp_path, arm) / "status.json").read_text())
        mc = st["manipulation_check"]
        assert st["status"] == "completed" and mc["passed"] and mc["sting_posts"] == 0 and mc["floor_check"]["passed"]
        assert mc["floor_check"]["arm"] == arm


def test_message_arm_with_silent_floor_flag_fails_g2():
    rec = {"condition": "offer", "competitive": None, "x_rule": dict(X_RULE, silent_floor=True)}
    orig = study1rc._FROZEN_G2
    study1rc._FROZEN_G2 = lambda *a: {"problems": [], "passed": True}
    try:
        out = study1rd.g2_checks_1rd(None, rec, [], 500)
    finally:
        study1rc._FROZEN_G2 = orig
    assert not out["passed"] and "silent_floor flag in a message arm" in out["problems"]


def test_three_consecutive_api_failures_stop_the_campaign(tmp_path, monkeypatch):
    calls = []
    statuses = iter([{"status": "failed", "failure_reason": "api_failure"},
                     {"status": "completed"},
                     {"status": "failed", "failure_reason": "api_failure"},
                     {"status": "failed", "failure_reason": "provider_mismatch"},
                     {"status": "failed", "failure_reason": "attempt_cap"}])

    def fake(*a, **k):
        calls.append(1)
        return dict(next(statuses), replicate_id=f"r{len(calls)}")

    monkeypatch.setattr(sr, "run_episode", fake)
    monkeypatch.setattr(study1r_checks, "g2_checks", study1r_checks.g2_checks)
    monkeypatch.setattr(study1rc, "_FROZEN_G2", None)
    monkeypatch.setattr(mr, "StingSeller", mr.StingSeller)
    study1rd.install(stop_dir=tmp_path)
    for _ in range(4):
        sr.run_episode()                                  # failure, success (reset), failure, failure
    with pytest.raises(study1rd.ConsecutiveApiFailures):
        sr.run_episode()                                  # third consecutive API failure
    with pytest.raises(study1rd.ConsecutiveApiFailures):
        sr.run_episode()                                  # no further episode starts
    assert len(calls) == 5 and len(list(tmp_path.glob("STOPPED_*.json"))) == 1


def test_non_api_failure_resets_the_count():
    g = study1rd.FailureGuard()
    for s in ({"status": "failed", "failure_reason": "api_failure"}, {"status": "failed", "failure_reason": "api_failure"},
              {"status": "failed", "failure_reason": "manipulation_check"}, {"status": "failed", "failure_reason": "api_failure"}):
        g.after(s)
    assert not g.tripped and g.run == 1


def test_cell_a_configs_differ_from_sources_only_in_allowed_keys(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("mk1rd", REPO_ROOT / "scripts" / "make_study1rd_configs.py")
    mk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mk)
    monkeypatch.setattr(mk, "OUT", tmp_path)
    plan = mk.campaign(None, None)
    allowed = {"stage", "run_name", "run_type", "estimated_cost_per_episode_usd", "budget", "replicates"}
    for arm, src in (("offer_floor", "configs/study1r/mini-low_offer.yaml"),
                     ("silent_floor", "configs/study1r_addon_C/mini-low_silent_floor.yaml")):
        new = yaml.safe_load((tmp_path / f"mini-low_{arm}.yaml").read_text(encoding="utf-8"))
        old = yaml.safe_load((REPO_ROOT / src).read_text(encoding="utf-8"))
        assert {k for k in set(new) | set(old) if new.get(k) != old.get(k)} <= allowed
        assert new["replicates"] == 60 and new["budget"]["group"] == "study1r_addon_D"
    camp = yaml.safe_load((tmp_path / "campaign.yaml").read_text(encoding="utf-8"))
    assert [a["indices"] for a in camp["arms"]] == [list(range(60))] * 2 and plan["episodes"] == 120


def test_cell_b_configs_pin_one_provider(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("mk1rd_b", REPO_ROOT / "scripts" / "make_study1rd_configs.py")
    mk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mk)
    monkeypatch.setattr(mk, "OUT", tmp_path)
    plan = mk.campaign("qwen", 0.06)
    camp = yaml.safe_load((tmp_path / "campaign.yaml").read_text(encoding="utf-8"))
    b = [a for a in camp["arms"] if a["cell"] == "qwen"]
    assert [a["arm"] for a in b] == ["silent", "silent_floor", "offer_floor"] and all(a["indices"] == list(range(33)) for a in b)
    for a in b:
        c = yaml.safe_load((tmp_path / f"{a['name']}.yaml").read_text(encoding="utf-8"))
        agents = c["sellers"] + c["buyers"]
        assert len(agents) == 5 and all(x["model"] == "qwen/qwen3-235b-a22b-2507" and x["openrouter_provider"] == "deepinfra"
                                        for x in agents)
    assert plan["episodes"] == 120 + 99


def test_freeze_list_covers_amendment_configs_and_code(tmp_path):
    files = study1rd.campaign_files(__import__("pathlib").Path("configs/study1r_addon_D/campaign.yaml")) \
        if (REPO_ROOT / "configs/study1r_addon_D/campaign.yaml").is_file() else None
    if files is None:
        pytest.skip("campaign not generated yet")
    assert files[0] == study1rd.AMENDMENT and "sting/study1rd.py" in files and "scripts/study1r_results_1rd.py" in files


def test_analysis_verdicts_cell_a_ci_only_cell_b_ci_and_holm():
    spec = importlib.util.spec_from_file_location("r1rd", REPO_ROOT / "scripts" / "study1r_results_1rd.py")
    r = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r)

    def ep(cell, arm, change, source="1rd"):
        return {"cell": cell, "arm": arm, "source": source, "status": "completed", "change": change, "post": 90 + change,
                "jump": 5.0, "sting_mean_ask_11_30": 92.0, "floor_binding_rounds": 0, "rounds_10_30": 21,
                "g2_passed": True, "propensity_91.80": False, "propensity_92.70": False, "propensity_94.50": False,
                "probe": {"Seller A": "NO", "Seller B": "YES"}}
    eps = [ep("mini-low", "offer_floor", 1.0 + 0.01 * i) for i in range(20)] + \
          [ep("mini-low", "silent_floor", 0.0 + 0.01 * i) for i in range(20)] + \
          [ep("B", "offer_floor", 0.01 * i) for i in range(10)] + [ep("B", "silent_floor", 0.01 * i) for i in range(10)] + \
          [ep("B", "silent", -1.0 + 0.01 * i) for i in range(10)] + \
          [ep("mini-low", "silent_floor", 0.5, source="1rc") for _ in range(5)]
    res = r.analyse(eps, ["mini-low", "B"])
    a = res["primary, Cell A (mini-low): Offer-floor minus Silent-floor (words effect)"]
    assert a["words_effect_present"] and "p_holm" not in a
    fam = res["primary, Cell B (B; Holm family of two)"]
    assert not fam["Offer-floor minus Silent-floor (words effect)"]["effect_present"]
    assert fam["Silent-floor minus Silent (price effect)"]["effect_present"]
    assert "p_holm" in fam["Silent-floor minus Silent (price effect)"]
    assert "Cell A" in r.report(res, [], [])
