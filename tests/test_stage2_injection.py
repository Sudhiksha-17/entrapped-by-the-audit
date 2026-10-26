"""Stage 2 message injection tests (fake LLM clients only, no network)."""
import json
import re
from pathlib import Path

import pytest
import yaml

from sting.minimal_runner import run_batch, stimulus_for
from sting.paths import REPO_ROOT
from sting.sting_seller import StingSeller

SPEC = REPO_ROOT / "prereg" / "stage2_message_and_judge.md"
STIM = yaml.safe_load((REPO_ROOT / "configs" / "stage2_stimuli.yaml").read_text(encoding="utf-8"))


def spec_tables() -> dict[str, str]:
    text = SPEC.read_text(encoding="utf-8")
    section = text[text.index("## 2. Messages"):text.index("### Notes for the limitations section")]
    return {m.group(1): m.group(2) for m in re.finditer(r"^\| ([SARDO][123]) \| (.+?) \| \d+ \|$", section, flags=re.M)}


def test_stimuli_match_the_spec_verbatim():
    table = spec_tables()
    assert len(table) == 15
    ours = {mid: text for cond in STIM["messages"].values() for mid, text in cond.items()}
    assert ours == table
    assert STIM["x_price"] == 98.00 and STIM["t0"] == 10


def test_judge_prompt_matches_the_spec_verbatim():
    text = SPEC.read_text(encoding="utf-8")
    section = text[text.index("## 3. Judge prompt"):text.index("## 4. Judge validation")]
    block = re.findall(r"```\n(.*?)\n```", section, flags=re.S)[0]
    assert (REPO_ROOT / "sting" / "prompts" / "judge_prompt.jinja2").read_text(encoding="utf-8") == block + "\n"


@pytest.mark.parametrize("index,expected", [(0, "O1"), (1, "O2"), (2, "O3"), (3, "O1"), (31, "O2")])
def test_paraphrase_is_replicate_index_mod_3(index, expected):
    t0, mid, text = stimulus_for({"condition": "offer", "stimuli_file": "configs/stage2_stimuli.yaml"}, index)
    assert (t0, mid, text) == (10, expected, STIM["messages"]["offer"][expected])


def test_silent_condition_has_no_stimulus():
    assert stimulus_for({"mode": "silent"}, 5) == (None, None, None)
    assert stimulus_for({"condition": "silent"}, 5) == (None, None, None)


def make_sting(condition, text=None, t0=None):
    from sting.minimal_runner import build_params
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    return StingSeller(id="Seller C", company="c", valuation=80.0, expt_params=build_params(cfg),
                       pricing_rule="follow", initial_ask=97.5, llm_seller_ids=["Seller A", "Seller B"],
                       condition=condition, t0=t0, message_text=text, message_id="X1" if text else None)


def test_message_only_in_round_t0():
    sting = make_sting("offer", "hello", 10)
    assert [r for r in range(1, 31) if sting.message_at(r)] == [10]
    resp = [sting.generate_bid_response(round_num=r) for r in range(1, 31)]
    assert [i + 1 for i, x in enumerate(resp) if "message_to_sellers" in x] == [10]
    assert sting.sent_messages == [{"round": 10, "message_id": "X1", "text": "hello"}]


def test_condition_validation():
    with pytest.raises(ValueError):
        make_sting("offer", None, 10)
    with pytest.raises(ValueError):
        make_sting("silent", "text", None)


def rounds_of(rep: Path):
    return [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````",
                                              (rep / "upstream_logs" / "auction_results.md").read_text(encoding="utf-8"), flags=re.S)]


