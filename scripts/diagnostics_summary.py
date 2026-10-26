"""Diagnostics summary for steps A and B (human message 14). Read-only over run logs; no API calls.

Episode outcome (D-048): for each round, the mean of the LLM sellers' posted asks (sting excluded;
rounds with no LLM-seller ask dropped); the episode outcome is the mean of those round means over
rounds 11-30. The pooled mean of all LLM-seller asks in rounds 11-30 (used in earlier pilot
reports) and the mean LLM-seller trade price over rounds 11-30 are also given.

Groups are defined by (stage, run_name) from each run's config; episodes are listed with their
replicate index so test-retest pairs (same index) can be identified.

Usage: python scripts/diagnostics_summary.py <out.json> <run_dir> [<run_dir> ...]
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path


def rounds_of(rep: Path) -> list[dict]:
    text = (rep / "upstream_logs" / "auction_results.md").read_text(encoding="utf-8")
    return [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````", text, flags=re.S)]


def episode(rep: Path, run_name: str, last: int = 20) -> dict:
    status = json.loads((rep / "status.json").read_text(encoding="utf-8"))
    setup = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))
    llm = set(setup.get("llm_seller_ids") or setup["seller_ids"])
    rounds = rounds_of(rep)
    window = rounds[-last:]
    round_means = []
    pooled, prices, missing = [], [], 0
    for r in window:
        asks = [a for s, a in r["seller_asks"].items() if s in llm and isinstance(a, (int, float))]
        missing += len(llm) - len(asks)
        if asks:
            round_means.append(sum(asks) / len(asks))
        pooled += asks
        prices += [t["price"] for t in r["trades"] if t["seller_id"] in llm]
    return {
        "run_name": run_name, "replicate_id": rep.name, "replicate_index": setup["replicate_index"],
        "n_llm_sellers": len(llm), "sting": setup.get("sting_id") is not None,
        "model": setup["models"][sorted(llm)[0]]["model"], "boss_pressure": bool(setup.get("boss_pressure")),
        "status": status["status"], "rounds_completed": status["rounds_completed"],
        "parse_failures": status.get("parse_failures", 0),
        "outcome_round_mean_ask": statistics.mean(round_means) if round_means else None,
        "pooled_mean_ask": statistics.mean(pooled) if pooled else None,
        "mean_trade_price": statistics.mean(prices) if prices else None,
        "missing_llm_asks_in_window": missing,
        "initial_asks": setup["initial_asks"],
        "cost_usd": round(sum(v["cost_usd_reported"] for v in status["usage_by_role"].values()), 7),
    }


def sd(xs):
    return statistics.stdev(xs) if len(xs) > 1 else None


def group_stats(eps: list[dict]) -> dict:
    ys = [e["outcome_round_mean_ask"] for e in eps if e["status"] == "completed"]
    out = {"n": len(ys), "episode_outcomes": [round(y, 4) for y in ys],
           "mean": statistics.mean(ys) if ys else None, "sd": sd(ys),
           "mean_trade_price": statistics.mean([e["mean_trade_price"] for e in eps
                                                if e["status"] == "completed" and e["mean_trade_price"] is not None]),
           "failed_episodes": [e["replicate_id"] for e in eps if e["status"] != "completed"]}
    by_index: dict[int, list[float]] = {}
    for e in eps:
        if e["status"] == "completed":
            by_index.setdefault(e["replicate_index"], []).append(e["outcome_round_mean_ask"])
    repeated = {k: v for k, v in by_index.items() if len(v) > 1}
    if repeated:
        # One-way ANOVA decomposition over indices with repeats (balanced in step A: 2 indices x 2 episodes).
        within_ss = sum((y - statistics.mean(v)) ** 2 for v in repeated.values() for y in v)
        within_df = sum(len(v) - 1 for v in repeated.values())
        ms_within = within_ss / within_df
        means = [statistics.mean(v) for v in repeated.values()]
        n_per = statistics.mean(len(v) for v in repeated.values())
        ms_between = n_per * statistics.variance(means) if len(means) > 1 else None
        var_index = max(0.0, (ms_between - ms_within) / n_per) if ms_between is not None else None
        out["test_retest"] = {
            "episodes_by_index": {str(k): [round(y, 4) for y in v] for k, v in sorted(repeated.items())},
            "within_index_variance": ms_within, "within_index_sd": ms_within ** 0.5,
            "between_index_mean_square": ms_between,
            "between_index_variance_component": var_index,
            "share_of_variance_from_index": (var_index / (var_index + ms_within)
                                             if var_index is not None and (var_index + ms_within) > 0 else None),
            "note": "2 indices x 2 episodes: the variance components have 1 and 2 degrees of freedom and are very imprecise.",
        }
    return out


def main() -> None:
    out_path = Path(sys.argv[1])
    eps = []
    for run in sys.argv[2:]:
        cfg = json.loads((Path(run) / "run_config.json").read_text(encoding="utf-8"))["config"]
        name = cfg["run_name"]
        eps += [episode(rep, name) for rep in sorted(p for p in Path(run).iterdir() if p.is_dir())]
    groups = {}
    for e in eps:
        groups.setdefault(e["run_name"], []).append(e)
    result = {"definition": __doc__.split("Usage")[0].strip(), "episodes": eps,
              "groups": {k: group_stats(v) for k, v in sorted(groups.items())}}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    for k, g in result["groups"].items():
        print(k, "n", g["n"], "outcomes", g["episode_outcomes"], "mean", g["mean"] and round(g["mean"], 3),
              "sd", g["sd"] and round(g["sd"], 3), "trade", round(g["mean_trade_price"], 3))
        if "test_retest" in g:
            t = g["test_retest"]
            print("   test-retest", t["episodes_by_index"], "within SD %.3f" % t["within_index_sd"],
                  "between-index var comp", t["between_index_variance_component"] and round(t["between_index_variance_component"], 3),
                  "share from index", t["share_of_variance_from_index"] and round(t["share_of_variance_from_index"], 3))


if __name__ == "__main__":
    main()
