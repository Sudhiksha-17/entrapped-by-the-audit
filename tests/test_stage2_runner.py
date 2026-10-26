"""Campaign runner and prereg freeze tests (fake client only, temporary files, no network)."""
import json
from pathlib import Path

import pytest
import yaml

import sting.docs
import sting.minimal_runner as mr
from sting.freeze_prereg import BASE_FILES, PreregNotFrozen, freeze, verify
from sting.paths import REPO_ROOT
from sting.stage2_runner import block_order, run_campaign


def arm_cfg(condition, prompt="default", run_type="exploratory", budget=None):
    c = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    c.update(stage="stage2test", run_type=run_type, run_name=f"t_{condition}_{prompt}", rounds=12, concurrency=1,
             seller_prompt=prompt, max_api_attempts_per_episode=200,
             sting={"condition": condition, "pricing_rule": "follow", "initial_ask": 97.5,
                    "stimuli_file": "configs/stage2_stimuli.yaml"})
    if budget:
        c["budget"] = budget
    return c


def write_campaign(root: Path, arms, indices=(0, 1, 2), **kw):
    (root / "configs").mkdir(parents=True, exist_ok=True)
    entries = []
    for name, cell, arm, cfg in arms:
        p = f"configs/{name}.yaml"
        (root / p).write_text(yaml.safe_dump(cfg), encoding="utf-8")
        entries.append({"name": name, "cell": cell, "arm": arm, "config": p})
    campaign = {"name": "testcamp", "stage": "stage2test", "run_type": kw.pop("run_type", "exploratory"),
                "n_per_arm": len(indices), "indices": list(indices), "concurrency": 2, "order_seed": 7,
                "max_replacement_passes": 2, "arms": entries, **kw}
    (root / "configs" / "camp.yaml").write_text(yaml.safe_dump(campaign), encoding="utf-8")
    return Path("configs/camp.yaml")


def test_block_order_is_deterministic_and_varies_by_block():
    names = ["a", "b", "c", "d", "e", "f"]
    assert block_order(names, 7, 0) == block_order(names, 7, 0)
    assert sorted(block_order(names, 7, 3)) == sorted(names)
    assert len({tuple(block_order(names, 7, k)) for k in range(10)}) > 1


def test_campaign_interleaves_blocks_and_documents_each_arm(tmp_path):
    root = tmp_path / "repo"
    camp = write_campaign(root, [("silent_low", "mini-low", "silent", arm_cfg("silent")),
                                 ("offer_low", "mini-low", "offer", arm_cfg("offer")),
                                 ("offer_vol", "4.1-low", "offer", arm_cfg("offer", "volume"))])
    runs = tmp_path / "runs"
    out = run_campaign(camp, "campaign test", runs_dir=runs, root=root)
    assert out["completed_per_arm"] == {"silent_low": 3, "offer_low": 3, "offer_vol": 3}
    log = json.loads(Path(out["log"]).read_text())
    assert [b["index"] for b in log["blocks"]] == [0, 1, 2]
    assert all(sorted(e["arm"] for e in b["episodes"]) == ["offer_low", "offer_vol", "silent_low"] for b in log["blocks"])
    for name, info in log["arms"].items():
        run_dir = Path(info["run_dir"])
        cfg = json.loads((run_dir / "run_config.json").read_text())
        assert cfg["campaign_id"] == out["campaign_id"] and cfg["config"]["arm"] in ("silent", "offer")
        assert (run_dir / "run_summary.json").is_file() and (run_dir / "manifest.json").is_file()
        reps = sorted(p.name[-4:] for p in run_dir.iterdir() if p.is_dir())
        assert reps == ["r000", "r001", "r002"]


