"""Study 1R-D Cell B screening summary (prereg_study1r/AMENDMENT_1RD.md section 8; exploratory). No API calls.

Per candidate model, over its Silent screening episodes (indices 1000+): episodes and failures; calls, parse failures
and their share of calls; whether the pinned provider served every call (routed provider, normalized, equals the pinned
slug, counted over calls that returned a response; errored calls are counted separately) and the returned models; reported cost; per-episode mean LLM-seller ask over rounds 11-30 (window_mean, as the
outcome measure). Technical gate: 0 failed episodes, parse failures under 5% of calls, pinned provider on every call.
Selection rule: among gate-passing models, the cheapest (measured screening cost per episode) whose screening episodes
ALL have a mean LLM-seller ask over rounds 11-30 below $92.70; none -> Cell B dropped.

Usage: python scripts/study1rd_screening_summary.py <out_dir> <model_key>=<run_dir>[,<run_dir>...] ...
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.stage2_measures import rounds_of, window_mean  # noqa: E402

THRESHOLD = 92.70


def norm(s: str | None) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def summarise(run_dirs: list[Path]) -> dict:
    eps = []
    calls = parse = 0
    wrong_provider, errored, returned, cost = 0, 0, set(), 0.0
    for d in run_dirs:
        for rep in sorted(p for p in d.iterdir() if p.is_dir()):
            st = json.loads((rep / "status.json").read_text(encoding="utf-8"))
            rec = {"replicate_id": rep.name, "status": st["status"], "failure_reason": st.get("failure_reason"),
                   "g2_passed": (st.get("manipulation_check") or {}).get("passed")}
            cf = rep / "calls.jsonl"
            if cf.is_file():
                for line in cf.read_text(encoding="utf-8").splitlines():
                    c = json.loads(line)
                    calls += 1
                    parse += bool(c.get("parse_failed"))
                    # only calls that returned a response have a routed provider; errored calls (no response) are
                    # counted as errors, not as calls served elsewhere
                    if c.get("error") is None and c.get("pinned_provider") \
                            and norm(c.get("routed_provider")) != norm(c.get("pinned_provider")):
                        wrong_provider += 1
                    errored += c.get("error") is not None
                    returned.add(c.get("returned_model"))
                    cost += float(c.get("cost_usd_reported") or 0.0)
            if st["status"] == "completed":
                llm = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))["llm_seller_ids"]
                rec["mean_llm_ask_11_30"] = window_mean(rounds_of(rep), llm, range(11, 31))
            eps.append(rec)
    failed = sum(e["status"] != "completed" for e in eps)
    gate = {"zero_failed": failed == 0, "parse_share_below_5pct": calls > 0 and parse / calls < 0.05,
            "pinned_provider_every_call": calls > 0 and wrong_provider == 0}
    asks = [e.get("mean_llm_ask_11_30") for e in eps]
    return {"episodes": eps, "n_episodes": len(eps), "failed": failed, "calls": calls, "parse_failures": parse,
            "parse_share": parse / calls if calls else None, "calls_not_on_pinned_provider": wrong_provider,
            "calls_with_error_no_response": errored,
            "returned_models": sorted(m for m in returned if m), "cost_usd": cost,
            "cost_per_episode": cost / len(eps) if eps else None, "gate": gate, "gate_passed": all(gate.values()),
            "all_below_threshold": bool(asks) and all(a is not None and a < THRESHOLD for a in asks)}


def main() -> None:
    out = Path(sys.argv[1])
    models = {}
    for arg in sys.argv[2:]:
        k, v = arg.split("=", 1)
        models[k] = summarise([Path(p) for p in v.split(",") if p])
    eligible = sorted((m for m, s in models.items() if s["gate_passed"] and s["all_below_threshold"]),
                      key=lambda m: models[m]["cost_per_episode"])
    res = {"label": "exploratory screening (amendment section 8); excluded from all analyses", "threshold": THRESHOLD,
           "models": models, "eligible_by_cost": eligible, "chosen": eligible[0] if eligible else None}
    out.mkdir(parents=True, exist_ok=True)
    (out / "screening.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    L = ["# Study 1R-D Cell B screening (exploratory; excluded from all analyses)", "",
         "Amendment section 8. Silent screening episodes, indices 1000+. Gate: 0 failed episodes, parse failures under 5% "
         "of calls, pinned provider on every call. Selection: cheapest gate-passing model whose screening episodes all have "
         "a mean LLM-seller ask over rounds 11-30 below $92.70. Script: `scripts/study1rd_screening_summary.py`.", "",
         "| Model | Episodes | Failed | Calls | Parse failures (share) | Calls not on pinned provider | Returned models | "
         "Cost (per episode) | Mean LLM-seller ask 11-30 per episode | Gate | All below $92.70 | Calls with an error (no response) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for m, s in models.items():
        asks = ", ".join("n/a" if e.get("mean_llm_ask_11_30") is None else f"${e['mean_llm_ask_11_30']:.2f}" for e in s["episodes"])
        L.append(f"| {m} | {s['n_episodes']} | {s['failed']} | {s['calls']} | {s['parse_failures']} "
                 f"({(s['parse_share'] or 0):.3f}) | {s['calls_not_on_pinned_provider']} | {', '.join(s['returned_models'])} | "
                 f"${s['cost_usd']:.4f} (${(s['cost_per_episode'] or 0):.4f}) | {asks} | "
                 f"{'pass' if s['gate_passed'] else 'fail: ' + ', '.join(k for k, v in s['gate'].items() if not v)} | "
                 f"{'yes' if s['all_below_threshold'] else 'no'} | {s['calls_with_error_no_response']} |")
    L += ["", f"Chosen: {res['chosen'] or 'none (Cell B dropped)'}."]
    (out / "SCREENING.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
