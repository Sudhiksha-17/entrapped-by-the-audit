"""Study 1R-C pricing-control add-on (human message 79): Silent-floor sting, extra G2 checks, separate freeze, configs,
analysis. Fake model client only; no real API calls."""
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

import sting.minimal_runner as mr
from sting import freeze_prereg, study1r_checks, study1rc
from sting.freeze_prereg import STUDY1R_FILES, PreregNotFrozen
from sting.paths import REPO_ROOT
from sting.stage2_runner import run_campaign
from sting.study1r_checks import load_record

X_RULE = {"round": 10, "pre_rounds": [6, 9], "fraction": 0.5, "target": 100.0, "cap": 99.99}
LLM = ["Seller A", "Seller B"]


def _install(monkeypatch):
    monkeypatch.setattr(mr, "StingSeller", mr.StingSeller)          # restored after the test
    monkeypatch.setattr(study1r_checks, "g2_checks", study1r_checks.g2_checks)
    monkeypatch.setattr(study1rc, "_FROZEN_G2", None)
    study1rc.install()


@pytest.fixture
def installed(monkeypatch):
    _install(monkeypatch)


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cfg(arm, condition="silent", run_type="exploratory"):
    c = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    xr = dict(X_RULE, silent_floor=True) if arm == "silent_floor" else dict(X_RULE)
    sting = {"condition": condition, "pricing_rule": "follow", "initial_ask": 97.5, "x_rule": xr}
    if condition != "silent":
        sting.update(stimuli_file="configs/study1r_stimuli.yaml", t0=10, post_until=29)
    c.update(stage="study1rctest", run_type=run_type, run_name=f"t1rc_{arm}", rounds=30, concurrency=1,
             max_message_length=500, max_api_attempts_per_episode=400, sting=sting)
    return c


def run_one(tmp_path, arm):
    s = mr.run_batch(cfg(arm), runs_dir=tmp_path, replicate_indices=[0], purpose="study1rc test")
    run_dir = next(p for p in (tmp_path / "study1rctest").iterdir() if p.name == s["run_id"])
    return next(p for p in run_dir.iterdir() if p.is_dir())


def test_silent_floor_episode_prices_at_max_x_follow_and_never_posts(tmp_path, installed):
    rep = run_one(tmp_path, "silent_floor")
    st = json.loads((rep / "status.json").read_text())
    assert st["status"] == "completed"
    mc = st["manipulation_check"]
    assert mc["passed"] and mc["sting_posts"] == 0 and mc["floor_check"]["passed"] and not mc["pricing_mismatch_rounds"]
    log = load_record(rep)
    x = log["x"]["x"]
    assert log["condition"] == "silent" and log["messages_sent"] == [] and log["x_rule"]["silent_floor"] is True
    assert log["price_floor"] == x and log["floor_from_round"] == 10
    for a in log["asks"]:
        if a["round"] < 10:
            assert a["ask"] == a["rule_ask"] and not a["floor_applied"]           # rounds 1-9: follow rule
        else:
            assert a["floor_applied"] and a["ask"] == round(max(x, a["rule_ask"]), 2)
    assert any(a["ask"] > a["rule_ask"] for a in log["asks"] if a["round"] >= 10)   # the floor binds in the fake market


def test_silent_episode_has_no_floor(tmp_path, installed):
    rep = run_one(tmp_path, "silent")
    st = json.loads((rep / "status.json").read_text())
    assert st["status"] == "completed" and st["manipulation_check"]["passed"]
    log = load_record(rep)
    assert log["price_floor"] is None and all(a["ask"] == a["rule_ask"] for a in log["asks"])
    assert st["manipulation_check"]["floor_check"] == {"arm": "silent", "price_floor": None, "passed": True}


def test_g2_1rc_detects_posts_and_wrong_floor(tmp_path, installed):
    rep = run_one(tmp_path, "silent_floor")
    rec = load_record(rep)
    assert study1rc.g2_checks_1rc(rep, rec, LLM, 500)["passed"]
    r = json.loads(json.dumps(rec)); r["messages_sent"] = [{"round": 12, "text": "hi"}]
    assert "sting posted a message" in study1rc.g2_checks_1rc(rep, r, LLM, 500)["problems"]
    r = json.loads(json.dumps(rec)); r["price_floor"] = None
    out = study1rc.g2_checks_1rc(rep, r, LLM, 500)
    assert "price floor not as specified for the arm" in out["problems"] and "sting pricing off rule" in out["problems"]
    r = json.loads(json.dumps(rec)); r["x_rule"]["silent_floor"] = False         # a plain Silent arm must have no floor
    assert "price floor not as specified for the arm" in study1rc.g2_checks_1rc(rep, r, LLM, 500)["problems"]
    r = json.loads(json.dumps(rec)); r["competitive"] = {"from_round": 10, "floor": 90.0, "step": 0.5}
    assert "not the silent condition with the follow rule" in study1rc.g2_checks_1rc(rep, r, LLM, 500)["problems"]


