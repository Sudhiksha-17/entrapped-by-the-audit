"""Stage 1a pilot log check (read-only, no API calls).

For each episode in the given run directories: run health (status, calls, errors, retries, parse
failures split by role, provider_unknown, routed providers, returned models, log errors), sting
checks (every logged sting ask equals the follow rule recomputed from the logged history; the sting
never appears as a message sender; messages it received), LLM-seller messaging (each LLM seller's
messages per round, and whether each LLM seller's prompt shows the other's previous-round message),
missing LLM-seller asks, and cost by role.

Usage: python scripts/stage1a_pilot_check.py results/stage1a/pilot_check.json runs/stage1a/<run_id> ...
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.sting_seller import follow_ask  # noqa: E402


def rounds_of(logs: Path) -> list[dict]:
    text = (logs / "auction_results.md").read_text(encoding="utf-8")
    return [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````", text, flags=re.S)]


def check(rep: Path) -> dict:
    status = json.loads((rep / "status.json").read_text(encoding="utf-8"))
    setup = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))
    calls = [json.loads(l) for l in (rep / "calls.jsonl").read_text(encoding="utf-8").splitlines()]
    logs = rep / "upstream_logs"
    rounds = rounds_of(logs)
    sting_id, llm = setup["sting_id"], setup["llm_seller_ids"]
    sting_cfg = setup["models"][sting_id]
    sting_log_floor = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
    floor, floor_from = sting_log_floor.get("price_floor"), sting_log_floor.get("floor_from_round")
    mismatches = []
    for i, r in enumerate(rounds):
        expected = follow_ask([x["seller_asks"] for x in rounds[:i]], llm, sting_cfg["initial_ask"])
        if floor is not None and r["round_number"] >= floor_from:  # max(X, follow) arms (stage2_spec section 4)
            expected = round(max(floor, expected), 2)
        if r["seller_asks"].get(sting_id) != expected:
            mismatches.append({"round": r["round_number"], "logged": r["seller_asks"].get(sting_id), "expected": expected})
    sting_log = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
    seen_other = {}
    for s in llm:
        other = [x for x in llm if x != s][0]
        prompts = (logs / f"{s}.md").read_text(encoding="utf-8")
        seen_other[s] = sum(1 for r in rounds[:-1] if other in r["seller_messages"]
                            and f"- From {other}: {r['seller_messages'][other]}" in prompts)
    by_role_parse = collections.Counter(c["role"] for c in calls if c.get("parse_failed"))
    return {
        "replicate_id": rep.name, "model": setup["models"][llm[0]]["model"], "boss_pressure": setup.get("boss_pressure"),
        "status": status["status"], "failure_reason": status.get("failure_reason"),
        "rounds": status["rounds_completed"], "wall_clock_s": status["wall_clock_s"],
        "calls": len(calls), "errors": [c["error"] for c in calls if c["error"]],
        "retries": sum(1 for c in calls if c["attempts"] > 1),
        "parse_failures_total": status["parse_failures"], "parse_failures_by_role": dict(by_role_parse),
        "provider_unknown_calls": status["provider_unknown_calls"],
        "routed": dict(collections.Counter(str(c["routed_provider"]) for c in calls)),
        "returned_models": dict(collections.Counter(str(c["returned_model"]) for c in calls)),
        "log_error_lines": sum(1 for l in (logs / "unified.log").read_text(encoding="utf-8").splitlines()
                               if "ERROR" in l or "Traceback" in l),
        "sting_ask_rule_mismatches": mismatches, "sting_in_message_senders": any(sting_id in r["seller_messages"] for r in rounds),
        "sting_messages_sent": sting_log["messages_sent"], "sting_messages_received": len(sting_log["received_messages"]),
        "llm_seller_messages_per_round": [sorted(x for x in r["seller_messages"] if x in llm) for r in rounds],
        "llm_seller_saw_other_message_rounds": seen_other,
        "missing_llm_asks": [{"round": r["round_number"], "seller": s} for r in rounds for s in llm if s not in r["seller_asks"]],
        "tokens_in": sum(c["tokens_in"] for c in calls), "tokens_out": sum(c["tokens_out"] for c in calls),
        "cost_by_role": {k: round(v["cost_usd_reported"], 7) for k, v in status["usage_by_role"].items()},
        "cost_total": round(sum(c["cost_usd_reported"] or 0 for c in calls), 7),
    }


def main() -> None:
    out = [check(rep) for run in sys.argv[2:] for rep in sorted(p for p in Path(run).iterdir() if p.is_dir())]
    Path(sys.argv[1]).parent.mkdir(parents=True, exist_ok=True)
    Path(sys.argv[1]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    for e in out:
        print(e["replicate_id"][-48:], e["status"], e["failure_reason"], "rounds", e["rounds"], "calls", e["calls"],
              "errors", len(e["errors"]), "retries", e["retries"], "parse", e["parse_failures_total"], e["parse_failures_by_role"],
              "prov_unknown", e["provider_unknown_calls"], "routed", e["routed"], "returned", e["returned_models"],
              "log_err", e["log_error_lines"])
        print("   sting mismatches", len(e["sting_ask_rule_mismatches"]), "sting sent", len(e["sting_messages_sent"]),
              "sting in senders", e["sting_in_message_senders"], "received", e["sting_messages_received"],
              "| llm msgs/round min", min(len(x) for x in e["llm_seller_messages_per_round"]),
              "saw-other", e["llm_seller_saw_other_message_rounds"], "missing llm asks", len(e["missing_llm_asks"]),
              "| cost", e["cost_total"], e["cost_by_role"], "tokens", e["tokens_in"], e["tokens_out"])
        for err in e["errors"][:3]:
            print("   ERR", err[:200])


if __name__ == "__main__":
    main()
