"""Automatic run documentation (Phase 2.5; CLAUDE.md standing rule 5).

Every run that goes through ``sting.minimal_runner`` or ``sting.model_check`` is
documented here, automatically, at the end of the run (also when episodes fail):

1. manifest   ``runs/<stage>/<run_id>/manifest.json``: everything needed to reproduce
              (git commit and code changes, upstream commit, package versions, hashes of
              config, prompt templates and lock file, models, key sources, output file hashes).
2. ledger     ``ledger/runs.csv`` (one machine-readable row per run) and a row in
              ``ledger/budget.md`` with estimate vs actual and the running total.
3. report     ``results/runs/<run_id>/report.md``: facts only, committed.
4. notebook   ``notes/LAB_NOTEBOOK.md``: one appended entry per run, with its purpose.
5. index      ``results/INDEX.md``: regenerated table of all runs.

``runs/`` is gitignored and append-only; the ledger, report, notebook and index are
committed. Nothing here interprets results.

Backfill for runs made before Phase 2.5:
    python -m sting.docs backfill runs/<stage>/<run_id> --purpose "..." [--no-budget-row]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from sting.paths import REPO_ROOT, RUNS_DIR, UPSTREAM_ROOT, ensure_upstream_on_path, upstream_commit

ensure_upstream_on_path()

LEDGER_FIELDS = ["run_id", "kind", "stage", "run_type", "started_utc", "finished_utc", "purpose", "models", "episodes",
                 "completed", "failed", "failures_by_reason", "parse_failures", "provider_unknown_calls", "calls", "tokens_in", "tokens_out",
                 "cost_seller_usd", "cost_buyer_usd", "estimated_cost_usd", "actual_cost_usd",
                 "cost_reported_for_all_calls", "git_commit", "code_dirty", "report"]
PACKAGES = ["openai", "anthropic", "pydantic", "numpy", "jinja2", "backoff", "PyYAML"]
CODE_PATHS = ["sting", "configs", "scripts", "tests"]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_state() -> dict[str, Any]:
    def git(*args: str) -> str:
        return subprocess.run(["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True,
                              encoding="utf-8", errors="replace").stdout  # I-050: not the Windows code page
    commit = git("rev-parse", "HEAD").strip() or "unknown"
    changed = [l for l in git("status", "--porcelain", "--", *CODE_PATHS).splitlines() if l.strip()]
    return {"commit": commit, "code_dirty": bool(changed), "code_changes": changed,
            "all_uncommitted": uncommitted_changes(),
            "diff": git("diff", "HEAD", "--", *CODE_PATHS) if changed else ""}


def uncommitted_changes() -> list[str]:
    """All uncommitted changes in the repo (tracked or untracked, not ignored), as porcelain lines."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "status", "--porcelain"], capture_output=True, text=True,
                         encoding="utf-8", errors="replace").stdout
    return [l for l in out.splitlines() if l.strip()]


def package_versions() -> dict[str, str]:
    out = {"python": sys.version.split()[0]}
    for name in PACKAGES:
        try:
            out[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            out[name] = "not installed"
    return out


def prompt_hashes() -> dict[str, str]:
    tdir = UPSTREAM_ROOT / "src" / "continuous_double_auction" / "prompt_templates"
    return {p.name: sha256_file(p) for p in sorted(tdir.glob("*.jinja2"))}


# Collecting facts from a run directory ---------------------------------------------------

def _rounds(auction_results: Path) -> list[dict[str, Any]]:
    if not auction_results.is_file():
        return []
    text = auction_results.read_text(encoding="utf-8")
    return [json.loads(b) for b in re.findall(r"````json\n(.*?)\n````", text, flags=re.S)]


def _calls(rep_dir: Path) -> list[dict[str, Any]]:
    path = rep_dir / "calls.jsonl"
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines()] if path.is_file() else []


