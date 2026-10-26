"""All 15 stimuli pass the manipulation check under the exact Stage 2 arm configs (human message 23).

Each message-arm config in configs/stage2/ is loaded unchanged except that every model is replaced by the fake
client (no network) and outputs go to a temporary directory. Replicate indices 0, 1, 2 cover the three paraphrases
(index mod 3). Confirmatory configs require a clean tree; the check is bypassed here only for the temporary run.
"""
import json
from pathlib import Path

import pytest
import yaml

import sting.docs
from sting.minimal_runner import run_batch
from sting.paths import REPO_ROOT

STIM = yaml.safe_load((REPO_ROOT / "configs" / "stage2_stimuli.yaml").read_text(encoding="utf-8"))
ARM_CONFIGS = sorted(p for p in (REPO_ROOT / "configs" / "stage2").glob("*.yaml")
                     if p.name != "campaign.yaml" and not p.name.endswith("_silent.yaml"))
FAKE = {"provider": "fake", "model": "fake-model"}


def test_message_arm_configs_cover_all_five_conditions():
    conditions = {yaml.safe_load(p.read_text(encoding="utf-8"))["sting"]["condition"] for p in ARM_CONFIGS}
    assert conditions == {"sham", "anchor", "rapport", "directive", "offer"} and len(ARM_CONFIGS) == 8


def test_longest_stimulus_is_below_every_configured_limit():
    longest = max(len(t) for c in STIM["messages"].values() for t in c.values())
    for p in ARM_CONFIGS:
        assert longest < yaml.safe_load(p.read_text(encoding="utf-8"))["max_message_length"]


@pytest.mark.parametrize("config_path", ARM_CONFIGS, ids=lambda p: p.stem)
def test_every_paraphrase_passes_the_manipulation_check(tmp_path, monkeypatch, config_path):
    monkeypatch.setattr(sting.docs, "uncommitted_changes", lambda: [])
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    cfg["sellers"] = [dict(FAKE) for _ in cfg["sellers"]]
    cfg["buyers"] = [dict(FAKE) for _ in cfg["buyers"]]
    # approve_cost: the configured estimates are for real models; this run uses the fake client (no cost, no network).
    summary = run_batch(cfg, runs_dir=tmp_path, replicate_indices=[0, 1, 2], approve_cost=True,
                        purpose="manipulation check, fake client")
    assert summary["completed"] == 3 and summary["failed"] == 0
    seen = set()
    for rep in (p for p in Path(summary["run_dir"]).iterdir() if p.is_dir()):
        status = json.loads((rep / "status.json").read_text(encoding="utf-8"))
        log = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
        assert status["manipulation_check"] == {"round": 11, "passed": True, "missing": []}
        assert log["messages_sent"][0]["text"] == STIM["messages"][cfg["sting"]["condition"]][log["message_id"]]
        seen.add(log["message_id"])
    assert len(seen) == 3
