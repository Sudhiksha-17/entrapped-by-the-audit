"""Study 1R-D fresh Cell B (human message 88): configs differ from the first Cell B only in provider, names, budget and
cost; the lock covers amendment, addendum, campaign, configs and code. No model calls."""
import importlib.util
from pathlib import Path

import yaml

from sting import study1rd_b2
from sting.paths import REPO_ROOT


def test_b2_configs_change_only_provider_names_budget_and_cost(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("mkb2", REPO_ROOT / "scripts" / "make_study1rd_b2_configs.py")
    mk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mk)
    monkeypatch.setattr(mk, "OUT", tmp_path)
    monkeypatch.setattr("sys.argv", ["x", "--provider", "venice", "--key", "qwenv", "--cost", "0.10"])
    mk.main()
    camp = yaml.safe_load((tmp_path / "campaign.yaml").read_text(encoding="utf-8"))
    assert [a["arm"] for a in camp["arms"]] == ["silent", "silent_floor", "offer_floor"]
    assert all(a["indices"] == list(range(33)) for a in camp["arms"])
    for arm in ("silent", "silent_floor", "offer_floor"):
        new = yaml.safe_load((tmp_path / f"qwenv_{arm}.yaml").read_text(encoding="utf-8"))
        old = yaml.safe_load((REPO_ROOT / "configs" / "study1r_addon_D" / f"qwen_{arm}.yaml").read_text(encoding="utf-8"))
        diff = {k for k in set(new) | set(old) if new.get(k) != old.get(k)}
        assert diff <= {"stage", "run_name", "estimated_cost_per_episode_usd", "budget", "sellers", "buyers"}
        for a_new, a_old in zip(new["sellers"] + new["buyers"], old["sellers"] + old["buyers"]):
            assert {k for k in a_new if a_new[k] != a_old.get(k)} == {"openrouter_provider"}
            assert a_new["openrouter_provider"] == "venice" and a_new["model"] == "qwen/qwen3-235b-a22b-2507"
        assert new["sting"] == old["sting"] and new["temperature"] == old["temperature"]


def test_b2_lock_covers_addendum_and_code():
    files = study1rd_b2.FILES
    assert "prereg_study1r/AMENDMENT_1RD.md" in files and "prereg_study1r/AMENDMENT_1RD_ADDENDUM_1.md" in files
    assert "sting/study1rd_b2.py" in files and "scripts/make_study1rd_b2_configs.py" in files
    assert study1rd_b2.LOCK_NAME == "FROZEN_1RD_B2.json"