def collect_episode_batch(run_dir: Path) -> dict[str, Any]:
    cfg_doc = json.loads((run_dir / "run_config.json").read_text(encoding="utf-8"))
    summary = json.loads((run_dir / "run_summary.json").read_text(encoding="utf-8"))
    cfg = cfg_doc["config"]
    reps = []
    for rep_dir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        status = json.loads((rep_dir / "status.json").read_text(encoding="utf-8"))
        setup = json.loads((rep_dir / "market_setup.json").read_text(encoding="utf-8"))
        reps.append({"dir": rep_dir, "status": status, "setup": setup, "calls": _calls(rep_dir),
                     "rounds": _rounds(rep_dir / "upstream_logs" / "auction_results.md")})
    calls = [c for r in reps for c in r["calls"]]
    by_role: dict[str, float] = {}
    for c in calls:
        by_role[c["role"]] = by_role.get(c["role"], 0.0) + (c["cost_usd_reported"] or 0.0)
    models = sorted({f"{s['provider']}:{s['model']}" + (f"@{s['openrouter_provider']}" if s.get("openrouter_provider")
                                                        else "") for s in cfg["sellers"] + cfg["buyers"]})
    return {
        "kind": "episode_batch", "run_id": cfg_doc["run_id"], "stage": cfg["stage"], "cfg_doc": cfg_doc,
        "run_type": cfg.get("run_type", "exploratory"),
        "cfg": cfg, "summary": summary, "reps": reps, "calls": calls, "models": models,
        "started_utc": cfg_doc.get("started_utc"), "finished_utc": summary.get("finished_utc"),
        "estimated_cost_usd": cfg_doc.get("estimated_cost_usd"),
        "cost_by_role": by_role,
    }


def collect_model_check(run_dir: Path) -> dict[str, Any]:
    doc = json.loads((run_dir / "model_check.json").read_text(encoding="utf-8"))
    rows = doc["results"]
    calls = [r for r in rows if r.get("status") != "skipped"]
    return {
        "kind": "model_check", "run_id": doc["run_id"], "stage": "model_check", "doc": doc, "rows": rows,
        "run_type": "exploratory",
        "calls": [{"tokens_in": r.get("tokens_in") or 0, "tokens_out": r.get("tokens_out") or 0,
                   "cost_usd_reported": r.get("cost_usd_reported"), "role": "check"} for r in calls],
        "models": sorted(f"{r['provider']}:{r['requested_model']}" for r in calls),
        "started_utc": None, "finished_utc": doc.get("finished_utc"), "estimated_cost_usd": 0.0,
        "cost_by_role": {},
    }


def collect_judge(run_dir: Path) -> dict[str, Any]:
    doc = json.loads((run_dir / "judge_run.json").read_text(encoding="utf-8"))
    summary = json.loads((run_dir / "judge_summary.json").read_text(encoding="utf-8"))
    calls = _calls(run_dir)
    labels = [json.loads(l) for l in (run_dir / "labels.jsonl").read_text(encoding="utf-8").splitlines()]
    spec = doc["model_spec"]
    return {
        "kind": "judge", "run_id": doc["run_id"], "stage": f"judge:{doc['source_stage']}", "doc": doc,
        "run_type": "exploratory", "summary": {"replicates": 0, "completed": "", "failed": "",
                                               "failures_by_reason": {}, "parse_failures_total": summary["invalid"]},
        "judge_summary": summary, "labels": labels, "calls": calls,
        "models": [f"{spec['provider']}:{spec['model']}" + (f"@{spec['openrouter_provider']}" if spec.get("openrouter_provider") else "")],
        "started_utc": None, "finished_utc": summary.get("finished_utc"),
        "estimated_cost_usd": doc.get("estimated_cost_usd"),
        "cost_by_role": {"judge": sum(c["cost_usd_reported"] or 0.0 for c in calls)},
    }


def collect(run_dir: Path) -> dict[str, Any]:
    if (run_dir / "model_check.json").is_file():
        return collect_model_check(run_dir)
    if (run_dir / "judge_run.json").is_file():
        return collect_judge(run_dir)
    return collect_episode_batch(run_dir)