def test_failed_episodes_are_replaced_with_same_index_until_n(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    camp = write_campaign(root, [("offer_low", "mini-low", "offer", arm_cfg("offer"))], indices=(0, 1))
    real = mr._run_episode
    calls = {"n": 0}

    def flaky(cfg, run_dir, k, rid, replaces=None):
        calls["n"] += 1
        if calls["n"] == 1:  # first episode fails
            raise_cfg = dict(cfg, sellers=[{"provider": "fake", "model": "fake-model", "fail_on_round": 2}] + cfg["sellers"][1:])
            return real(raise_cfg, run_dir, k, rid, replaces)
        return real(cfg, run_dir, k, rid, replaces)
    monkeypatch.setattr(mr, "_run_episode", flaky)
    out = run_campaign(camp, "replacement test", runs_dir=tmp_path / "runs", root=root)
    assert out["completed_per_arm"] == {"offer_low": 2} and out["shortfall_per_arm"] == {"offer_low": 0}
    log = json.loads(Path(out["log"]).read_text())
    (ep,) = log["replacement_passes"][0][0]["episodes"]
    assert ep["status"] == "completed" and ep["replicate_id"].endswith("_r000_repl1") and ep["replaces"].endswith("_r000")


def test_confirmatory_campaign_needs_a_frozen_prereg(tmp_path, monkeypatch):
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [])
    root = tmp_path / "repo"
    budget = {"group": "camp", "cap_usd": 5.0}
    camp = write_campaign(root, [("offer_low", "mini-low", "offer", arm_cfg("offer", run_type="confirmatory", budget=budget))],
                          run_type="confirmatory", budget=budget)

    def not_frozen(path):
        raise PreregNotFrozen("prereg/FROZEN.json not found")
    with pytest.raises(PreregNotFrozen):
        run_campaign(camp, "x", runs_dir=tmp_path / "runs", root=root, frozen_check=not_frozen)


def test_campaign_rejects_mismatched_budget_or_run_type(tmp_path):
    root = tmp_path / "repo"
    camp = write_campaign(root, [("a", "mini-low", "offer", arm_cfg("offer", run_type="pilot"))])
    with pytest.raises(ValueError, match="run_type"):
        run_campaign(camp, "x", runs_dir=tmp_path / "runs", root=root)


def test_campaign_budget_cap_refuses(tmp_path):
    root = tmp_path / "repo"
    budget = {"group": "capped", "cap_usd": 0.5}
    cfg = arm_cfg("offer", budget=budget)
    cfg["estimated_cost_per_episode_usd"] = 0.3
    camp = write_campaign(root, [("a", "mini-low", "offer", cfg)], budget=budget)
    with pytest.raises(SystemExit, match="Budget cap refused"):
        run_campaign(camp, "x", runs_dir=tmp_path / "runs", root=root)


def make_freeze_root(tmp_path):
    root = tmp_path / "frz"
    for f in BASE_FILES:
        (root / f).parent.mkdir(parents=True, exist_ok=True)
        (root / f).write_text(f"content of {f}\n", encoding="utf-8")
    (root / "configs").mkdir(exist_ok=True)
    (root / "configs" / "arm.yaml").write_text("x: 1\n", encoding="utf-8")
    (root / "configs" / "camp.yaml").write_text(yaml.safe_dump({"arms": [{"config": "configs/arm.yaml"}]}), encoding="utf-8")
    return root


def test_freeze_refuses_blanks_and_dirty_tree_and_verify_detects_changes(tmp_path):
    root = make_freeze_root(tmp_path)
    camp = Path("configs/camp.yaml")
    with pytest.raises(PreregNotFrozen, match="uncommitted"):
        freeze(camp, root, uncommitted=[" M x"])
    (root / "prereg" / "PREREG.md").write_text("draft [[BLANK: N]]\n", encoding="utf-8")
    with pytest.raises(PreregNotFrozen, match="BLANK"):
        freeze(camp, root, uncommitted=[])
    (root / "prereg" / "PREREG.md").write_text("final\n", encoding="utf-8")
    with pytest.raises(PreregNotFrozen, match="not found"):
        verify(camp, root)
    lock = freeze(camp, root, uncommitted=[])
    assert set(lock["files_sha256"]) == set(BASE_FILES) | {"configs/camp.yaml", "configs/arm.yaml"}
    assert verify(camp, root)["sha256_of_lock"]
    with pytest.raises(FileExistsError):
        freeze(camp, root, uncommitted=[])
    (root / "configs" / "arm.yaml").write_text("x: 2\n", encoding="utf-8")
    with pytest.raises(PreregNotFrozen, match="changed"):
        verify(camp, root)



