"""Power analysis for the low-cell T1 contrast (Offer minus Anchor, unpaired), human message 16.

Inputs (from the human): SD = upper 80% confidence bound of the arm-a SD (gpt-4.1-mini default, real
structure; episode outcomes from results/diagnostics/stepAB_summary.json); minimum effect $2; power 0.80;
unpaired. Alpha: two-sided 0.05, matching T1's "bootstrap 95% CI excludes zero".

"Upper 80% confidence bound" is computed as the one-sided bound SD * sqrt(df / chi2_{0.20, df}).
The upper end of a two-sided 80% interval (chi2_{0.10, df}) is reported alongside.

N per arm by (1) the normal approximation n = 2 (z_{1-a/2} + z_{power})^2 SD^2 / d^2 and (2) the exact
two-sample t-test power (noncentral t), smallest n reaching 0.80. The bootstrap CI analysis has no closed
form; these are planning approximations.

Cost: measured cost per 30-round episode in the real structure (stage1a runs, OpenRouter-reported):
low cell = gpt-4.1-mini default (arm a episodes), medium = gpt-4.1 default (arm d), high = gpt-4.1 CEO
(arm e). Stage 2 plan: low cell 5 arms (silent, sham, anchor, rapport, offer); medium and high 2 arms each
(silent, offer). Same N per arm in every cell (an assumption; the human may set medium/high N separately).

Usage: python scripts/power_t1.py results/diagnostics/stepAB_summary.json results/power/power_t1.json
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from pathlib import Path

from scipy import stats


def t_power(n: int, d: float, sd: float, alpha: float = 0.05) -> float:
    df = 2 * n - 2
    ncp = d / (sd * math.sqrt(2 / n))
    tcrit = stats.t.ppf(1 - alpha / 2, df)
    return (1 - stats.nct.cdf(tcrit, df, ncp)) + stats.nct.cdf(-tcrit, df, ncp)


def main() -> None:
    summary = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    eps = summary["episodes"]

    def arm(name):
        return [e for e in eps if e["run_name"] == name and e["status"] == "completed"]

    a = arm("stage1a_a_gpt-4.1-mini_default")
    ys = [e["outcome_round_mean_ask"] for e in a]
    n, sd = len(ys), statistics.stdev(ys)
    df = n - 1
    sd_upper_one_sided_80 = sd * math.sqrt(df / stats.chi2.ppf(0.20, df))
    sd_upper_two_sided_80 = sd * math.sqrt(df / stats.chi2.ppf(0.10, df))
    d, alpha, power = 2.0, 0.05, 0.80
    z = stats.norm.ppf(1 - alpha / 2) + stats.norm.ppf(power)

    def n_needed(s):
        normal = 2 * z * z * s * s / (d * d)
        k = 2
        while t_power(k, d, s, alpha) < power:
            k += 1
        return {"sd": s, "n_normal_approx": normal, "n_normal_approx_ceil": math.ceil(normal),
                "n_t_test": k, "power_at_n_t_test": t_power(k, d, s, alpha)}

    primary = n_needed(sd_upper_one_sided_80)
    alternative = n_needed(sd_upper_two_sided_80)
    point = n_needed(sd)

    cost = {
        "low_gpt-4.1-mini_default": statistics.mean(e["cost_usd"] for e in a),
        "medium_gpt-4.1_default": statistics.mean(e["cost_usd"] for e in arm("stage1a_d_gpt-4.1_default")),
        "high_gpt-4.1_ceo": statistics.mean(e["cost_usd"] for e in arm("stage1a_e_gpt-4.1_ceo")),
    }
    arms = {"low_gpt-4.1-mini_default": 5, "medium_gpt-4.1_default": 2, "high_gpt-4.1_ceo": 2}
    per_rep = sum(cost[c] * k for c, k in arms.items())

    def plan(n_arm):
        return {"n_per_arm": n_arm, "episodes": n_arm * sum(arms.values()),
                "cost_by_cell": {c: n_arm * k * cost[c] for c, k in arms.items()},
                "total_cost": n_arm * per_rep}

    out = {
        "arm_a_episode_outcomes": ys, "arm_a_n": n, "arm_a_sd": sd,
        "sd_upper_80_one_sided": sd_upper_one_sided_80, "sd_upper_80_two_sided_interval": sd_upper_two_sided_80,
        "min_effect": d, "alpha_two_sided": alpha, "power": power,
        "n_primary_one_sided_bound": primary, "n_alternative_two_sided_bound": alternative,
        "n_at_point_estimate_sd": point,
        "cost_per_episode": cost, "arms_per_cell": arms, "cost_per_replicate_set": per_rep,
        "plan_primary": plan(primary["n_t_test"]), "plan_alternative": plan(alternative["n_t_test"]),
    }
    Path(sys.argv[2]).parent.mkdir(parents=True, exist_ok=True)
    Path(sys.argv[2]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("arm_a_sd", "sd_upper_80_one_sided", "sd_upper_80_two_sided_interval")}, indent=1))
    for k in ("n_primary_one_sided_bound", "n_alternative_two_sided_bound", "n_at_point_estimate_sd"):
        print(k, {x: round(v, 4) if isinstance(v, float) else v for x, v in out[k].items()})
    print("cost per episode", {k: round(v, 4) for k, v in cost.items()}, "per replicate set", round(per_rep, 4))
    for k in ("plan_primary", "plan_alternative"):
        p = out[k]
        print(k, "n/arm", p["n_per_arm"], "episodes", p["episodes"], "cost", round(p["total_cost"], 2),
              {c: round(v, 2) for c, v in p["cost_by_cell"].items()})


if __name__ == "__main__":
    main()