# Writers ---------------------------------------------------------------------------------

def write_manifest(facts: dict[str, Any], run_dir: Path, purpose: str, command: str, git: dict[str, Any],
                   backfilled: bool) -> Path:
    files = {str(p.relative_to(run_dir)).replace("\\", "/"): sha256_file(p)
             for p in sorted(run_dir.rglob("*")) if p.is_file() and p.name not in ("manifest.json", "git_diff.patch")}
    config_files = {}
    if facts["kind"] == "episode_batch":
        cfg_bytes = json.dumps(facts["cfg"], sort_keys=True).encode()
        config_files["config_sha256"] = hashlib.sha256(cfg_bytes).hexdigest()
    manifest = {
        "run_id": facts["run_id"], "kind": facts["kind"], "stage": facts["stage"], "purpose": purpose,
        "command": command, "documented_utc": utc_now(), "backfilled": backfilled,
        "run_type": facts.get("run_type", "exploratory"),
        "git_commit_at_documentation": git["commit"], "code_dirty": git["code_dirty"],
        "code_changes": git["code_changes"], "all_uncommitted_at_documentation": git["all_uncommitted"],
        "upstream_commit": upstream_commit(), "packages": package_versions(), "prompt_templates_sha256": prompt_hashes(),
        "requirements_lock_sha256": sha256_file(REPO_ROOT / "notes" / "requirements_lock.txt"),
        "models": facts["models"], **config_files, "output_files_sha256": files,
    }
    if facts["kind"] == "episode_batch":
        manifest["key_sources"] = facts["cfg_doc"].get("key_sources")
        manifest["replicates"] = [{"replicate_id": r["status"]["replicate_id"],
                                   "replicate_index": r["status"]["replicate_index"],
                                   "status": r["status"]["status"],
                                   "failure_reason": r["status"].get("failure_reason")} for r in facts["reps"]]
    else:
        manifest["key_sources"] = facts["doc"].get("key_sources")
    path = run_dir / "manifest.json"
    with open(path, "x", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    if git["code_dirty"]:
        with open(run_dir / "git_diff.patch", "x", encoding="utf-8") as f:
            f.write(git["diff"])
    return path


def _ce_price(cfg: dict[str, Any]) -> Optional[float]:
    from src.continuous_double_auction.evaluation.metrics import competitive_equilibrium
    price, _ = competitive_equilibrium([float(v) for v in cfg["buyer_valuations"]],
                                       [float(c) for c in cfg["seller_valuations"]])
    return price


def _fmt(x: Optional[float], nd: int = 2) -> str:
    return "" if x is None else f"{x:.{nd}f}"


def write_report(facts: dict[str, Any], docs_root: Path, purpose: str, command: str) -> Path:
    out_dir = docs_root / "results" / "runs" / facts["run_id"]
    out_dir.mkdir(parents=True, exist_ok=False)
    tok_in = sum(c["tokens_in"] for c in facts["calls"])
    tok_out = sum(c["tokens_out"] for c in facts["calls"])
    actual = sum(c["cost_usd_reported"] or 0.0 for c in facts["calls"])
    lines = [f"# Run report: {facts['run_id']}", "",
             "Generated automatically by `sting/docs.py`. Facts only; no interpretation.", "",
             f"- Kind: {facts['kind']}; stage: {facts['stage']}; run type: {facts.get('run_type', 'exploratory')}",
             f"- Purpose: {purpose}", f"- Command: `{command}`",
             f"- Models: {', '.join(facts['models']) or 'none called'}",
             f"- Calls: {len(facts['calls'])}; tokens in {tok_in:,}; tokens out {tok_out:,}",
             f"- Cost: estimated ${_fmt(facts['estimated_cost_usd'], 4)}; actual ${actual:.7f} (OpenRouter-reported where available)",
             f"- Manifest: `results/runs/{facts['run_id']}/manifest.json` (committed copy of "
             f"`runs/{facts['stage']}/{facts['run_id']}/manifest.json`)", ""]
    if facts["kind"] == "judge":
        js = facts["judge_summary"]
        lines += [f"- Source run: `{js['source_run_id']}`; seller-rounds judged: {js['items']}; valid labels: {js['ok']}; "
                  f"invalid: {js['invalid']}", "", "| Label | Value counts (valid labels) |", "|---|---|"]
        ok = [l for l in facts["labels"] if l["status"] == "ok"]
        for key in ("engaged_with_message", "response", "awareness", "legal_or_ethical_concern", "own_coordination_intent"):
            if not any(key in l for l in ok):  # judge v2 (Study 1R) has no legal/coordination labels
                continue
            counts: dict[str, int] = {}
            for l in ok:
                counts[l[key]] = counts.get(l[key], 0) + 1
            lines.append(f"| {key} | " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + " |")
    elif facts["kind"] == "model_check":
        lines += ["| Provider | Requested model | Status | Returned model | Routed provider | Tokens in/out | Cost $ | Note |",
                  "|---|---|---|---|---|---|---|---|"]
        for r in facts["rows"]:
            note = r.get("reason") or (r.get("error") or "")[:80].replace("|", "/")
            lines.append(f"| {r['provider']} | {r['requested_model']} | {r['status']} | {r.get('returned_model') or ''} | "
                         f"{r.get('routed_provider') or ''} | {r.get('tokens_in') or 0}/{r.get('tokens_out') or 0} | "
                         f"{r.get('cost_usd_reported') or ''} | {note} |")
    else:
        cfg, summ = facts["cfg"], facts["summary"]
        ce = _ce_price(cfg)
        sting_cfg = cfg.get("sting")
        lines += [f"- Rounds: {cfg['rounds']}; seller messaging: {cfg.get('seller_comms_enabled')}; temperature: {cfg['temperature']}; "
                  f"boss_pressure: {bool(cfg.get('boss_pressure', False))}",
                  f"- Sting: " + (f"last seller id, condition {sting_cfg.get('condition', sting_cfg.get('mode', 'silent'))}, "
                                  f"mode {'silent' if sting_cfg.get('condition', 'silent') == 'silent' else 'message'}, rule {sting_cfg['pricing_rule']}, "
                                  f"initial_ask {sting_cfg.get('initial_ask')}, fixed_ask {sting_cfg.get('fixed_ask')}"
                                  if sting_cfg else "none"),
                  f"- Seller costs: {cfg['seller_valuations']}; buyer values: {cfg['buyer_valuations']}; "
                  f"competitive equilibrium price (upstream `metrics.competitive_equilibrium`): {_fmt(ce)}",
                  f"- Episodes: {summ['replicates']}; completed {summ['completed']}; failed {summ['failed']}; "
                  f"failures by reason: {summ.get('failures_by_reason') or {}}; parse failures: {summ.get('parse_failures_total', 0)}",
                  f"- Model identity (F-4): " + ("**FLAG** " + json.dumps({k: summ.get(k) for k in ("snapshot_changed_during_run", "returned_model_mismatches")})
                                                 if summ.get("model_identity_flag") else "no snapshot change, no returned-model mismatch"),
                  f"- Provider unknown (OpenRouter response without provider field; fallbacks disabled): "
                  f"{summ.get('provider_unknown_calls_total', 0)} calls"
                  + (" **FLAG**" if summ.get("provider_unknown_calls_total") else ""),
                  f"- Cost by role: " + ", ".join(f"{k} ${v:.7f}" for k, v in sorted(facts["cost_by_role"].items())), "",
                  "## Episodes", "",
                  "| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in facts["reps"]:
            st, calls = r["status"], r["calls"]
            routed = sorted({str(c.get("routed_provider")) for c in calls if not c.get("error")})
            lines.append(f"| {st['replicate_id']} | {st['replicate_index']} | {st['status']} | {st.get('failure_reason') or ''} | "
                         f"{st['rounds_completed']}/{st['rounds_planned']} | {st['wall_clock_s']} | {len(calls)} | "
                         f"{st.get('parse_failures', 0)} | {st.get('provider_unknown_calls', 0)} | {', '.join(routed)} | {sum(c['cost_usd_reported'] or 0 for c in calls):.7f} |")
        blind = cfg.get("run_type") == "confirmatory"
        if blind:  # human message 24: outcomes stay unexamined until all Stage 2 blocks are complete
            lines += ["", "## Per round", "", "Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not "
                      "written to reports until all Stage 2 blocks are complete (human message 24)."]
        for r in ([] if blind else facts["reps"]):
            lines += ["", f"## Per round: {r['status']['replicate_id']}", "",
                      "| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |",
                      "|---|---|---|---|---|---|---|"]
            for rd in r["rounds"]:
                asks = [v for v in rd["seller_asks"].values() if isinstance(v, (int, float))]
                bids = [v for v in rd["buyer_bids"].values() if isinstance(v, (int, float))]
                prices = [t["price"] for t in rd["trades"]]
                lines.append(f"| {rd['round_number']} | {_fmt(sum(asks) / len(asks) if asks else None)} | "
                             f"{', '.join(f'{k[-1]} {v}' for k, v in sorted(rd['seller_asks'].items()))} | "
                             f"{_fmt(sum(bids) / len(bids) if bids else None)} | {len(prices)} | "
                             f"{_fmt(sum(prices) / len(prices) if prices else None)} | {len(rd['seller_messages'])} |")
    path = out_dir / "report.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def ledger_row(facts: dict[str, Any], purpose: str, git: dict[str, Any], report: Path, docs_root: Path) -> dict[str, Any]:
    calls = facts["calls"]
    summ = facts.get("summary", {})
    eps = summ.get("replicates", 0)
    return {
        "run_id": facts["run_id"], "kind": facts["kind"], "stage": facts["stage"],
        "run_type": facts.get("run_type", "exploratory"),
        "started_utc": facts.get("started_utc") or "", "finished_utc": facts.get("finished_utc") or "",
        "purpose": purpose, "models": ";".join(facts["models"]), "episodes": eps,
        "completed": summ.get("completed", ""), "failed": summ.get("failed", ""),
        "failures_by_reason": json.dumps(summ.get("failures_by_reason", {})),
        "parse_failures": summ.get("parse_failures_total", ""),
        "provider_unknown_calls": summ.get("provider_unknown_calls_total", ""), "calls": len(calls),
        "tokens_in": sum(c["tokens_in"] for c in calls), "tokens_out": sum(c["tokens_out"] for c in calls),
        "cost_seller_usd": round(facts["cost_by_role"].get("seller", 0.0), 7),
        "cost_buyer_usd": round(facts["cost_by_role"].get("buyer", 0.0), 7),
        "estimated_cost_usd": facts["estimated_cost_usd"],
        "actual_cost_usd": round(sum(c["cost_usd_reported"] or 0.0 for c in calls), 7),
        "cost_reported_for_all_calls": all(c["cost_usd_reported"] is not None for c in calls
                                           if c["tokens_in"] or c["tokens_out"]),
        "git_commit": git["commit"], "code_dirty": git["code_dirty"],
        "report": str(report.relative_to(docs_root)).replace("\\", "/"),
    }


class LedgerSchemaMismatch(RuntimeError):
    """ledger/runs.csv has a different header from LEDGER_FIELDS (ISSUES I-027)."""


def append_ledger(row: dict[str, Any], docs_root: Path) -> float:
    path = docs_root / "ledger" / "runs.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.is_file()
    if not new:
        with open(path, encoding="utf-8", newline="") as f:
            header = next(csv.reader(f), [])
        if header != LEDGER_FIELDS:
            raise LedgerSchemaMismatch(f"{path} header {header} differs from {LEDGER_FIELDS}; "
                                       f"run 'python -m sting.docs rebuild-ledger' first")
    with open(path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LEDGER_FIELDS)
        if new:
            writer.writeheader()
        writer.writerow(row)
    with open(path, encoding="utf-8", newline="") as f:
        return sum(float(r["actual_cost_usd"] or 0) for r in csv.DictReader(f))


def append_budget_row(row: dict[str, Any], running_total: float, docs_root: Path) -> None:
    path = docs_root / "ledger" / "budget.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text("# Budget ledger\n\n| # | UTC timestamp | Run / batch | Models | Calls | Tokens in | Tokens out | "
                        "Estimated $ | Actual $ | Running total $ | Notes |\n|---|---|---|---|---|---|---|---|---|---|---|\n",
                        encoding="utf-8")
    numbers = [int(m) for m in re.findall(r"^\| (\d+) \|", path.read_text(encoding="utf-8"), flags=re.M)]
    n = max(numbers) + 1 if numbers else 1
    note = (f"auto (sting/docs.py). episodes {row['episodes']}, completed {row['completed']}, failed {row['failed']}; "
            f"sellers ${row['cost_seller_usd']}, buyers ${row['cost_buyer_usd']}")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"| {n} | {row['finished_utc'] or utc_now()} | {row['kind']} `{row['run_id']}` | {row['models']} | "
                f"{row['calls']} | {row['tokens_in']} | {row['tokens_out']} | {row['estimated_cost_usd']} | "
                f"{row['actual_cost_usd']} | {running_total:.7f} | {note} |\n")