@pytest.mark.parametrize("condition", ["sham", "anchor", "rapport", "directive", "offer"])
def test_episode_injects_message_in_round_10_seen_in_round_11(tmp_path, condition):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    cfg.update(rounds=12, replicates=2, concurrency=1,
               sting={"condition": condition, "pricing_rule": "follow", "initial_ask": 97.5,
                      "stimuli_file": "configs/stage2_stimuli.yaml"})
    summary = run_batch(cfg, runs_dir=tmp_path, replicate_indices=[1], purpose="injection test")
    rep = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    expected_id = sorted(STIM["messages"][condition])[1]
    expected = STIM["messages"][condition][expected_id]
    rounds = rounds_of(rep)
    assert [r["round_number"] for r in rounds if "Seller C" in r["seller_messages"]] == [10]
    assert rounds[9]["seller_messages"]["Seller C"] == expected
    for seller in ("Seller A", "Seller B"):
        md = (rep / "upstream_logs" / f"{seller}.md").read_text(encoding="utf-8")
        prompts = {int(m.group(1)): m.group(2) for m in
                   re.finditer(r"## Prompt: Round (\d+) - [^\n]*\n`{6}\n(.*?)\n`{6}", md, flags=re.S)}
        assert f"- From Seller C: {expected}" in prompts[11]
        assert all("From Seller C" not in prompts[r] for r in prompts if r != 11)
    log = json.loads((rep / "sting_log.json").read_text())
    assert log["condition"] == condition and log["message_id"] == expected_id and log["t0"] == 10
    assert log["messages_sent"] == [{"round": 10, "message_id": expected_id, "text": expected}]
    from sting.sting_seller import follow_ask
    floor = condition in ("anchor", "directive", "offer")  # max($98, follow) from round 10 (stage2_spec section 4)
    for i, r in enumerate(rounds):
        rule = follow_ask([x["seller_asks"] for x in rounds[:i]], ["Seller A", "Seller B"], 97.5)
        expected_ask = max(98.0, rule) if floor and r["round_number"] >= 10 else rule
        assert r["seller_asks"]["Seller C"] == expected_ask
    assert log["price_floor"] == (98.0 if floor else None)


def test_floor_rule_only_from_t0_and_never_below_follow():
    sting = make_sting("offer", "hello", 10)
    sting.price_floor, sting.floor_from_round = 98.0, 10
    sting.history = lambda: [{"Seller A": 99.5, "Seller B": 99.0}]
    assert sting.generate_bid_response(round_num=9)["ask"] == 99.25       # before t0: follow only
    assert sting.generate_bid_response(round_num=10)["ask"] == 99.25      # follow above the floor
    sting.history = lambda: [{"Seller A": 85.0, "Seller B": 86.0}]
    assert sting.generate_bid_response(round_num=9)["ask"] == 85.5
    assert sting.generate_bid_response(round_num=10)["ask"] == 98.0       # floor binds from t0
    assert sting.ask_log[-1]["rule_ask"] == 85.5 and sting.ask_log[-1]["floor_applied"] is True


@pytest.mark.parametrize("condition,floor", [("silent", None), ("sham", None), ("rapport", None),
                                             ("anchor", 98.0), ("directive", 98.0), ("offer", 98.0)])
def test_price_floor_by_arm(condition, floor):
    from sting.minimal_runner import price_floor_for
    assert price_floor_for({"condition": condition, "stimuli_file": "configs/stage2_stimuli.yaml"}) == floor



def test_manipulation_check_passes_when_both_sellers_see_the_message(tmp_path):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    cfg.update(rounds=12, replicates=1, sting={"condition": "offer", "pricing_rule": "follow", "initial_ask": 97.5,
                                                "stimuli_file": "configs/stage2_stimuli.yaml"})
    summary = run_batch(cfg, runs_dir=tmp_path, purpose="manipulation check pass")
    rep = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    status = json.loads((rep / "status.json").read_text())
    assert status["status"] == "completed"
    assert status["manipulation_check"] == {"round": 11, "passed": True, "missing": []}


def test_manipulation_check_failure_is_a_failed_episode_counted_per_arm(tmp_path):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    # Upstream truncates messages to max_message_length, so the full sting message never reaches the sellers.
    cfg.update(rounds=12, replicates=1, max_message_length=40,
               sting={"condition": "offer", "pricing_rule": "follow", "initial_ask": 97.5,
                      "stimuli_file": "configs/stage2_stimuli.yaml"})
    summary = run_batch(cfg, runs_dir=tmp_path, purpose="manipulation check fail")
    assert summary["failed"] == 1 and summary["failures_by_reason"] == {"manipulation_check": 1}
    rep = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    status = json.loads((rep / "status.json").read_text())
    assert status["failure_reason"] == "manipulation_check"
    assert status["manipulation_check"]["missing"] == ["Seller A", "Seller B"]


def test_silent_arm_has_no_manipulation_check(tmp_path):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    cfg.update(rounds=12, replicates=1)
    summary = run_batch(cfg, runs_dir=tmp_path, purpose="silent")
    rep = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    assert "manipulation_check" not in json.loads((rep / "status.json").read_text())