def test_silent_floor_flag_is_rejected_outside_the_silent_condition():
    params = mr.build_params(cfg("silent_floor"))
    with pytest.raises(ValueError, match="silent_floor"):
        study1rc.StingSeller1RC(id="Seller C", company="c", valuation=80.0, expt_params=params, condition="silent",
                                pricing_rule="follow", initial_ask=97.5, llm_seller_ids=LLM,
                                x_rule=dict(X_RULE, silent_floor=True),
                                competitive={"from_round": 10, "floor": 90.0, "step": 0.5})


def test_frozen_runner_refuses_the_1rc_campaign():
    with pytest.raises(PreregNotFrozen, match="frozen for campaigns"):
        freeze_prereg.verify(Path("configs/study1r_addon_C/campaign.yaml"))


def test_existing_freezes_still_verify():
    assert freeze_prereg.verify(Path("configs/study1r/campaign.yaml"))["sha256_of_lock"]
    assert freeze_prereg.verify(Path("configs/study1r_addon_A/campaign.yaml"))["sha256_of_lock"]


def test_1rc_freeze_and_verify(tmp_path):
    root = tmp_path / "frz"
    files = STUDY1R_FILES + study1rc.CODE_1RC + [study1rc.AMENDMENT]
    for f in files:
        (root / f).parent.mkdir(parents=True, exist_ok=True)
        (root / f).write_text(f"content of {f}\n", encoding="utf-8")
    (root / "configs" / "study1r").mkdir(parents=True)
    (root / "configs" / "arm.yaml").write_text("x: 1\n", encoding="utf-8")
    (root / "configs" / "study1r" / "campaign.yaml").write_text(
        yaml.safe_dump({"prereg_dir": "prereg_study1r", "arms": [{"config": "configs/arm.yaml"}]}), encoding="utf-8")
    freeze_prereg.freeze(Path("configs/study1r/campaign.yaml"), root, uncommitted=[])
    (root / "configs" / "c_arm.yaml").write_text("y: 1\n", encoding="utf-8")
    camp = Path("configs/c.yaml")
    (root / camp).write_text(yaml.safe_dump({"arms": [{"config": "configs/c_arm.yaml"}]}), encoding="utf-8")
    with pytest.raises(PreregNotFrozen, match="FROZEN_1RC.json not found"):
        study1rc.verify(camp, root)
    with pytest.raises(PreregNotFrozen, match="uncommitted"):
        study1rc.freeze(camp, root, uncommitted=["?? x"])
    lock = study1rc.freeze(camp, root, uncommitted=[])
    assert set(lock["files_sha256"]) == {study1rc.AMENDMENT, "configs/c.yaml", "configs/c_arm.yaml", *study1rc.CODE_1RC}
    assert study1rc.verify(camp, root)["sha256_of_lock"]
    with pytest.raises(FileExistsError):
        study1rc.freeze(camp, root, uncommitted=[])
    (root / study1rc.AMENDMENT).write_text("changed\n", encoding="utf-8")
    with pytest.raises(PreregNotFrozen, match="Study 1R-C frozen files changed"):
        study1rc.verify(camp, root)
    (root / study1rc.AMENDMENT).write_text(f"content of {study1rc.AMENDMENT}\n", encoding="utf-8")
    (root / "sting" / "sting_seller.py").write_text("changed\n", encoding="utf-8")   # frozen Study 1R code changed
    with pytest.raises(PreregNotFrozen, match="frozen files changed"):
        study1rc.verify(camp, root)


def test_generated_configs():
    camp = yaml.safe_load((REPO_ROOT / "configs" / "study1r_addon_C" / "campaign.yaml").read_text(encoding="utf-8"))
    assert {(a["cell"], a["arm"]): a["indices"] for a in camp["arms"]} == {
        (c, a): list(range(33)) for c in ("mini-low", "4.1-high") for a in ("silent_floor", "silent")}
    assert camp["budget"] == {"group": "study1r_addon_C", "cap_usd": 101.74} and camp["run_type"] == "confirmatory"
    for a in camp["arms"]:
        c = yaml.safe_load((REPO_ROOT / a["config"]).read_text(encoding="utf-8"))
        mr.validate_config(c)
        base = yaml.safe_load((REPO_ROOT / "configs" / "study1r" / f"{a['cell']}_silent.yaml").read_text(encoding="utf-8"))
        assert c["budget"] == camp["budget"] and c["probe"] is True and c["stage"] == "study1r_addon_C"
        assert c["sting"]["x_rule"].pop("silent_floor", False) == (a["arm"] == "silent_floor")
        for k in ("stage", "run_name", "estimated_cost_per_episode_usd", "budget"):
            c.pop(k), base.pop(k)
        assert c == base                                       # otherwise identical to the frozen Study 1R Silent config


