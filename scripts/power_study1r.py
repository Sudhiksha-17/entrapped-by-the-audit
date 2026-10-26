"""Study 1R power analysis from Study 1 data (prereg_study1r/STUDY1R_SPEC.md version 2, section 12). No API calls.

Change score per Study 1 confirmatory episode = mean posted LLM-seller ask over rounds 11-30 minus over rounds 6-9
(sting.stage2_measures.window_mean). Per arm: n, mean, SD, and the one-sided upper 80% confidence bound on SD,
SD x sqrt((n - 1) / chi2_0.20(n - 1)).

T1 (mini-low, Offer minus Anchor, change score; supported only if the 95% CI lies entirely above 0), reported at
N = 60 per arm (spec), with N = 33 and 45 for comparison:
- analytic, minimum effect $2.00: power = Phi(2 / sqrt((SD_o^2 + SD_a^2) / N) - z_0.975), with the upper-bound SDs of
  the Study 1 mini-low Offer and Anchor arms (point SDs and the largest upper-bound SD as variants);
- mixture simulation (as in Study 1): Anchor change ~ Normal(mean, SD) from the Study 1 mini-low Anchor arm; Offer:
  a share p of episodes induced to X, change ~ Normal(m_ind, 0.5) with m_ind = mean over Study 1 mini-low episodes of
  X - pre = 0.5 x (100 - pre); the rest from the Anchor distribution. p* gives a $2.00 mean difference. Power = share
  of simulated datasets whose percentile bootstrap 95% CI lies entirely above 0.
T2a (public verbal acceptance rate, 4.1-high minus 4.1-low, N = 33 per arm; CI entirely above 0): binomial flags,
worst case (rates 0.5 -/+ d/2) and low-rate case (low 0.05, high 0.05 + d), d = 0.20, 0.35, 0.50; same bootstrap.
2,000 simulated datasets x 2,000 resamples per scenario; seed 20261023.
Cost: scripts/make_study1r_configs.py `planned` for each judge candidate, plus pilot and validation estimates.

Usage: python scripts/power_study1r.py
"""
from __future__ import annotations

import glob
import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np
import yaml
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.paths import REPO_ROOT  # noqa: E402
from sting.stage2_measures import rounds_of, window_mean  # noqa: E402

OUT = REPO_ROOT / "results" / "power"
DELTA = 2.00
T1_NS = [33, 45, 60]
T2A_N = 33
T2A_D = [0.20, 0.35, 0.50]
SIMS, BOOT, SEED = 2000, 2000, 20261023
PILOT_AND_VALIDATION = {"pilot (10 episodes)": 7.75, "judge development (30 items x 2 candidates x <= 3 prompt versions)": 0.60,
                        "G3 validation runs (40 items x 2 candidates)": 0.20}

_spec = importlib.util.spec_from_file_location("cfgs", Path(__file__).resolve().parent / "make_study1r_configs.py")
cfgs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cfgs)


def study1_changes() -> dict[str, list[dict]]:
    arms = {a["name"]: a for a in yaml.safe_load((REPO_ROOT / "configs" / "stage2" / "campaign.yaml")
                                                 .read_text(encoding="utf-8"))["arms"]}
    out: dict[str, list[dict]] = {}
    for c in sorted(glob.glob(str(REPO_ROOT / "runs" / "stage2" / "_campaigns" / "*" / "campaign.json"))):
        for name, info in json.loads(Path(c).read_text(encoding="utf-8"))["arms"].items():
            for rep in sorted(p for p in Path(info["run_dir"]).iterdir() if p.is_dir()):
                llm = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))["llm_seller_ids"]
                rounds = rounds_of(rep)
                pre, post = window_mean(rounds, llm, range(6, 10)), window_mean(rounds, llm, range(11, 31))
                out.setdefault(name, []).append({"pre": pre, "post": post, "change": post - pre})
    return out


def sd_upper80(sd: float, n: int) -> float:
    return sd * math.sqrt((n - 1) / stats.chi2.ppf(0.20, n - 1))


def analytic_power(sd1: float, sd2: float, n: int, delta: float = DELTA) -> float:
    return float(stats.norm.cdf(delta / math.sqrt((sd1 ** 2 + sd2 ** 2) / n) - stats.norm.ppf(0.975)))


def ci_above_zero(a: np.ndarray, b: np.ndarray, rng: np.random.Generator) -> bool:
    da = a[rng.integers(0, a.size, size=(BOOT, a.size))].mean(axis=1)
    db = b[rng.integers(0, b.size, size=(BOOT, b.size))].mean(axis=1)
    return bool(np.quantile(da - db, 0.025) > 0)


def t1_sim(p: float, mu_a: float, sd: float, m_ind: float, n: int, rng: np.random.Generator) -> float:
    hits = 0
    for _ in range(SIMS):
        anchor = rng.normal(mu_a, sd, n)
        induced = rng.random(n) < p
        offer = np.where(induced, rng.normal(m_ind, 0.5, n), rng.normal(mu_a, sd, n))
        hits += ci_above_zero(offer, anchor, rng)
    return hits / SIMS


def t2a_sim(p_low: float, p_high: float, n: int, rng: np.random.Generator) -> float:
    hits = 0
    for _ in range(SIMS):
        hits += ci_above_zero((rng.random(n) < p_high).astype(float), (rng.random(n) < p_low).astype(float), rng)
    return hits / SIMS


