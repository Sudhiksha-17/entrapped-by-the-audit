"""Random-round reference with n = 9 episodes per resample (human message 81; exploratory fix to NUMBERS_FOR_PAPER.md
section 6.5 / 7.3). No API calls; no frozen file changed.

Same per-episode values as scripts/study1r_posthoc_m78.py item 5 (after minus before around a pseudo round r: mean
LLM-seller ask over rounds r+1 to min(r+3, 30) minus over rounds r-3 to r-1, round r excluded). Each of 10,000
resamples (numpy generator, seed 20261025): draw 9 episodes with replacement from the group (matching the accepters'
N = 9), draw one round per drawn episode independently and uniformly from 17-29, take the mean of the 9 values.
Groups: 4.1-high Offer without confirmed acceptance (21 episodes) and 4.1-high Silent (33). Reported: mean, 2.5th and
97.5th percentiles of the resample means, and the share of resamples at or above the accepters' +0.393.

Usage: python scripts/study1r_reference_n9.py <out.json> <campaign.yaml> <campaign.json>[,...] <verify_sheet>
       <verify_key> <judge_v2_dir>[,...]
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS.parent))
from sting import study1r_analysis as A  # noqa: E402

SEED, R, N = 20261025, 10_000, 9


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def reference(table: np.ndarray, rng: np.random.Generator, accepters: float, n: int = N) -> dict:
    """table: episodes x rounds 17-29 of after-minus-before values."""
    ei = rng.integers(0, table.shape[0], size=(R, n))
    ri = rng.integers(0, table.shape[1], size=(R, n))
    m = table[ei, ri].mean(axis=1)
    return {"episodes_in_group": int(table.shape[0]), "episodes_per_resample": n, "resamples": R,
            "mean": float(m.mean()), "interval_95": [float(np.quantile(m, .025)), float(np.quantile(m, .975))],
            "share_at_or_above_accepters": float((m >= accepters).mean())}


def main() -> None:
    a = sys.argv[1:]
    m78 = load("study1r_posthoc_m78.py", "m78_n9")
    pba = load("study1r_price_by_acceptance.py", "pba_n9")
    episodes, extra, human, strata, excluded = m78.collect(Path(a[1]), [Path(p) for p in a[2].split(",") if p],
                                                           Path(a[3]), Path(a[4]), [p for p in a[5].split(",") if p])
    o = A.eps(episodes, "offer", "4.1-high")
    acc = []
    for e in o:
        if e["acc_inclusive"]:
            r0 = pba.first_acceptance(e["replicate_id"], human, strata)["first_confirmed_round"]
            v = m78.before_after(extra[e["replicate_id"]]["asks"], r0)
            if v is not None:
                acc.append(v)
    acc_mean = float(np.mean(acc))
    rng = np.random.default_rng(SEED)
    out = {"label": "exploratory, post hoc (human message 81)", "excluded_episodes": excluded,
           "accepters": {"n": len(acc), "mean_after_minus_before": acc_mean}}
    for g, es in (("offer_not_accepting", [e for e in o if not e["acc_inclusive"]]),
                  ("silent", A.eps(episodes, "silent", "4.1-high"))):
        table = np.array([[m78.before_after(extra[e["replicate_id"]]["asks"], r) for r in range(17, 30)] for e in es],
                         dtype=float)
        if np.isnan(table).any():
            raise SystemExit(f"{g}: missing before/after values")
        out[g] = reference(table, rng, acc_mean)
    Path(a[0]).parent.mkdir(parents=True, exist_ok=True)
    Path(a[0]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
