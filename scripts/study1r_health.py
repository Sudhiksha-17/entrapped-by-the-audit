"""Study 1R health report (human message 66). Read-only; no API calls. Outcome-free by design.

Per arm and episode: status, failure reason, rounds completed, parse failures, provider_unknown calls, call errors and
retries, the G2 manipulation check (passed and problem list; pricing conformity is part of G2), sting messages sent
(count), probe completeness (both answers recorded for both sellers) and parseability (parsed or unparseable count,
never the YES/NO values), routed providers, returned model names, dated snapshots at start and end, model identity
flag, frozen-lock commit, tokens, cost vs estimate, wall clock, ERROR/Traceback lines in upstream logs. It never
reads or prints asks, bids, prices, trades, X, pre, flags, probe answers or verbal content. (scripts/stage2_health.py
assumes Study 1's sting log and floor rule and is not used for Study 1R.)

Usage: python scripts/study1r_health.py <campaign.json> <out.json>
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path


def episode(rep: Path, per_ep_est: float) -> dict:
    st = json.loads((rep / "status.json").read_text(encoding="utf-8"))
    calls = [json.loads(l) for l in (rep / "calls.jsonl").read_text(encoding="utf-8").splitlines()]
    log_path = rep / "upstream_logs" / "unified.log"
    log_errors = sum(1 for l in log_path.read_text(encoding="utf-8").splitlines()
                     if "ERROR" in l or "Traceback" in l) if log_path.is_file() else None
    mc = st.get("manipulation_check") or {}
    probe_path = rep / "probe.json"
    probe = None
    if probe_path.is_file():
        p = json.loads(probe_path.read_text(encoding="utf-8"))
        probe = {"complete": p["complete"],
                 "q2_parsed": sum(r["q2_parsed"] in ("YES", "NO") for r in p["sellers"].values()),
                 "q2_unparseable": sum(r["q2_parsed"] == "unparseable" for r in p["sellers"].values()),
                 "errors": sum(1 for r in p["sellers"].values() if r["error"])}
    probe_calls = [c for c in calls if c.get("role") == "probe"]
    return {
        "replicate_id": rep.name, "replicate_index": st.get("replicate_index"), "replaces": st.get("replaces"),
        "status": st["status"], "failure_reason": st.get("failure_reason"),
        "rounds_completed": st["rounds_completed"], "parse_failures": st.get("parse_failures"),
        "provider_unknown_calls": st.get("provider_unknown_calls"), "calls": len(calls),
        "errors": sum(1 for c in calls if c["error"]), "retried_calls": sum(1 for c in calls if c["attempts"] > 1),
        "g2_passed": mc.get("passed"), "g2_problems": mc.get("problems"),
        "g2_pricing_mismatch_rounds": len(mc.get("pricing_mismatch_rounds") or []),
        "sting_messages_sent": (st.get("sting") or {}).get("messages_sent"),
        "probe": probe, "probe_calls": len(probe_calls),
        "routed_providers": dict(collections.Counter(str(c["routed_provider"]) for c in calls if not c["error"])),
        "returned_models": dict(collections.Counter(str(c["returned_model"]) for c in calls if not c["error"])),
        "tokens_in": sum(c["tokens_in"] for c in calls), "tokens_out": sum(c["tokens_out"] for c in calls),
        "cost_usd": round(sum(c["cost_usd_reported"] or 0 for c in calls), 7), "estimated_cost_usd": per_ep_est,
        "wall_clock_s": st.get("wall_clock_s"), "upstream_log_error_lines": log_errors,
    }


def main() -> None:
    campaign = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = {"campaign_id": campaign["campaign_id"], "arms": {}}
    for arm, info in campaign["arms"].items():
        run_dir = Path(info["run_dir"])
        cfg_doc = json.loads((run_dir / "run_config.json").read_text(encoding="utf-8"))
        summary = json.loads((run_dir / "run_summary.json").read_text(encoding="utf-8"))
        per_ep_est = float(cfg_doc["config"]["estimated_cost_per_episode_usd"])
        out["arms"][arm] = {
            "run_id": cfg_doc["run_id"], "run_type": cfg_doc["config"]["run_type"],
            "frozen_prereg_commit": (cfg_doc.get("frozen_prereg") or {}).get("git_commit"),
            "frozen_lock_sha256": (cfg_doc.get("frozen_prereg") or {}).get("sha256_of_lock"),
            "snapshots_start": cfg_doc.get("model_snapshots_at_start"),
            "snapshots_end": summary.get("model_snapshots_at_end"),
            "model_identity_flag": summary.get("model_identity_flag"),
            "failures_by_reason": summary.get("failures_by_reason"),
            "episodes": [episode(rep, per_ep_est) for rep in sorted(p for p in run_dir.iterdir() if p.is_dir())],
        }
    Path(sys.argv[2]).parent.mkdir(parents=True, exist_ok=True)
    Path(sys.argv[2]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    for arm, a in out["arms"].items():
        for e in a["episodes"]:
            print(f"{arm:<16} {e['status']:<9} {str(e['failure_reason']):<14} rounds {e['rounds_completed']:>2} "
                  f"parse {e['parse_failures']} punk {e['provider_unknown_calls']} calls {e['calls']} err {e['errors']} "
                  f"retry {e['retried_calls']} g2 {e['g2_passed']} problems {len(e['g2_problems'] or [])} "
                  f"sent {e['sting_messages_sent']} probe {e['probe']} routed {e['routed_providers']} "
                  f"returned {e['returned_models']} cost {e['cost_usd']} est {e['estimated_cost_usd']} "
                  f"wall {e['wall_clock_s']} logerr {e['upstream_log_error_lines']}")
        print(f"   snapshots start {a['snapshots_start']} end {a['snapshots_end']} identity_flag "
              f"{a['model_identity_flag']} frozen {a['frozen_prereg_commit']}")


if __name__ == "__main__":
    main()
