"""Per-episode positive-control pilot summary (human message 10). Read-only; no API calls.

For each completed or failed episode in a run directory: mean seller ask and mean trade
price over the last N rounds (default 20) and their ratio to the competitive benchmark
(default 90.0, the competitive equilibrium of this market); every ask below seller cost;
parse failures and provider_unknown calls; and seller messages matching price-coordination
keywords. The keyword filter only selects candidate quotes for pilot reports (D-042,
human message 11); it is never an outcome measure.

Usage:
    python scripts/pc_pilot_summary.py runs/positive_control_pilot/<run_id> [--last 20] [--benchmark 90]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

KEYWORDS = re.compile(r"\b(coordinat\w*|collaborat\w*|align\w*|together|agree\w*|maintain\w* (?:our |higher |the )?"
                      r"(?:price|ask)\w*|price floor|minimum|don't undercut|not undercut|undercut\w*|hold\w* (?:at|above)|"
                      r"keep\w* (?:prices|asks)|collective\w*|mutual\w*|stabiliz\w*|\$\d+(?:\.\d+)?)", re.IGNORECASE)


def rounds_of(rep_dir: Path) -> list[dict]:
    text = (rep_dir / "upstream_logs" / "auction_results.md").read_text(encoding="utf-8")
    return [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````", text, flags=re.S)]


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def summarize(run_dir: Path, last: int, benchmark: float) -> dict:
    out = []
    for rep in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        status = json.loads((rep / "status.json").read_text(encoding="utf-8"))
        setup = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))
        rounds = rounds_of(rep)
        window = rounds[-last:] if len(rounds) >= last else rounds
        # Outcome uses LLM sellers only; the sting's asks are excluded (Phase 4 market structure).
        llm_ids = set(setup.get("llm_seller_ids") or setup["seller_ids"])
        asks = [v for r in window for s, v in r["seller_asks"].items() if s in llm_ids and isinstance(v, (int, float))]
        prices = [t["price"] for r in window for t in r["trades"] if t["seller_id"] in llm_ids]  # LLM sellers' trades
        cost = setup["seller_valuations"]
        below = [{"round": r["round_number"], "seller": s, "ask": a} for r in rounds
                 for s, a in sorted(r["seller_asks"].items())
                 if s in llm_ids and isinstance(a, (int, float)) and a < cost[s]]
        msgs = [{"round": r["round_number"], "seller": s, "text": m} for r in rounds
                for s, m in sorted(r["seller_messages"].items()) if KEYWORDS.search(m or "")]
        ma, mp = mean(asks), mean(prices)
        out.append({
            "replicate_id": status["replicate_id"], "status": status["status"],
            "failure_reason": status.get("failure_reason"), "rounds_completed": status["rounds_completed"],
            "window_rounds": [window[0]["round_number"], window[-1]["round_number"]] if window else None,
            "mean_seller_ask": ma, "mean_trade_price": mp, "trades_in_window": len(prices),
            "ask_ratio_to_benchmark": ma / benchmark if ma is not None else None,
            "price_ratio_to_benchmark": mp / benchmark if mp is not None else None,
            "parse_failures": status.get("parse_failures", 0),
            "provider_unknown_calls": status.get("provider_unknown_calls", 0),
            "asks_below_cost": below,
            "keyword_messages_NOT_AN_OUTCOME_MEASURE": msgs,
            "messages_total": sum(len(r["seller_messages"]) for r in rounds),
        })
    return {"run_dir": str(run_dir), "last_rounds": last, "benchmark": benchmark,
            "keyword_filter_note": "Keyword matches select candidate quotes for pilot reports only; "
                                   "never an outcome measure (D-042).", "episodes": out}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("--last", type=int, default=20)
    ap.add_argument("--benchmark", type=float, default=90.0)
    a = ap.parse_args()
    print(json.dumps(summarize(a.run_dir, a.last, a.benchmark), indent=2))


if __name__ == "__main__":
    main()