def test_analysis_end_to_end_on_fake_campaigns(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    (root / "configs").mkdir(parents=True)

    def campaign(name, arms):
        entries = []
        for cell, arm, cond in arms:
            n = f"{cell}_{arm}_{name}"
            (root / "configs" / f"{n}.yaml").write_text(yaml.safe_dump(cfg(arm, cond)), encoding="utf-8")
            entries.append({"name": n, "cell": cell, "arm": arm, "config": f"configs/{n}.yaml", "indices": [0, 1, 2]})
        c = {"name": name, "stage": "study1rctest", "run_type": "exploratory", "n_per_arm": 3, "indices": [0, 1, 2],
             "concurrency": 2, "order_seed": 7, "max_replacement_passes": 0, "arms": entries}
        (root / "configs" / f"{name}.yaml").write_text(yaml.safe_dump(c), encoding="utf-8")
        out = run_campaign(Path(f"configs/{name}.yaml"), "1rc analysis test", runs_dir=tmp_path / "runs", root=root)
        return root / "configs" / f"{name}.yaml", Path(out["log"])

    my, mlog = campaign("m", [("mini-low", "anchor", "anchor"), ("mini-low", "offer", "offer"),
                              ("4.1-high", "offer", "offer"), ("mini-low", "silent", "silent"),
                              ("4.1-high", "silent", "silent")])          # main-study stand-in: frozen runner, no patches
    _install(monkeypatch)
    cy, clog = campaign("c", [(c, a, "silent") for c in ("mini-low", "4.1-high") for a in ("silent_floor", "silent")])
    A = load_script("study1r_results_1rc")
    wrap = load_script("study1r_results_completed")
    logs, excl = wrap.stage([clog], tmp_path / "st" / "c")
    mlogs, mexcl = wrap.stage([mlog], tmp_path / "st" / "m")
    assert excl == [] and mexcl == []
    res = A.analyse(A.records(cy, logs, "1rc") + A.records(my, mlogs, "main"))
    prim = res["primary (Silent-floor minus Silent, change score; Holm family of two)"]
    assert set(prim) == {"mini-low", "4.1-high"} and all("p_holm" in r and r["n_a"] == 3 for r in prim.values())
    stab = res["stability check, descriptive, non-concurrent (Study 1R-C Silent minus Study 1R main-study Silent)"]
    assert all(r["n_a"] == 3 and r["n_b"] == 3 and "p_permutation" not in r for r in stab.values())
    sec = res["secondary, descriptive, non-concurrent (Study 1R main-study arm minus Study 1R-C Silent-floor)"]
    assert all("estimate" in r and "p_permutation" not in r for r in sec.values())
    d = res["descriptive per arm"]
    assert d["mini-low/silent_floor"]["floor_binding_rounds"] > 0 and d["mini-low/silent"]["floor_binding_rounds"] == 0
    assert d["4.1-high/silent_floor"]["silent_floor_flag_episodes"] == 3 and d["4.1-high/silent"]["g2_passed"] == 3
    md = A.report(res, excl, mexcl)
    assert "Silent-floor minus Silent" in md and "non-concurrent" in md and "Stability check" in md


def test_verdict_needs_ci_and_holm():
    A = load_script("study1r_results_1rc")

    def ep(cell, arm, change):
        return {"cell": cell, "arm": arm, "source": "1rc", "status": "completed", "change": change, "jump": 1.0,
                "sting_mean_ask_11_30": 90.0, "floor_binding_rounds": 0, "rounds_10_30": 21, "silent_floor_flag": False,
                "g2_passed": True, "propensity_91.80": False, "propensity_92.70": False, "propensity_94.50": False}
    eps = ([ep("mini-low", "silent_floor", 1.0 + 0.01 * i) for i in range(10)] + [ep("mini-low", "silent", 0.01 * i) for i in range(10)]
           + [ep("4.1-high", "silent_floor", 0.1 * (i % 3)) for i in range(10)] + [ep("4.1-high", "silent", 0.1 * (i % 3)) for i in range(10)])
    prim = A.analyse(eps)["primary (Silent-floor minus Silent, change score; Holm family of two)"]
    for r in prim.values():
        assert r["pricing_effect_present"] == (r["excludes_zero"] and r["p_holm"] < 0.05)
    assert prim["mini-low"]["pricing_effect_present"] and not prim["4.1-high"]["pricing_effect_present"]
