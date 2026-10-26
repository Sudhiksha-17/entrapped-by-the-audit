"""Stage 2 checkpoint (human message 25): outcome-free health over all confirmatory campaign invocations so far,
and the stop conditions. Read-only; no API calls. Never reads asks, bids, prices, trades or flags.

Stop conditions (any one -> STOP):
1. any arm's failure rate exceeds 10% of its completed episodes so far (failed / completed > 0.10);
2. any manipulation check fails;
3. any provider or model id mismatch (returned model != requested, routed provider failure, provider_unknown,
   dated snapshot changed during a run, or run-level model identity flag);
4. cost of any block deviates more than 25% from block 0's cost ($7.2628536);
5. projected total spend (spent in the budget group + remaining blocks x mean block cost so far) exceeds the cap.

Usage: python scripts/stage2_checkpoint.py <out.md> <out.json> <campaign.json> [<campaign.json> ...]
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BLOCK0_COST = 7.2628536
TOTAL_BLOCKS = 33


def health_for(campaign_json: Path) -> dict:
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "h.json"
        subprocess.run([sys.executable, "-I", str(REPO / "scripts" / "stage2_health.py"), str(campaign_json), str(out)],
                       check=True, capture_output=True, text=True)
        return json.loads(out.read_text(encoding="utf-8"))


def main() -> None:
    out_md, out_json, campaigns = Path(sys.argv[1]), Path(sys.argv[2]), [Path(p) for p in sys.argv[3:]]
    import yaml
    camp_cfg = yaml.safe_load((REPO / "configs" / "stage2" / "campaign.yaml").read_text(encoding="utf-8"))
    cap = float(camp_cfg["budget"]["cap_usd"])
    per_arm = defaultdict(lambda: {"completed": 0, "failed": 0, "not_started": 0, "reasons": defaultdict(int),
                                   "parse_failures": 0, "cost": 0.0})
    block_cost = defaultdict(float)
    block_episodes = defaultdict(int)
    mc_failures, identity_issues = [], []
    for c in campaigns:
        h = health_for(c)
        for arm, a in h["arms"].items():
            if a.get("model_identity_flag"):
                identity_issues.append(f"{arm}: run-level model identity flag ({a['run_id']})")
            for m, snap in (a.get("snapshots_start") or {}).items():
                end = (a.get("snapshots_end") or {}).get(m, {})
                if snap.get("canonical_slug") != end.get("canonical_slug"):
                    identity_issues.append(f"{arm}: snapshot changed {snap.get('canonical_slug')} -> {end.get('canonical_slug')}")
            for e in a["episodes"]:
                pa = per_arm[arm]
                if e["status"] == "completed":
                    pa["completed"] += 1
                elif e["status"] == "failed":
                    pa["failed"] += 1
                    pa["reasons"][e["failure_reason"]] += 1
                else:
                    pa["not_started"] += 1
                pa["parse_failures"] += e["parse_failures"] or 0
                pa["cost"] += e["cost_usd"]
                k = int(e["replicate_id"].split("_r")[-1][:3])
                block_cost[k] += e["cost_usd"]
                block_episodes[k] += 1
                mc = e.get("manipulation_check")
                if mc is not None and not mc.get("passed"):
                    mc_failures.append(f"{arm} {e['replicate_id']}: missing in {mc.get('missing')}")
                if e["failure_reason"] == "manipulation_check":
                    mc_failures.append(f"{arm} {e['replicate_id']}: failure_reason manipulation_check")
                if (e.get("provider_unknown_calls") or 0) > 0:
                    identity_issues.append(f"{arm} {e['replicate_id']}: provider_unknown {e['provider_unknown_calls']}")
                if set(e["routed_providers"]) - {"OpenAI"}:
                    identity_issues.append(f"{arm} {e['replicate_id']}: routed {e['routed_providers']}")
                expected = "openai/gpt-4.1-mini" if arm.startswith("mini-low") else "openai/gpt-4.1"
                if set(e["returned_models"]) - {expected}:
                    identity_issues.append(f"{arm} {e['replicate_id']}: returned {e['returned_models']}")
                if e["failure_reason"] == "provider_mismatch":
                    identity_issues.append(f"{arm} {e['replicate_id']}: provider_mismatch failure")
    failure_flags = {arm: (v["failed"] / v["completed"] if v["completed"] else (1.0 if v["failed"] else 0.0))
                     for arm, v in per_arm.items()}
    over = {a: r for a, r in failure_flags.items() if r > 0.10}
    deviations = {k: c for k, c in block_cost.items() if abs(c - BLOCK0_COST) / BLOCK0_COST > 0.25}
    blocks_done = sorted(block_cost)
    mean_block = sum(block_cost.values()) / len(block_cost) if block_cost else 0.0
    spent = sum(v["cost"] for v in per_arm.values())
    projected = spent + (TOTAL_BLOCKS - len(blocks_done)) * mean_block
    stops = {
        "failure_rate_over_10pct": over, "manipulation_check_failures": mc_failures,
        "provider_or_model_id_mismatch": identity_issues, "block_cost_deviation_over_25pct": deviations,
        "projected_spend_over_cap": projected > cap,
    }
    stop = bool(over or mc_failures or identity_issues or deviations or projected > cap)
    result = {"campaigns": [str(c) for c in campaigns], "blocks_done": blocks_done, "per_arm": {
        a: {**{k: v for k, v in d.items() if k != "reasons"}, "reasons": dict(d["reasons"])} for a, d in sorted(per_arm.items())},
        "block_cost": {str(k): round(v, 7) for k, v in sorted(block_cost.items())},
        "block_episodes": {str(k): n for k, n in sorted(block_episodes.items())},
        "spent_usd": round(spent, 7), "mean_block_cost_usd": round(mean_block, 7), "projected_total_usd": round(projected, 4),
        "cap_usd": cap, "stop_conditions": stops, "stop": stop}
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    lines = [f"# Stage 2 checkpoint: blocks {blocks_done[0]}-{blocks_done[-1]} (outcome-free)", "",
             "Generated by `scripts/stage2_checkpoint.py` (human message 25). No asks, bids, prices, trades or flags were read.",
             "", f"- Campaign invocations: {', '.join('`' + c.parent.name + '`' for c in campaigns)}",
             f"- Blocks completed: {len(blocks_done)} ({blocks_done[0]} to {blocks_done[-1]}); episodes: {sum(block_episodes.values())}",
             f"- Spent (these campaigns): ${spent:.4f}; mean block cost ${mean_block:.4f} (block 0: ${BLOCK0_COST:.4f}); "
             f"projected total for 33 blocks ${projected:.2f}; cap ${cap:.2f}",
             f"- **Stop: {'YES' if stop else 'no'}**", "", "| Arm | Completed | Failed | Failure rate | Reasons | Parse failures | Cost $ |",
             "|---|---|---|---|---|---|---|"]
    for a, d in sorted(per_arm.items()):
        lines.append(f"| {a} | {d['completed']} | {d['failed']} | {failure_flags[a]:.3f} | {dict(d['reasons']) or ''} | "
                     f"{d['parse_failures']} | {d['cost']:.4f} |")
    lines += ["", "Stop conditions:", f"- Failure rate > 10%: {over or 'none'}",
              f"- Manipulation check failures: {mc_failures or 'none'}",
              f"- Provider or model id mismatch: {identity_issues or 'none'}",
              f"- Block cost deviation > 25%: {deviations or 'none'}",
              f"- Projected spend over cap: {projected > cap}", "",
              "Block costs: " + ", ".join(f"{k}: ${v:.4f}" for k, v in sorted(block_cost.items()))]
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