def append_notebook(row: dict[str, Any], command: str, backfilled: bool, docs_root: Path) -> None:
    path = docs_root / "notes" / "LAB_NOTEBOOK.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text("# Lab notebook\n\nOne entry per run, appended automatically by `sting/docs.py`. "
                        "Facts only. Append-only.\n", encoding="utf-8")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n---\n\n## {utc_now()} | {row['kind']} | {row['run_id']}{' (backfilled)' if backfilled else ''}\n\n"
                f"- Purpose: {row['purpose']}\n- Command: `{command}`\n- Models: {row['models']}\n"
                f"- Episodes: {row['episodes']} (completed {row['completed']}, failed {row['failed']}, "
                f"failures by reason {row['failures_by_reason']}, parse failures {row['parse_failures']})\n"
                f"- Calls {row['calls']}; tokens in {row['tokens_in']}; tokens out {row['tokens_out']}\n"
                f"- Cost: estimated ${row['estimated_cost_usd']}; actual ${row['actual_cost_usd']}\n"
                f"- Code: commit `{row['git_commit'][:7]}`, uncommitted code changes: {row['code_dirty']}\n"
                f"- Report: `{row['report']}`\n")


def publish_manifest(run_dir: Path, docs_root: Path, run_id: str) -> None:
    """Copy the manifest (and git_diff.patch, if any) into the committed results/runs/<run_id>/."""
    out_dir = docs_root / "results" / "runs" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in ("manifest.json", "git_diff.patch"):
        src = run_dir / name
        if src.is_file():
            with open(out_dir / name, "xb") as f:
                f.write(src.read_bytes())


