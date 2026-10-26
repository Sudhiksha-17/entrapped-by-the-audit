"""Study 1R checkpoint (human message 67): outcome-free health over all confirmatory campaign invocations so far and
the preregistered stop conditions (PREREG.md section 11). Read-only; no API calls. Uses scripts/study1r_health.py,
which never reads asks, bids, prices, trades, X, flags, probe answers or verbal content.

Stop conditions (any one -> STOP):
1. any arm's failure rate exceeds 10% of its completed episodes so far (failed / completed > 0.10);
2. any manipulation check (G2, including both probe answers for every seller) fails, or any probe is incomplete;
3. any provider or model id mismatch (routed provider other than OpenAI, returned model other than the arm's model,
   provider_unknown calls, provider_mismatch failure, dated snapshot changed during a run, run-level identity flag);
4. block cost more than 25% from block 0: each block's cost is compared with block 0's cost for the same arms
   (blocks 33-59 contain only mini-low Anchor and Offer); replacement episodes are excluded from block costs;
5. projected spend over the cap: spent in these campaigns + remaining episodes x per-arm mean cost so far + the
   planned judge runs (judge v2 $25.77, judge v1 $4.32) > cap.

Usage: python scripts/study1r_checkpoint.py [--campaign-yaml Y] [--planned-extra USD] <out.md> <out.json> <campaign.json> [...]
Defaults: the main campaign (configs/study1r/campaign.yaml) and its planned judge runs ($30.09). For the Study 1R-A
add-on (human message 71): --campaign-yaml configs/study1r_addon_A/campaign.yaml --planned-extra 0.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
PLANNED_JUDGES = 25.77 + 4.32


def health_for(campaign_json: Path) -> dict:
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "h.json"
        subprocess.run([sys.executable, "-I", str(REPO / "scripts" / "study1r_health.py"), str(campaign_json), str(out)],
                       check=True, capture_output=True, text=True)
        return json.loads(out.read_text(encoding="utf-8"))


def main() -> None:
    args, campaign_yaml, planned = sys.argv[1:], REPO / "configs" / "study1r" / "campaign.yaml", PLANNED_JUDGES
    while args and args[0].startswith("--"):
        flag, value, args = args[0], args[1], args[2:]
        if flag == "--campaign-yaml":
            campaign_yaml = REPO / value
        elif flag == "--planned-extra":
            planned = float(value)
        else:
            raise SystemExit(f"unknown flag {flag}")
    out_md, out_json, campaigns = Path(args[0]), Path(args[1]), [Path(p) for p in args[2:]]
    camp_cfg = yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))
    cap = float(camp_cfg["budget"]["cap_usd"])
    targets = {a["name"]: len(a.get("indices") or camp_cfg["indices"]) for a in camp_cfg["arms"]}
    models = {}
    for a in camp_cfg["arms"]:
        cfg = yaml.safe_load((REPO / a["config"]).read_text(encoding="utf-8"))
        models[a["name"]] = cfg["sellers"][0]["model"]
    per_arm = defaultdict(lambda: {"completed": 0, "failed": 0, "not_started": 0, "replacements": 0,
                                   "reasons": defaultdict(int), "parse_failures": 0, "cost": 0.0, "done_indices": set()})
    cost_by_block_arm: dict[int, dict[str, float]] = defaultdict(dict)
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
                    pa["done_indices"].add(e["replicate_index"])
                elif e["status"] == "failed":
                    pa["failed"] += 1
                    pa["reasons"][e["failure_reason"]] += 1
                else:
                    pa["not_started"] += 1
                pa["replacements"] += bool(e["replaces"])
                pa["parse_failures"] += e["parse_failures"] or 0
                pa["cost"] += e["cost_usd"]
                if not e["replaces"]:
                    cost_by_block_arm[e["replicate_index"]][arm] = e["cost_usd"]
                if e["status"] == "completed" and not e["g2_passed"]:
                    mc_failures.append(f"{arm} {e['replicate_id']}: G2 problems {e['g2_problems']}")
                if e["failure_reason"] in ("manipulation_check", "probe_missing"):
                    mc_failures.append(f"{arm} {e['replicate_id']}: failure_reason {e['failure_reason']}")
                if e["status"] == "completed" and (not e["probe"] or not e["probe"]["complete"]):
                    mc_failures.append(f"{arm} {e['replicate_id']}: probe incomplete")
                if (e.get("provider_unknown_calls") or 0) > 0:
                    identity_issues.append(f"{arm} {e['replicate_id']}: provider_unknown {e['provider_unknown_calls']}")
                if set(e["routed_providers"]) - {"OpenAI"}:
                    identity_issues.append(f"{arm} {e['replicate_id']}: routed {e['routed_providers']}")
                if set(e["returned_models"]) - {models[arm]}:
                    identity_issues.append(f"{arm} {e['replicate_id']}: returned {e['returned_models']}")
                if e["failure_reason"] == "provider_mismatch":
                    identity_issues.append(f"{arm} {e['replicate_id']}: provider_mismatch failure")
    failure_rate = {arm: (v["failed"] / v["completed"] if v["completed"] else (1.0 if v["failed"] else 0.0))
                    for arm, v in per_arm.items()}
    over = {a: r for a, r in failure_rate.items() if r > 0.10}
    block0 = cost_by_block_arm.get(0, {})
    block_cost, deviations = {}, {}
    for k, arms in sorted(cost_by_block_arm.items()):
        cost = sum(arms.values())
        ref = sum(block0.get(a, 0.0) for a in arms)
        block_cost[k] = {"cost": round(cost, 7), "block0_same_arms": round(ref, 7), "arms": len(arms)}
        if ref and abs(cost - ref) / ref > 0.25:
            deviations[k] = block_cost[k]
    spent = sum(v["cost"] for v in per_arm.values())
    remaining = 0.0
    for arm, n in targets.items():
        pa = per_arm.get(arm)
        done = len(pa["done_indices"]) if pa else 0
        mean = (pa["cost"] / (pa["completed"] + pa["failed"])) if pa and (pa["completed"] + pa["failed"]) else 0.0
        remaining += max(n - done, 0) * mean
    projected = spent + remaining + planned
    stop = bool(over or mc_failures or identity_issues or deviations or projected > cap)
    result = {"campaigns": [str(c) for c in campaigns], "blocks_done": sorted(cost_by_block_arm),
              "per_arm": {a: {**{k: v for k, v in d.items() if k not in ("reasons", "done_indices")},
                              "reasons": dict(d["reasons"]), "target": targets.get(a)} for a, d in sorted(per_arm.items())},
              "block_cost": {str(k): v for k, v in block_cost.items()}, "spent_usd": round(spent, 7),
              "projected_total_usd": round(projected, 4), "cap_usd": cap,
              "stop_conditions": {"failure_rate_over_10pct": over, "manipulation_check_failures": mc_failures,
                                  "provider_or_model_id_mismatch": identity_issues,
                                  "block_cost_deviation_over_25pct": {str(k): v for k, v in deviations.items()},
                                  "projected_spend_over_cap": projected > cap}, "stop": stop}
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    blocks = result["blocks_done"]
    lines = [f"# Study 1R checkpoint: blocks {blocks[0]}-{blocks[-1]} (outcome-free)", "",
             "Generated by `scripts/study1r_checkpoint.py` (human message 67). No asks, bids, prices, trades, X, flags, "
             "probe answers or verbal content were read.", "",
             f"- Campaign invocations: {', '.join('`' + c.parent.name + '`' for c in campaigns)}",
             f"- Blocks with episodes: {len(blocks)}; episodes: {sum(d['completed'] + d['failed'] for d in per_arm.values())}",
             f"- Spent (these campaigns): ${spent:.4f}; projected total incl. planned judges ${projected:.2f}; cap ${cap:.2f}",
             f"- **Stop: {'YES' if stop else 'no'}**", "",
             "| Arm | Target | Completed | Failed | Failure rate | Reasons | Replacements | Parse failures | Cost $ |",
             "|---|---|---|---|---|---|---|---|---|"]
    for a, d in sorted(per_arm.items()):
        lines.append(f"| {a} | {targets.get(a)} | {d['completed']} | {d['failed']} | {failure_rate[a]:.3f} | "
                     f"{dict(d['reasons']) or ''} | {d['replacements']} | {d['parse_failures']} | {d['cost']:.4f} |")
    lines += ["", "Stop conditions:", f"- Failure rate > 10%: {over or 'none'}",
              f"- Manipulation check failures (G2, probe): {mc_failures or 'none'}",
              f"- Provider or model id mismatch: {identity_issues or 'none'}",
              f"- Block cost deviation > 25% (vs block 0, same arms): {deviations or 'none'}",
              f"- Projected spend over cap: {projected > cap}", "",
              "Block costs (actual / block 0 same arms): " + ", ".join(
                  f"{k}: ${v['cost']:.4f} / ${v['block0_same_arms']:.4f}" for k, v in block_cost.items())]
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
