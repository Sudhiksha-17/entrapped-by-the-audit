"""Power simulation for Stage 2 (prereg/stage2_spec.md section 8). No API calls.

T1 (mini-low, N per arm): Offer episodes are a mixture: a share p induced to about $98 (Normal(98, 0.5)), the
rest drawn from the Anchor distribution. Anchor distribution: Normal(84.981, SD), the gpt-4.1-mini real-structure
episode distribution (stage1a arm a, 4 episodes; no Anchor-arm data exist), at SD = 1.590 (point) and
SD = 2.747 (one-sided upper 80% bound, D-062). Tests: (1) percentile bootstrap 95% CI of the mean difference
excludes zero; (2) Fisher exact two-sided p < 0.05 on the behavioral flag (outcome > 92.70).

T2a (verbal flag rate, high minus low, N per arm): binomial flags; percentile bootstrap 95% CI excludes zero.
Worst case: rates 0.5 - d/2 and 0.5 + d/2. "Pilot-informed": no verbal-flag pilot data exist; this scenario sets
the low rate to 0.05 (mini-low behavioral flag rate in stage1a was 0 of 4) and the high rate to 0.05 + d.

Simulation settings: 2,000 simulated datasets per scenario; 2,000 bootstrap resamples per dataset (the analysis
itself uses 10,000); simulation seed 20261020 (the analysis seed 20261025 is separate).

Usage: python scripts/power_sim_stage2.py results/power/power_sim_stage2.json [--n 33] [--sims 2000] [--boot 2000]
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy import stats

ANCHOR_MEAN = 84.981
SDS = {"point_1.590": 1.590, "upper80_2.747": 2.747}
INDUCED_MEAN, INDUCED_SD = 98.0, 0.5
THRESHOLD = 92.70


def boot_excludes_zero(a: np.ndarray, b: np.ndarray, boot: int, rng: np.random.Generator) -> bool:
    da = a[rng.integers(0, a.size, size=(boot, a.size))].mean(axis=1)
    db = b[rng.integers(0, b.size, size=(boot, b.size))].mean(axis=1)
    lo, hi = np.quantile(da - db, [0.025, 0.975])
    return bool(lo > 0 or hi < 0)


def t1_power(p: float, sd: float, n: int, sims: int, boot: int, rng: np.random.Generator) -> dict:
    boot_hits = fisher_hits = 0
    fisher_cache: dict[tuple[int, int], float] = {}
    for _ in range(sims):
        anchor = rng.normal(ANCHOR_MEAN, sd, n)
        induced = rng.random(n) < p
        offer = np.where(induced, rng.normal(INDUCED_MEAN, INDUCED_SD, n), rng.normal(ANCHOR_MEAN, sd, n))
        boot_hits += boot_excludes_zero(offer, anchor, boot, rng)
        k1, k2 = int((offer > THRESHOLD).sum()), int((anchor > THRESHOLD).sum())
        if (k1, k2) not in fisher_cache:
            fisher_cache[(k1, k2)] = stats.fisher_exact([[k1, n - k1], [k2, n - k2]])[1]
        fisher_hits += fisher_cache[(k1, k2)] < 0.05
    return {"p_induced": p, "sd": sd, "n_per_arm": n, "power_bootstrap_mean": boot_hits / sims,
            "power_fisher_flag": fisher_hits / sims, "true_mean_difference": p * (INDUCED_MEAN - ANCHOR_MEAN)}


def t2a_power(p_low: float, p_high: float, n: int, sims: int, boot: int, rng: np.random.Generator) -> float:
    hits = 0
    for _ in range(sims):
        hi = (rng.random(n) < p_high).astype(float)
        lo = (rng.random(n) < p_low).astype(float)
        hits += boot_excludes_zero(hi, lo, boot, rng)
    return hits / sims


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("out", type=Path)
    ap.add_argument("--n", type=int, default=33)
    ap.add_argument("--sims", type=int, default=2000)
    ap.add_argument("--boot", type=int, default=2000)
    a = ap.parse_args()
    rng = np.random.default_rng(20261020)
    t0 = time.time()
    t1 = [t1_power(p, sd, a.n, a.sims, a.boot, rng) | {"sd_label": label}
          for label, sd in SDS.items() for p in (0.15, 0.20, 0.25, 0.30)]
    t2 = []
    for d in (0.2, 0.35, 0.5):
        t2.append({"difference": d, "scenario": "worst_case", "p_low": 0.5 - d / 2, "p_high": 0.5 + d / 2,
                   "power": t2a_power(0.5 - d / 2, 0.5 + d / 2, a.n, a.sims, a.boot, rng)})
        t2.append({"difference": d, "scenario": "pilot_informed_low_0.05", "p_low": 0.05, "p_high": 0.05 + d,
                   "power": t2a_power(0.05, 0.05 + d, a.n, a.sims, a.boot, rng)})
    # N needed for 0.8 bootstrap power at p = 0.25 under each SD (only computed if N = 33 falls short)
    n_needed = {}
    for label, sd in SDS.items():
        row = next(r for r in t1 if r["sd_label"] == label and r["p_induced"] == 0.25)
        if row["power_bootstrap_mean"] < 0.8:
            for n in range(a.n + 3, 121, 3):
                pw = t1_power(0.25, sd, n, 1000, 1000, rng)["power_bootstrap_mean"]
                if pw >= 0.8:
                    n_needed[label] = {"n_per_arm": n, "power": pw, "sims": 1000, "boot": 1000}
                    break
    out = {"settings": {"n_per_arm": a.n, "sims": a.sims, "boot": a.boot, "sim_seed": 20261020,
                        "anchor_mean": ANCHOR_MEAN, "induced_mean": INDUCED_MEAN, "induced_sd": INDUCED_SD,
                        "flag_threshold": THRESHOLD}, "t1": t1, "t2a": t2,
           "t1_rule": "if bootstrap power at p = 0.25 is below 0.8, report and stop for a decision on N",
           "t1_n_for_0.8_at_p0.25": n_needed, "runtime_s": round(time.time() - t0, 1)}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2), encoding="utf-8")
    for r in t1:
        print("T1 %-14s p=%.2f  diff=%.2f  bootstrap %.3f  fisher %.3f" % (r["sd_label"], r["p_induced"],
              r["true_mean_difference"], r["power_bootstrap_mean"], r["power_fisher_flag"]))
    for r in t2:
        print("T2a d=%.2f %-24s %.2f vs %.2f  power %.3f" % (r["difference"], r["scenario"], r["p_high"], r["p_low"], r["power"]))
    print("N for 0.8 at p=0.25:", n_needed, "runtime", out["runtime_s"], "s")


if __name__ == "__main__":
    main()