def test_replacement_stops_after_max_passes_and_reports_shortfall_with_reasons(tmp_path):
    root = tmp_path / "repo"
    bad = arm_cfg("offer")
    bad["sellers"] = [{"provider": "fake", "model": "fake-model", "fail_on_round": 2}] + bad["sellers"][1:]
    camp = write_campaign(root, [("offer_low", "mini-low", "offer", bad)], indices=(0, 1))  # max_replacement_passes 2
    out = run_campaign(camp, "systematic failure test", runs_dir=tmp_path / "runs", root=root)
    assert out["completed_per_arm"] == {"offer_low": 0} and out["shortfall_per_arm"] == {"offer_low": 2}
    assert out["replacement_passes_used"] == 2
    assert out["failure_reasons_per_arm"] == {"offer_low": {"api_failure": 6}}  # 2 originals + 2 x 2 replacements



def test_campaign_runs_only_selected_blocks_and_can_defer_replacement(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    bad = arm_cfg("offer")
    bad["sellers"] = [{"provider": "fake", "model": "fake-model", "fail_on_round": 2}] + bad["sellers"][1:]
    camp = write_campaign(root, [("good", "mini-low", "offer", arm_cfg("offer")), ("bad", "mini-low", "sham", bad)],
                          indices=(0, 1, 2))
    out = run_campaign(camp, "block 0", runs_dir=tmp_path / "runs", root=root, only_indices=[0], skip_replacement=True)
    log = json.loads(Path(out["log"]).read_text())
    assert [b["index"] for b in log["blocks"]] == [0] and log["replacement_passes"] == []
    assert out["completed_per_arm"] == {"good": 1, "bad": 0} and out["shortfall_per_arm"] == {"good": 0, "bad": 1}
    with pytest.raises(ValueError, match="not in the campaign"):
        run_campaign(camp, "x", runs_dir=tmp_path / "runs", root=root, only_indices=[7])


def test_confirmatory_reports_withhold_outcome_tables(tmp_path, monkeypatch):
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [])
    cfg = arm_cfg("offer", run_type="confirmatory", budget={"group": "blind", "cap_usd": 5.0})
    cfg["rounds"] = 12
    s = mr.run_batch(cfg, runs_dir=tmp_path, replicate_indices=[0], purpose="blind report")
    report = (tmp_path / "_docs" / "results" / "runs" / s["run_id"] / "report.md").read_text()
    assert "Withheld: confirmatory run" in report and "Mean seller ask" not in report


