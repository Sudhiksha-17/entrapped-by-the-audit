"""Exploratory plan C, cheap talk (notes/EXPLORATORY_PLAN_B_C.md section C, committed 1e32de1; D-126 approved).
EXPLORATORY, post hoc, descriptive only (no tests). No API calls; no frozen file changed.

4.1-high Offer episodes with human-confirmed acceptance (`acc_inclusive`, frozen `build` on completed episodes via the
D-116 staging). Accepter = the LLM seller with a confirmed acceptance (Labeler A, verification message, accept or
conditional_accept); if both sellers have one, the seller with the earlier first confirmed round (tie: Seller A), and
the episode is flagged. Partner = the other LLM seller. Window = rounds r to 30, r = the accepter's first confirmed
round (first_rounds of scripts/study1r_plan_b_sheet.py).

Per episode, accepter and partner: mean posted ask over the window (rounds where the seller posted a numeric ask);
trades with that seller as seller in the window; profit = sum over those trades of (price - 80.00); and the share of
window rounds (both posted) in which the partner's ask was below the accepter's. Means over episodes with 95%
percentile bootstrap CIs over episodes (10,000 resamples, seed 20261025). Split: accepter "raised toward X" = its mean
ask over rounds r to 30 above its own mean ask over rounds r-3 to r-1.

Usage: python scripts/study1r_plan_c.py <out_dir> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS.parent))
from sting.stage2_measures import rounds_of  # noqa: E402

CELL = "4.1-high"
SEED = 20261025
SELLER_COST = 80.00
MEASURES = ("mean_ask", "trades", "profit")


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _ask(rnd: dict, s: str):
    a = rnd["seller_asks"].get(s)
    return a if isinstance(a, (int, float)) and not isinstance(a, bool) else None


def mean_ask(rounds: list[dict], s: str, window: range):
    asks = [a for r in rounds if r["round_number"] in window for a in [_ask(r, s)] if a is not None]
    return sum(asks) / len(asks) if asks else None


def pick_accepter(first: dict[str, int]) -> tuple[str, bool]:
    """first: seller -> first confirmed round. Earlier round wins; tie by seller id (Seller A first)."""
    s = min(first, key=lambda k: (first[k], k))
    return s, len(first) > 1


def episode_measures(rounds: list[dict], llm: list[str], accepter: str, r: int) -> dict:
    partner = next(s for s in llm if s != accepter)
    win = range(r, 31)
    out = {"accepter_id": accepter, "partner_id": partner, "first_confirmed_round": r, "window": [r, 30]}
    for role, s in (("accepter", accepter), ("partner", partner)):
        trades = [t for rd in rounds if rd["round_number"] in win for t in rd["trades"] if t["seller_id"] == s]
        out[role] = {"mean_ask": mean_ask(rounds, s, win), "trades": len(trades),
                     "profit": round(sum(t["price"] - SELLER_COST for t in trades), 6)}
    both = [(_ask(rd, accepter), _ask(rd, partner)) for rd in rounds if rd["round_number"] in win]
    both = [(a, p) for a, p in both if a is not None and p is not None]
    out["rounds_both_posted"] = len(both)
    out["share_partner_below"] = sum(p < a for a, p in both) / len(both) if both else None
    before = mean_ask(rounds, accepter, range(max(1, r - 3), r))
    out["accepter_ask_before"] = before
    out["raised_toward_x"] = None if before is None or out["accepter"]["mean_ask"] is None \
        else out["accepter"]["mean_ask"] > before
    return out


def boot(values: list[float], rng: np.random.Generator) -> dict:
    v = np.array([x for x in values if x is not None], dtype=float)
    if v.size == 0:
        return {"n": 0, "mean": None, "ci": [None, None]}
    b = v[rng.integers(0, v.size, size=(10_000, v.size))].mean(axis=1)
    return {"n": int(v.size), "mean": float(v.mean()),
            "ci": [float(np.quantile(b, 0.025)), float(np.quantile(b, 0.975))]}


def summarise(eps: list[dict], rng: np.random.Generator) -> dict:
    out = {"n": len(eps)}
    for m in MEASURES:
        out[m] = {"accepter": boot([e["accepter"][m] for e in eps], rng),
                  "partner": boot([e["partner"][m] for e in eps], rng),
                  "accepter_minus_partner": boot([None if e["accepter"][m] is None or e["partner"][m] is None
                                                  else e["accepter"][m] - e["partner"][m] for e in eps], rng)}
    out["share_partner_below"] = boot([e["share_partner_below"] for e in eps], rng)
    return out


def analyse(eps: list[dict]) -> dict:
    rng = np.random.default_rng(SEED)
    return {"label": "exploratory, post hoc, descriptive (no tests)", "cell": CELL, "all": summarise(eps, rng),
            "raised": summarise([e for e in eps if e["raised_toward_x"] is True], rng),
            "not_raised": summarise([e for e in eps if e["raised_toward_x"] is False], rng),
            "raised_undefined": sum(e["raised_toward_x"] is None for e in eps),
            "both_sellers_accepted": sum(e["both_accepted"] for e in eps), "per_episode": eps}


def collect(cy: Path, logs: list[Path], sheet: Path, key: Path) -> tuple[list[dict], list[str]]:
    wrap = load("study1r_results_completed.py", "wrap_pc")
    res = load("study1r_results.py", "res_pc")
    pb = load("study1r_plan_b_sheet.py", "pb_pc")
    human, strata, protected = res.verify_labels(sheet, key)
    eps = []
    with tempfile.TemporaryDirectory(prefix="s1r_pc_") as tmp:
        staged, excluded = wrap.stage(logs, Path(tmp))
        built = res.build([cy], staged, human, strata, {}, {}, False, protected)
        dirs = {p.name: p for log in staged for info in json.loads(log.read_text(encoding="utf-8"))["arms"].values()
                for p in Path(info["run_dir"]).iterdir() if p.is_dir()}
        for e in built:
            if e["arm"] != "offer" or e["cell"] != CELL:
                continue
            first = pb.first_rounds(e["replicate_id"], human, strata)
            if bool(first) != bool(e["acc_inclusive"]):
                raise SystemExit(f"acceptance mismatch in {e['replicate_id']}")
            if not first:
                continue
            rep = dirs[e["replicate_id"]]
            llm = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))["llm_seller_ids"]
            acc, both = pick_accepter(first)
            m = episode_measures(rounds_of(rep), llm, acc, first[acc])
            eps.append({"replicate_id": e["replicate_id"], "both_accepted": both,
                        "first_confirmed_rounds": first, **m})
    return sorted(eps, key=lambda e: e["replicate_id"]), [x["replicate_id"] for x in excluded]


def f(s: dict, money: bool = False, dp: int = 2, signed: bool = True) -> str:
    if s["mean"] is None:
        return "n/a"
    p, sg = ("$", "") if money else ("", "+" if signed else "")
    return f"{p}{s['mean']:{sg}.{dp}f} ({p}{s['ci'][0]:{sg}.{dp}f}, {p}{s['ci'][1]:{sg}.{dp}f})"


def table(name: str, s: dict) -> list[str]:
    if s["n"] == 0:
        return [f"### {name} (N = 0)", "", "No episodes.", ""]
    L = [f"### {name} (N = {s['n']} episodes)", "",
         "| Measure | Accepter | Partner | Accepter minus partner |", "|---|---|---|---|"]
    for m, lab, money in (("mean_ask", "Mean posted ask, rounds r-30", True), ("trades", "Trades as seller", False),
                          ("profit", "Profit, sum of (price - $80.00)", True)):
        d = s[m]
        L.append(f"| {lab} | {f(d['accepter'], money, signed=False)} | {f(d['partner'], money, signed=False)} | "
                 f"{f(d['accepter_minus_partner'])} |")
    L += [f"| Share of rounds with partner ask below accepter ask | | | {f(s['share_partner_below'], dp=3)} |", ""]
    return L


def report(res: dict, excluded: list[str]) -> str:
    L = ["# Plan C: cheap talk, 4.1-high Offer (EXPLORATORY, post hoc, descriptive)", "",
         "Plan: `notes/EXPLORATORY_PLAN_B_C.md` section C (committed `1e32de1`; D-126). No tests. Completed episodes "
         f"(D-116 staging; excluded: {', '.join(excluded) or 'none'}). Acceptance: Labeler A verify coding. Window: "
         "rounds r to 30, r = the accepter's first confirmed acceptance round (may be later than its first acceptance "
         "because of the stopping rule). CIs: 95% percentile bootstrap over episodes (10,000 resamples, seed 20261025). "
         "Script: `scripts/study1r_plan_c.py`. Facts only.", "",
         f"Episodes: {res['all']['n']}; both sellers with a confirmed acceptance (accepter = earlier first confirmed "
         f"round, tie Seller A): {res['both_sellers_accepted']}. Raised toward X (accepter mean ask r-30 above its mean "
         f"r-3 to r-1): {res['raised']['n']}; not raised: {res['not_raised']['n']}; undefined (no ask before r): "
         f"{res['raised_undefined']}.", ""]
    L += table("All accepting episodes", res["all"]) + table("Accepter raised toward X", res["raised"]) \
        + table("Accepter did not raise", res["not_raised"])
    L += ["## Per episode", "",
          "| Episode | Accepter | r | Both accepted | Accepter ask | Partner ask | Accepter trades | Partner trades | "
          "Accepter profit | Partner profit | Share partner below | Accepter ask r-3 to r-1 | Raised |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for e in res["per_episode"]:
        a, p = e["accepter"], e["partner"]
        mo = lambda v: "n/a" if v is None else f"${v:.2f}"
        sh = "n/a" if e["share_partner_below"] is None else f"{e['share_partner_below']:.3f} ({e['rounds_both_posted']} rounds)"
        L.append(f"| {e['replicate_id'][-4:]} | {e['accepter_id']} | {e['first_confirmed_round']} | "
                 f"{'yes' if e['both_accepted'] else 'no'} | {mo(a['mean_ask'])} | {mo(p['mean_ask'])} | {a['trades']} | "
                 f"{p['trades']} | {mo(a['profit'])} | {mo(p['profit'])} | {sh} | {mo(e['accepter_ask_before'])} | "
                 f"{'n/a' if e['raised_toward_x'] is None else ('yes' if e['raised_toward_x'] else 'no')} |")
    return "\n".join(L) + "\n"


def main() -> None:
    out_dir, cy = Path(sys.argv[1]), Path(sys.argv[2])
    logs = [Path(p) for p in sys.argv[3].split(",") if p]
    eps, excluded = collect(cy, logs, Path(sys.argv[4]), Path(sys.argv[5]))
    res = analyse(eps)
    res["excluded_episodes"] = excluded
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "plan_c.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    text = report(res, excluded)
    (out_dir / "PLAN_C.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