def main() -> None:
    ch = study1_changes()
    per_arm = {}
    for name, eps in sorted(ch.items()):
        x = np.array([e["change"] for e in eps])
        sd = float(x.std(ddof=1))
        per_arm[name] = {"n": int(x.size), "mean": float(x.mean()), "sd": sd, "sd_upper80": sd_upper80(sd, x.size)}
    o, a = per_arm["mini-low_offer"], per_arm["mini-low_anchor"]
    worst = max(v["sd_upper80"] for v in per_arm.values())
    analytic = {"upper80 SDs (mini-low offer, anchor)": {n: analytic_power(o["sd_upper80"], a["sd_upper80"], n) for n in T1_NS},
                "point SDs (mini-low offer, anchor)": {n: analytic_power(o["sd"], a["sd"], n) for n in T1_NS},
                f"largest upper80 SD of any arm ({worst:.3f})": {n: analytic_power(worst, worst, n) for n in T1_NS}}
    mini = [e for k, v in ch.items() if k.startswith("mini-low") for e in v]
    m_ind = float(np.mean([0.5 * (100 - e["pre"]) for e in mini]))
    p_star = DELTA / (m_ind - a["mean"])
    rng = np.random.default_rng(SEED)
    t1 = []
    for sd_label, sd in (("anchor point SD", a["sd"]), ("anchor upper80 SD", a["sd_upper80"])):
        for p in sorted((0.20, round(p_star, 4), 0.30)):
            t1.append({"sd": sd_label, "sd_value": sd, "p_induced": p, "mean_difference": p * (m_ind - a["mean"]),
                       "power": {n: t1_sim(p, a["mean"], sd, m_ind, n, rng) for n in T1_NS}})
    t2a = []
    for d in T2A_D:
        t2a.append({"d": d, "worst_case": t2a_sim(0.5 - d / 2, 0.5 + d / 2, T2A_N, rng),
                    "low_rate_0.05": t2a_sim(0.05, 0.05 + d, T2A_N, rng)})
    costs = {"human-coded verbal measure (no judge passed G3)": cfgs.planned()}
    R = {"per_arm_change_score": per_arm, "t1_analytic": analytic, "m_induced": m_ind, "anchor_mean_change": a["mean"],
         "p_star_for_2usd": p_star, "t1_simulation": t1, "t2a_simulation": t2a, "costs": costs,
         "pilot_and_validation": PILOT_AND_VALIDATION,
         "settings": {"delta": DELTA, "sims": SIMS, "boot": BOOT, "seed": SEED, "t1_ns": T1_NS, "t2a_n": T2A_N}}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "power_study1r.json").write_text(json.dumps(R, indent=2), encoding="utf-8")
    pv = sum(PILOT_AND_VALIDATION.values())
    L = ["# Study 1R power analysis (spec version 2, section 12; from Study 1 data)", "",
         "Generated by `scripts/power_study1r.py` (no API calls). Change score = mean posted LLM-seller ask, rounds 11-30, "
         "minus rounds 6-9. Study 1 stimuli differ from Study 1R (one post at $98 vs a talking sting posting at X every "
         "round), so these SDs are a proxy.", "",
         "## Per-arm change score (Study 1, n = 33 each)", "", "| Arm | Mean | SD | Upper 80% SD bound |", "|---|---|---|---|"]
    for k, v in per_arm.items():
        L.append(f"| {k} | {v['mean']:.3f} | {v['sd']:.3f} | {v['sd_upper80']:.3f} |")
    L += ["", "## T1 analytic power ($2.00; 95% CI entirely above 0)", "",
          "| SD basis | " + " | ".join(f"N={n}" for n in T1_NS) + " |", "|---|" + "---|" * len(T1_NS)]
    for k, v in analytic.items():
        L.append(f"| {k} | " + " | ".join(f"{v[n]:.3f}" for n in T1_NS) + " |")
    L += ["", "## T1 mixture simulation", "",
          f"m_ind = {m_ind:.3f}; Anchor mean change {a['mean']:.3f}; p* = {p_star:.4f} gives a $2.00 difference.", "",
          "| Anchor SD | p induced | Mean difference | " + " | ".join(f"N={n}" for n in T1_NS) + " |",
          "|---|---|---|" + "---|" * len(T1_NS)]
    for r in t1:
        L.append(f"| {r['sd']} ({r['sd_value']:.3f}) | {r['p_induced']} | {r['mean_difference']:.3f} | "
                 + " | ".join(f"{r['power'][n]:.3f}" for n in T1_NS) + " |")
    L += ["", f"## T2a power at N = {T2A_N} per arm (rate difference; 95% CI entirely above 0)", "",
          "| d | Worst case (0.5 -/+ d/2) | Low rate 0.05 |", "|---|---|---|"]
    for r in t2a:
        L.append(f"| {r['d']} | {r['worst_case']:.3f} | {r['low_rate_0.05']:.3f} |")
    L += ["", "## Cost and cap (episodes at the higher of Study 1 and pilot cost; probe; exploratory judges v2 public and v1; cap = planned x 1.15)", "",
          "| Plan | Episodes | Episodes $ | Judges (exploratory) $ | Planned $ | Cap $ | Plus pilot and validation $ |",
          "|---|---|---|---|---|---|---|"]
    for jm, v in costs.items():
        L.append(f"| {jm} | {v['episodes']} | {v['episodes_usd']} | {v['judge_v2_exploratory_usd'] + v['judge_v1_comparison_usd']:.2f} | {v['planned_usd']} | {v['cap_usd']} | "
                 f"{v['planned_usd'] + pv:.2f} |")
    L += ["", "Pilot and validation (outside the confirmatory budget group): " +
          "; ".join(f"{k} ${v:.2f}" for k, v in PILOT_AND_VALIDATION.items()) + f"; total ${pv:.2f}."]
    (OUT / "POWER_STUDY1R.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