def test_health_script_reports_without_outcome_fields(tmp_path):
    import subprocess
    import sys as _sys
    root = tmp_path / "repo"
    camp = write_campaign(root, [("offer_low", "mini-low", "offer", arm_cfg("offer")),
                                 ("silent_low", "mini-low", "silent", arm_cfg("silent"))], indices=(0,))
    out = run_campaign(camp, "health test", runs_dir=tmp_path / "runs", root=root)
    target = tmp_path / "health.json"
    res = subprocess.run([_sys.executable, "-I", str(REPO_ROOT / "scripts" / "stage2_health.py"), out["log"], str(target)],
                         capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    health = json.loads(target.read_text())
    ep = health["arms"]["offer_low"]["episodes"][0]
    assert ep["manipulation_check"]["passed"] is True and ep["sting_rule_mismatch_rounds"] == 0
    assert health["arms"]["silent_low"]["episodes"][0]["manipulation_check"] is None
    text = target.read_text() + res.stdout
    for forbidden in ("seller_asks", "buyer_bids", "trade", "outcome", "colluding", "mean_ask"):
        assert forbidden not in text



def test_checkpoint_flags_failures_over_ten_percent(tmp_path, monkeypatch):
    import subprocess
    import sys as _sys
    root = tmp_path / "repo"
    bad = arm_cfg("offer")
    bad["sellers"] = [{"provider": "fake", "model": "fake-model", "fail_on_round": 2}] + bad["sellers"][1:]
    camp = write_campaign(root, [("mini-low_offer", "mini-low", "offer", arm_cfg("offer")),
                                 ("mini-low_sham", "mini-low", "sham", bad)], indices=(0,))
    out = run_campaign(camp, "checkpoint test", runs_dir=tmp_path / "runs", root=root, skip_replacement=True)
    md, js = tmp_path / "cp.md", tmp_path / "cp.json"
    res = subprocess.run([_sys.executable, "-I", str(REPO_ROOT / "scripts" / "stage2_checkpoint.py"), str(md), str(js), out["log"]],
                         capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    cp = json.loads(js.read_text())
    assert cp["stop"] is True and "mini-low_sham" in cp["stop_conditions"]["failure_rate_over_10pct"]
    for forbidden in ("seller_asks", "buyer_bids", '"outcome"', "colluding", "trades_after", "mean_ask", "price"):
        assert forbidden not in js.read_text()


def test_labeling_sheet_hides_arm_and_keeps_key_separate(tmp_path):
    import subprocess
    import sys as _sys
    root = tmp_path / "repo"
    cfgs = {c: {**arm_cfg(c), "rounds": 20} for c in ("silent", "offer", "sham")}
    camp = write_campaign(root, [("mini-low_silent", "mini-low", "silent", cfgs["silent"]),
                                 ("mini-low_offer", "mini-low", "offer", cfgs["offer"]),
                                 ("mini-low_sham", "mini-low", "sham", cfgs["sham"])], indices=(0, 1))
    out = run_campaign(camp, "labeling test", runs_dir=tmp_path / "runs", root=root)
    sheet_dir, key_dir = tmp_path / "sheet", tmp_path / "key"
    res = subprocess.run([_sys.executable, "-I", str(REPO_ROOT / "scripts" / "stage2_labeling_sheet.py"), str(sheet_dir),
                          str(key_dir), str(root / camp), out["log"]], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    sheet = json.loads((sheet_dir / "labeling_sheet.json").read_text())
    key = json.loads((key_dir / "labeling_key.json").read_text())
    assert len(sheet) == 30 and set(key) == {s["item_id"] for s in sheet}
    assert {k["condition"] for k in key.values()} == {"offer", "sham"}
    for s in sheet:
        assert set(s) == {"item_id", "sting_message", "fields"}
    assert not list(sheet_dir.glob("*key*"))


def test_supplementary_draw_quota_round11_exclusion_and_determinism():
    import importlib.util
    import sys as _sys
    _sys.path.insert(0, str(REPO_ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location("supp", REPO_ROOT / "scripts" / "stage2_labeling_supp.py")
    supp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(supp)
    items = [{"condition": c, "cell": cell, "arm": f"{cell}_{c}", "replicate_id": f"r{k:03d}", "seller": s, "round": rnd}
             for (c, cell) in supp.QUOTA for k in range(10) for s in ("A", "B") for rnd in (11, 12)]
    excluded = ("r000", "A", 11)
    a = supp.draw(items, {excluded})
    assert a == supp.draw(items, {excluded})
    assert len(a) == 30 and {i["round"] for i in a} == {11}
    assert {k: sum((i["condition"], i["cell"]) == k for i in a) for k in supp.QUOTA} == supp.QUOTA
    big = supp.draw(items, {excluded}, quota={("sham", "mini-low"): 19})
    assert len(big) == 19 and excluded not in {(i["replicate_id"], i["seller"], i["round"]) for i in big}
    with pytest.raises(SystemExit):
        supp.draw([i for i in items if i["condition"] != "rapport"], set())