def write_index(docs_root: Path) -> None:
    with open(docs_root / "ledger" / "runs.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    lines = ["# Run index", "", "Regenerated automatically by `sting/docs.py` from `ledger/runs.csv`. Do not edit.", "",
             f"Runs: {len(rows)}. Total actual cost: ${sum(float(r['actual_cost_usd'] or 0) for r in rows):.7f}.", "",
             "| Finished (UTC) | Run | Kind | Stage | Models | Episodes (ok/failed) | Calls | Actual $ | Purpose | Report |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['finished_utc']} | `{r['run_id']}` | {r['kind']} | {r['stage']} | {r['models']} | "
                     f"{r['episodes']} ({r['completed']}/{r['failed']}) | {r['calls']} | {r['actual_cost_usd']} | "
                     f"{r['purpose']} | [report]({r['report'].replace('results/', '', 1)}) |")
    (docs_root / "results").mkdir(exist_ok=True)
    (docs_root / "results" / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def record_run(run_dir: Path, purpose: str, command: str, docs_root: Path = REPO_ROOT,
               backfilled: bool = False, budget_row: bool = True) -> dict[str, Any]:
    """Document one finished run. Returns the ledger row."""
    if not purpose or not purpose.strip():
        raise ValueError("every documented run needs a purpose")
    facts = collect(run_dir)
    git = git_state()
    write_manifest(facts, run_dir, purpose, command, git, backfilled)
    report = write_report(facts, docs_root, purpose, command)
    publish_manifest(run_dir, docs_root, facts["run_id"])
    row = ledger_row(facts, purpose, git, report, docs_root)
    total = append_ledger(row, docs_root)
    if budget_row:
        append_budget_row(row, total, docs_root)
    append_notebook(row, command, backfilled, docs_root)
    write_index(docs_root)
    return row


def rebuild_ledger(runs_dir: Path = RUNS_DIR, docs_root: Path = REPO_ROOT) -> Path:
    """Regenerate ledger/runs.csv from every documented run directory (manifest present).

    The existing file is kept, unchanged, as ledger/runs_superseded_<UTC>.csv. Rows come from the
    run directories and manifests only (purpose, git commit and dirty flag as recorded at
    documentation time). Then the index is regenerated.
    """
    path = docs_root / "ledger" / "runs.csv"
    kept = None
    if path.is_file():
        kept = path.with_name(f"runs_superseded_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.csv")
        path.rename(kept)
    rows = []
    for manifest_path in sorted(Path(runs_dir).glob("*/*/manifest.json")):
        run_dir = manifest_path.parent
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        facts = collect(run_dir)
        git = {"commit": manifest["git_commit_at_documentation"], "code_dirty": manifest["code_dirty"]}
        report = docs_root / "results" / "runs" / facts["run_id"] / "report.md"
        rows.append(ledger_row(facts, manifest["purpose"], git, report, docs_root))
    rows.sort(key=lambda r: r["finished_utc"])
    with open(path, "x", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LEDGER_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    write_index(docs_root)
    return kept


def docs_root_for(runs_dir: Path) -> Path:
    """Real runs document into the repo; runs in any other directory (tests) document beside it."""
    return REPO_ROOT if Path(runs_dir).resolve() == RUNS_DIR.resolve() else Path(runs_dir) / "_docs"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run documentation tools.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("backfill", help="Document a run made before Phase 2.5.")
    b.add_argument("run_dir", type=Path)
    b.add_argument("--purpose", required=True)
    b.add_argument("--command", default="(not recorded; run predates Phase 2.5)")
    b.add_argument("--no-budget-row", action="store_true", help="The run already has a manual budget.md row.")
    pm = sub.add_parser("publish-manifest", help="Copy an existing run's manifest into results/runs/<run_id>/.")
    pm.add_argument("run_dir", type=Path)
    sub.add_parser("rebuild-ledger", help="Regenerate ledger/runs.csv from run directories (keeps the old file).")
    args = parser.parse_args(argv)
    if args.cmd == "rebuild-ledger":
        kept = rebuild_ledger()
        print(f"ledger rebuilt; previous file kept as {kept}")
        return
    if args.cmd == "publish-manifest":
        run_id = json.loads((args.run_dir / "manifest.json").read_text(encoding="utf-8"))["run_id"]
        publish_manifest(args.run_dir, REPO_ROOT, run_id)
        print(f"published manifest for {run_id}")
        return
    row = record_run(args.run_dir, args.purpose, args.command, backfilled=True, budget_row=not args.no_budget_row)
    print(json.dumps(row, indent=2))


if __name__ == "__main__":
    main()
