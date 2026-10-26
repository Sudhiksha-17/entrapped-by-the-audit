"""Stage 2 campaign runner: interleaved blocks, failed-episode replacement, budget cap, frozen-prereg check
(prereg/stage2_spec.md section 10).

A campaign YAML lists the arms (one arm config each, as for sting.minimal_runner) and the replicate indices.
Execution:
1. Checks: every arm config is valid, has the campaign's run_type and budget group; for confirmatory campaigns
   the repository must be clean (D-040) and the prereg frozen with matching hashes (sting.freeze_prereg.verify).
2. Cost: total estimate printed; the $2 approval rule and the budget cap apply to the whole campaign.
3. One run directory per arm (documented per arm at the end, like any batch).
4. Blocks: for each replicate index k (in order), one episode of every arm, in a per-block order shuffled with
   random.Random(f"{order_seed}-{k}"); the next block starts after the current one finishes. Episodes within a
   block run concurrently up to `concurrency`.
5. Replacement passes: failed episodes are replaced with new replicate ids (same index, market draw and
   paraphrase; `replaces` recorded), again in blocks by index, for at most `max_replacement_passes` passes (3 in the
   Stage 2 campaign; human message 21) or until every arm has `n_per_arm` completed episodes. Arms still short after
   the last pass are reported with their shortfall and failure reasons, not replaced further.
6. A campaign log (`runs/<stage>/_campaigns/<campaign_id>/campaign.json`) records the arm runs, the block
   order, every episode's status and replacements.

Usage:
    python -m sting.stage2_runner configs/stage2_campaign.yaml --purpose "..." [--estimate-only] [--approve-cost]
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Optional

import yaml

from sting.freeze_prereg import verify as verify_frozen
from sting.minimal_runner import (COST_APPROVAL_THRESHOLD_USD, BudgetGuard, check_run_type, close_run, open_run,
                                  run_episode, spent_in_budget_group, upstream_cwd, utc_stamp, validate_config,
                                  write_json)
from sting.paths import REPO_ROOT, RUNS_DIR


def load_campaign(path: Path, root: Path = REPO_ROOT) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    campaign = yaml.safe_load((root / path).read_text(encoding="utf-8"))
    arms = []
    for a in campaign["arms"]:
        cfg = yaml.safe_load((root / a["config"]).read_text(encoding="utf-8"))
        arms.append({"name": a["name"], "cell": a["cell"], "arm": a["arm"], "config_path": a["config"], "cfg": cfg,
                     "indices": a.get("indices")})
    return campaign, arms


def check_campaign(campaign: dict[str, Any], arms: list[dict[str, Any]]) -> None:
    names = [a["name"] for a in arms]
    if len(set(names)) != len(names):
        raise ValueError("arm names must be unique")
    for a in arms:
        validate_config(a["cfg"])
        if a["cfg"]["run_type"] != campaign["run_type"]:
            raise ValueError(f"arm {a['name']}: run_type {a['cfg']['run_type']} != campaign {campaign['run_type']}")
        if campaign.get("budget") and a["cfg"].get("budget") != campaign["budget"]:
            raise ValueError(f"arm {a['name']}: budget must equal the campaign budget")


def block_order(arm_names: list[str], seed: Any, k: int) -> list[str]:
    order = list(arm_names)
    random.Random(f"{seed}-{k}").shuffle(order)
    return order


def a_has_own(arms: list[dict[str, Any]], name: str) -> bool:
    return any(a["name"] == name and a.get("indices") for a in arms)


def run_campaign(campaign_path: Path, purpose: str, runs_dir: Path = RUNS_DIR, approve_cost: bool = False,
                 estimate_only: bool = False, root: Path = REPO_ROOT, command: str = "run_campaign()",
                 frozen_check=verify_frozen, only_indices: Optional[list[int]] = None,
                 skip_replacement: bool = False, only_arms: Optional[list[str]] = None) -> dict[str, Any]:
    """`only_indices` runs a subset of the campaign's blocks (e.g. block 0 only, human message 24); each invocation
    creates its own arm run directories under one campaign id. `skip_replacement` defers replacement passes (they
    run after all blocks, in a later invocation). With either option, shortfalls are computed against the episodes
    attempted in this invocation.

    Study 1R (spec version 2, sections 6 and 13): an arm entry may list its own `indices` (default: the campaign's);
    block k then contains every arm whose indices include k, so mini-low anchor and offer continue alone, interleaved
    with each other, after the other arms end. Each arm's target N is the number of its indices. `only_arms` restricts
    an invocation to some arms (e.g. the pilot's single first episode). A campaign with `gate_report: study1r_pilot`
    writes the automatic pilot gate report (sting.study1r_gates) over all its invocations after each one."""
    campaign, arms = load_campaign(campaign_path, root)
    check_campaign(campaign, arms)
    if only_arms is not None:
        unknown = sorted(set(only_arms) - {a["name"] for a in arms})
        if unknown:
            raise ValueError(f"arms {unknown} are not in the campaign")
        arms = [a for a in arms if a["name"] in only_arms]
    arm_idx = {a["name"]: list(a.get("indices") or campaign["indices"]) for a in arms}
    if only_indices is not None:
        known = set().union(*arm_idx.values())
        unknown = [k for k in only_indices if k not in known]
        if unknown:
            raise ValueError(f"indices {unknown} are not in the campaign")
        arm_idx = {n: [k for k in v if k in only_indices] for n, v in arm_idx.items()}
    indices = sorted(set().union(*arm_idx.values()))
    n_target = {n: (len(v) if (only_indices is not None or only_arms is not None or a_has_own(arms, n))
                    else int(campaign["n_per_arm"])) for n, v in arm_idx.items()}
    n_episodes = sum(len(v) for v in arm_idx.values())
    estimate = sum(float(a["cfg"]["estimated_cost_per_episode_usd"]) * len(arm_idx[a["name"]]) for a in arms)
    print(f"Campaign {campaign['name']}: {len(arms)} arms, {len(indices)} indices, {n_episodes} episodes; "
          f"estimated cost ${estimate:.2f}")
    if estimate_only:
        return {"estimate_only": True, "estimated_cost_usd": estimate, "episodes": n_episodes,
                "episodes_per_arm": {n: len(v) for n, v in arm_idx.items()}}
    lock = None
    if campaign["run_type"] == "confirmatory":
        check_run_type({"run_type": "confirmatory"})
        lock = frozen_check(campaign_path)
    guard = None
    if campaign.get("budget"):
        spent = spent_in_budget_group(campaign["budget"]["group"], runs_dir)
        cap = float(campaign["budget"]["cap_usd"])
        print(f"Budget group {campaign['budget']['group']!r}: spent ${spent:.4f} of cap ${cap:.2f}")
        if spent + estimate > cap:
            raise SystemExit(f"Budget cap refused: spent ${spent:.4f} + estimate ${estimate:.4f} > cap ${cap:.2f}")
        guard = BudgetGuard(campaign["budget"]["group"], cap, 0.0, runs_dir)
    if estimate > COST_APPROVAL_THRESHOLD_USD and not approve_cost:
        raise SystemExit(f"Estimate exceeds ${COST_APPROVAL_THRESHOLD_USD:.2f}; human approval required.")

    campaign_id = f"{utc_stamp()}_{campaign['name']}_{uuid.uuid4().hex[:6]}"
    extra = {"campaign_id": campaign_id, "frozen_prereg": lock}
    runs = {}
    for a in arms:
        cfg = dict(a["cfg"], cell=a["cell"], arm=a["arm"])
        run_id, run_dir, mirror_root = open_run(cfg, runs_dir,
                                                float(cfg["estimated_cost_per_episode_usd"]) * len(arm_idx[a["name"]]),
                                                arm_idx[a["name"]], extra)
        runs[a["name"]] = {"cfg": cfg, "run_id": run_id, "run_dir": run_dir, "statuses": [], "repl_count": 0}
    log: dict[str, Any] = {"campaign_id": campaign_id, "campaign": str(campaign_path), "started_utc": utc_stamp(),
                           "only_indices": only_indices, "skip_replacement": skip_replacement, "only_arms": only_arms,
                           "arms": {n: {"run_id": r["run_id"], "run_dir": str(r["run_dir"])} for n, r in runs.items()},
                           "blocks": [], "replacement_passes": []}
    seed = campaign.get("order_seed", campaign["name"])

    def run_block(tasks: list[tuple[str, int, str, Optional[str]]]) -> list[dict[str, Any]]:
        with ThreadPoolExecutor(max_workers=int(campaign.get("concurrency", 1))) as pool:
            futures = [(name, pool.submit(run_episode, runs[name]["cfg"], runs[name]["run_dir"], k, rid, replaces, guard))
                       for name, k, rid, replaces in tasks]
            results = []
            for name, fut in futures:
                status = fut.result()
                runs[name]["statuses"].append(status)
                results.append({"arm": name, "replicate_id": status["replicate_id"], "status": status["status"],
                                "failure_reason": status.get("failure_reason"), "replaces": status.get("replaces")})
            return results

    mirror_root = None
    with upstream_cwd(ensure_mirror_root()):
        for k in indices:
            order = block_order([a["name"] for a in arms if k in arm_idx[a["name"]]], seed, k)
            tasks = [(name, k, f"{runs[name]['run_id']}_r{k:03d}", None) for name in order]
            log["blocks"].append({"index": k, "order": order, "episodes": run_block(tasks)})
        for p in range(0 if skip_replacement else int(campaign.get("max_replacement_passes", 3))):
            pending = []
            for name, r in runs.items():
                done = sum(s["status"] == "completed" for s in r["statuses"])
                replaced = {s.get("replaces") for s in r["statuses"] if s.get("replaces")}
                failed = [s for s in r["statuses"] if s["status"] == "failed" and s["replicate_id"] not in replaced]
                for s in failed[:max(0, n_target[name] - done)]:
                    r["repl_count"] += 1
                    pending.append((name, s["replicate_index"],
                                    f"{r['run_id']}_r{s['replicate_index']:03d}_repl{r['repl_count']}", s["replicate_id"]))
            if not pending:
                break
            by_index: dict[int, list] = {}
            for t in pending:
                by_index.setdefault(t[1], []).append(t)
            pass_log = []
            for k in sorted(by_index):
                order = block_order([t[0] for t in by_index[k]], f"{seed}-repl{p}", k)
                tasks = sorted(by_index[k], key=lambda t: order.index(t[0]))
                pass_log.append({"index": k, "episodes": run_block(tasks)})
            log["replacement_passes"].append(pass_log)

    summaries = {}
    for name, r in runs.items():
        summaries[name] = close_run(r["cfg"], r["run_dir"], r["run_id"], r["statuses"], purpose, command, runs_dir)
    log["finished_utc"] = utc_stamp()
    log["completed_per_arm"] = {n: sum(s["status"] == "completed" for s in r["statuses"]) for n, r in runs.items()}
    log["shortfall_per_arm"] = {n: max(0, n_target[n] - c) for n, c in log["completed_per_arm"].items()}
    log["failure_reasons_per_arm"] = {
        n: {reason: sum(s.get("failure_reason") == reason for s in r["statuses"] if s["status"] != "completed")
            for reason in sorted({s.get("failure_reason") for s in r["statuses"] if s["status"] != "completed"})}
        for n, r in runs.items()}
    log["replacement_passes_used"] = len(log["replacement_passes"])
    out_dir = runs_dir / campaign["stage"] / "_campaigns" / campaign_id
    out_dir.mkdir(parents=True, exist_ok=False)
    write_json(out_dir / "campaign.json", log)
    gate = None
    if campaign.get("gate_report") == "study1r_pilot":
        from sting.study1r_gates import pilot_campaign_logs, pilot_report
        gate_dir = root / "results" / "study1r" / "pilot_gate" if runs_dir == RUNS_DIR else runs_dir / "_gate"
        gate = pilot_report(pilot_campaign_logs(runs_dir, campaign["stage"]), gate_dir)
    return {"campaign_id": campaign_id, "completed_per_arm": log["completed_per_arm"],
            "shortfall_per_arm": log["shortfall_per_arm"], "failure_reasons_per_arm": log["failure_reasons_per_arm"],
            "replacement_passes_used": log["replacement_passes_used"], "log": str(out_dir / "campaign.json"),
            "arm_summaries": summaries, "gate_report": gate}


def ensure_mirror_root():
    from sting.prompt_mirror import ensure_mirror
    return ensure_mirror()[0]


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Stage 2 interleaved campaign runner.")
    parser.add_argument("campaign", type=Path)
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--estimate-only", action="store_true")
    parser.add_argument("--approve-cost", action="store_true")
    parser.add_argument("--indices", type=lambda s: [int(x) for x in s.split(",")], default=None,
                        help="Run only these blocks (replicate indices), e.g. 0.")
    parser.add_argument("--arms", type=lambda s: s.split(","), default=None,
                        help="Run only these arms (comma-separated names), e.g. the pilot's first episode.")
    parser.add_argument("--skip-replacement", action="store_true",
                        help="Defer replacement passes to a later invocation (after all blocks).")
    args = parser.parse_args(argv)
    out = run_campaign(args.campaign, args.purpose, approve_cost=args.approve_cost, estimate_only=args.estimate_only,
                       only_indices=args.indices, skip_replacement=args.skip_replacement, only_arms=args.arms,
                       command="python -m sting.stage2_runner " + " ".join(sys.argv[1:]))
    print(json.dumps({k: v for k, v in out.items() if k != "arm_summaries"}, indent=2))


if __name__ == "__main__":
    main()
