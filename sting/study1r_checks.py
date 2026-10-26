"""Study 1R per-episode manipulation checks (prereg_study1r/STUDY1R_SPEC.md version 2, sections 10-11, gate G2;
STUDY1R_STIMULI.md section 7). Read-only over an episode directory plus the sting's record; no API calls.

Checks (each episode; message arms also the message checks):
- posts: exactly one sting message in every round t0 .. post_until (10-29);
- presence: that round's full message appears as "- From Seller C: <text>" in both LLM sellers' prompts of the next
  round (rounds 11-30);
- follow-up: the logged ASK/ACK state per seller per round equals the rule recomputed from the market's delivered
  previous-round messages (auction_results seller_messages), every ACK has its trigger text logged, and the posted
  text equals the composition of the logged states;
- X: appears exactly where specified (anchor: once, in the sentence; offer: once in the sentence plus once per ACK;
  sham: never). X is capped at 99.99 by construction (human message 40); a capped episode is logged and reported,
  never failed;
- no truncation: no posted message longer than max_message_length;
- sting pricing per rule: the sting's ask in every round equals follow (or max(X, follow) from round 10 in anchor
  and offer), recomputed from the logged asks of earlier rounds;
- pre consistency: the pre used for X equals the outcome measure's pre (rounds 6-9; or the most recent asks).
Silent arms: pricing and pre checks only.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from sting.stage2_measures import rounds_of, window_mean
from sting.sting_seller import competitive_ask, follow_ask
from sting.study1r_stimuli import compose, expected_x_count, segment_state, x_string

PROMPT_RE = re.compile(r"## Prompt: Round (\d+) - [^\n]*\n`{6}\n(.*?)\n`{6}", re.S)


def round_prompts(rep_dir: Path, seller: str) -> dict[int, str]:
    md = rep_dir / "upstream_logs" / f"{seller}.md"
    text = md.read_text(encoding="utf-8") if md.is_file() else ""
    return {int(m.group(1)): m.group(2) for m in PROMPT_RE.finditer(text)}


def pricing_mismatches(rounds: list[dict[str, Any]], record: dict[str, Any], llm_ids: list[str]) -> list[int]:
    bad = []
    for i, r in enumerate(rounds):
        exp = follow_ask([x["seller_asks"] for x in rounds[:i]], llm_ids, record["initial_ask"])
        comp = record.get("competitive")
        if comp is not None and r["round_number"] >= int(comp["from_round"]):
            exp = competitive_ask([x["seller_asks"] for x in rounds[:i]], llm_ids, comp["floor"], comp["step"],
                                  record["initial_ask"])
        if record.get("price_floor") is not None and r["round_number"] >= record["floor_from_round"]:
            exp = round(max(record["price_floor"], exp), 2)
        if r["seller_asks"].get(record["sting_id"]) != exp:
            bad.append(r["round_number"])
    return bad


def outcome_pre(rounds: list[dict[str, Any]], llm_ids: list[str], x_rule: dict[str, Any]) -> tuple[Any, str]:
    lo, hi = x_rule["pre_rounds"]
    pre = window_mean(rounds, llm_ids, range(lo, hi + 1))
    if pre is not None:
        return pre, "pre_rounds"
    before = [r["seller_asks"] for r in rounds if r["round_number"] < int(x_rule["round"])]
    return follow_ask(before, llm_ids, 0.0), "most_recent_asks"


def g2_checks(rep_dir: Path, record: dict[str, Any], llm_ids: list[str], max_len: int) -> dict[str, Any]:
    """`record` = the sting log dict (as written to sting_log.json)."""
    rounds = rounds_of(rep_dir)
    x_log, cond = record["x"], record["condition"]
    x = x_log["x"]
    out: dict[str, Any] = {"x": x, "x_capped": bool(x_log.get("capped")), "uncapped_x": x_log.get("uncapped_x")}
    pre, src = outcome_pre(rounds, llm_ids, record["x_rule"])
    out["pre_consistent"] = src == x_log["source"] and abs(pre - x_log["pre"]) < 1e-9
    out["pricing_mismatch_rounds"] = pricing_mismatches(rounds, record, llm_ids)
    problems = []
    if not out["pre_consistent"]:
        problems.append("pre inconsistent")
    if out["pricing_mismatch_rounds"]:
        problems.append("sting pricing off rule")
    if cond != "silent":
        t0, until = int(record["t0"]), int(record["post_until"])
        sent = {m["round"]: m["text"] for m in record["messages_sent"]}
        out["missing_posts"] = [r for r in range(t0, until + 1) if r not in sent]
        out["extra_posts"] = sorted(r for r in sent if not t0 <= r <= until)
        out["missing_in_prompts"] = {}
        for s in llm_ids:
            prompts = round_prompts(rep_dir, s)
            bad = [r + 1 for r in sorted(sent) if f"- From {record['sting_id']}: {sent[r]}" not in prompts.get(r + 1, "")]
            if bad:
                out["missing_in_prompts"][s] = bad
        delivered = {r["round_number"]: r.get("seller_messages", {}) for r in rounds}
        follow_bad, x_bad = [], []
        logged = {f["round"]: f for f in record["followup_log"]}
        for r in range(t0, until + 1):
            f = logged.get(r)
            if f is None:
                follow_bad.append(r)
                continue
            for s in llm_ids:
                exp_state = "ASK" if r == t0 else segment_state(delivered.get(r - 1, {}).get(s), x)[0]
                trig = f["triggers"].get(s)
                if f["states"][s] != exp_state or (exp_state == "ACK" and not (trig and trig.get("text"))):
                    follow_bad.append(r)
            if r in sent and sent[r] != compose(record["talk"], x, f["states"], llm_ids):
                follow_bad.append(r)
            if r in sent and sent[r].count(x_string(x)) != expected_x_count(cond, f["states"]):
                x_bad.append(r)
        out["followup_mismatch_rounds"] = sorted(set(follow_bad))
        out["x_placement_mismatch_rounds"] = x_bad
        out["messages_over_max_length"] = sorted(r for r, t in sent.items() if len(t) > max_len)
        out["ack_rounds"] = {s: [f["round"] for f in record["followup_log"] if f["states"].get(s) == "ACK"] for s in llm_ids}
        for key, label in (("missing_posts", "missing posts"), ("extra_posts", "extra posts"),
                           ("missing_in_prompts", "message missing from prompts"),
                           ("followup_mismatch_rounds", "follow-up rule mismatch"),
                           ("x_placement_mismatch_rounds", "X placement mismatch"),
                           ("messages_over_max_length", "truncation")):
            if out[key]:
                problems.append(label)
        out["rounds_checked"] = [r + 1 for r in range(t0, until + 1)]
    out["problems"] = problems
    out["passed"] = not problems
    return out


def load_record(rep_dir: Path) -> dict[str, Any]:
    return json.loads((rep_dir / "sting_log.json").read_text(encoding="utf-8"))
