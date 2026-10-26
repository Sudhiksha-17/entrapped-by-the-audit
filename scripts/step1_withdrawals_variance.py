"""Positive-control pilot step 1: withdrawn asks and variance of the round-level mean ask (human message 12).

Read-only over existing logs; no API calls.

For each episode:
- seller-rounds with no recorded ask, split by what the seller returned: JSON null, the string "null"
  (upstream removes the ask), key missing, or a number that was not recorded (should not happen);
- whether the seller had a standing ask in the queue at that point cannot be read from the round
  logs directly, so the previous round's trade status for that seller is reported (a seller whose
  ask traded in the previous round has no standing ask);
- the round-level mean ask (mean over submitted asks in the round) and its standard deviation over
  rounds 11-30 and over rounds 1-30;
- under three handling rules for missing asks: exclude (mean of submitted asks), carry forward the
  seller's last submitted ask, and replace the round by its mean trade price.

Across episodes of the same model: mean and sample SD of the episode-level means (rounds 11-30).

Usage:
    python scripts/step1_withdrawals_variance.py results/pc_pilot/step1_withdrawals_variance.json runs/positive_control_pilot/<run_id> ...
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path


def responses(md: Path) -> dict[int, dict]:
    text = md.read_text(encoding="utf-8")
    return {int(m.group(1)): json.loads(m.group(3))
            for m in re.finditer(r"## Response: Round (\d+) - [^\n]*\n(`{4,6})json\n(.*?)\n\2", text, flags=re.S)}


def sd(xs):
    return statistics.stdev(xs) if len(xs) > 1 else None


def episode(rep: Path) -> dict:
    setup = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))
    logs = rep / "upstream_logs"
    rounds = [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````",
                                                (logs / "auction_results.md").read_text(encoding="utf-8"), flags=re.S)]
    sellers = setup["seller_ids"]
    resp = {s: responses(logs / f"{s}.md") for s in sellers}
    missing = []
    for i, r in enumerate(rounds):
        for s in sellers:
            if s in r["seller_asks"]:
                continue
            raw = resp[s].get(r["round_number"], {})
            kind = ("key_missing" if "ask" not in raw else "json_null" if raw["ask"] is None
                    else "string_null" if raw["ask"] == "null" else f"other:{raw['ask']!r}")
            traded_prev = i > 0 and any(t["seller_id"] == s for t in rounds[i - 1]["trades"])
            missing.append({"round": r["round_number"], "seller": s, "returned": kind,
                            "traded_in_previous_round": traded_prev})

    def series(rule: str) -> list[float]:
        last: dict[str, float] = {}
        out = []
        for r in rounds:
            asks = {s: a for s, a in r["seller_asks"].items() if isinstance(a, (int, float))}
            last.update(asks)
            if rule == "exclude":
                vals = list(asks.values())
            elif rule == "carry_forward":
                vals = [last[s] for s in sellers if s in last]
            else:  # trade_price: mean trade price in rounds with any missing ask, else mean ask
                prices = [t["price"] for t in r["trades"]]
                vals = list(asks.values()) if len(asks) == len(sellers) or not prices else prices
            out.append(sum(vals) / len(vals) if vals else None)
        return out

    by_rule = {}
    for rule in ("exclude", "carry_forward", "trade_price"):
        s = series(rule)
        last20 = [x for x in s[-20:] if x is not None]
        all30 = [x for x in s if x is not None]
        by_rule[rule] = {"episode_mean_rounds_11_30": sum(last20) / len(last20),
                         "sd_round_means_rounds_11_30": sd(last20), "sd_round_means_rounds_1_30": sd(all30),
                         "round_means": [round(x, 4) if x is not None else None for x in s]}
    return {"replicate_id": rep.name, "model": setup["models"][sellers[0]]["model"],
            "seller_rounds_total": len(rounds) * len(sellers), "missing_seller_rounds": len(missing),
            "missing_by_kind": {k: sum(m["returned"] == k for m in missing) for k in sorted({m["returned"] for m in missing})},
            "missing_after_own_trade_previous_round": sum(m["traded_in_previous_round"] for m in missing),
            "missing_detail": missing, "by_rule": by_rule}


def main() -> None:
    out_path = Path(sys.argv[1])
    eps = [episode(rep) for run in sys.argv[2:] for rep in sorted(p for p in Path(run).iterdir() if p.is_dir())]
    across = {}
    for model in sorted({e["model"] for e in eps}):
        group = [e for e in eps if e["model"] == model]
        across[model] = {rule: {"n_episodes": len(group),
                                "episode_means": [round(e["by_rule"][rule]["episode_mean_rounds_11_30"], 4) for e in group],
                                "mean": statistics.mean(e["by_rule"][rule]["episode_mean_rounds_11_30"] for e in group),
                                "sd_across_episodes": sd([e["by_rule"][rule]["episode_mean_rounds_11_30"] for e in group])}
                         for rule in ("exclude", "carry_forward", "trade_price")}
    out_path.write_text(json.dumps({"episodes": eps, "across_episodes": across}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
