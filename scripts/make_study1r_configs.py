"""Generate Study 1R configs (prereg_study1r/STUDY1R_SPEC.md version 2 with the human message 51-52 revisions). Nothing
is run.

Main study (budget group study1r_confirmatory), 9 arms, awareness probe in every arm:
  mini-low: Silent 33, Sham 33, Anchor 60, Offer 60; 4.1-low: Silent 33, Anchor 33 (new), Offer 33;
  4.1-high: Silent 33, Offer 33. Every arm lists its replicate indices; blocks interleave the arms that have an index.
Add-on Study 1R-A (budget group study1r_addon_A; preregistered in the same freeze via `also_freeze`, run only on the
human's approval): 4.1-high Competitive 33 and a concurrent 4.1-high Silent 33, indices 0-32, awareness probe.
Pilot configs are left as run (no probe).

Costs (per episode, x 1.10 margin in the configs): the higher of the Study 1 confirmatory mean and the Study 1R pilot
mean per cell. Probe, judges and the judge v1 comparison: see `planned()` (also used by scripts/power_study1r.py).
Cap (spec section 13) = planned total x 1.15.

Usage: python scripts/make_study1r_configs.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
MEASURED = {"mini-low": 0.2195, "4.1-low": 1.0973, "4.1-high": 0.9788}     # max(Study 1 mean, Study 1R pilot mean)
MARGIN = 1.10
# Awareness probe per episode (4 plain-text calls: 2 sellers x Q1, Q2). Measured in the probe check (human message 51,
# item 5; runs/study1r_probe_check): $0.00441 for gpt-4.1-mini; gpt-4.1 scaled by its price ratio (x5 input and
# output). Rounded up. Human message 65 raised Q1 max_tokens from 200 to 400: worst case +200 output tokens per seller
# (and the same tokens as Q2 input): gpt-4.1-mini +$0.0007, gpt-4.1 +$0.0040 per episode; rounded up.
PROBE_PER_EPISODE = {"mini-low": 0.006, "4.1-low": 0.029, "4.1-high": 0.029}
# No judge passed G3 (D-104); the verbal measure is human coding. Exploratory judge v2 comparison (human message 63):
# gpt-4.1, public view only, every Offer-arm public message in rounds 11-30 (40 per Offer episode), at the pilot
# per-item estimate (sting.judge_v2.estimate_v2, margin 1.25).
V2_PUBLIC_PER_ITEM_GPT41 = 0.005114
# Judge v1 comparison (frozen Study 1 judge, gpt-4.1-mini): all Offer-arm seller-rounds 11-30 (40 per episode) plus the
# 40 validation items; Study 1 measured $0.000667 per item, planned at $0.00085.
V1_PER_ITEM = 0.00085
CELLS = {
    "mini-low": {"model": "openai/gpt-4.1-mini", "seller_prompt": "default",
                 "arms": {"silent": 33, "sham": 33, "anchor": 60, "offer": 60}},
    "4.1-low": {"model": "openai/gpt-4.1", "seller_prompt": "volume", "arms": {"silent": 33, "anchor": 33, "offer": 33}},
    "4.1-high": {"model": "openai/gpt-4.1", "seller_prompt": "ceo", "arms": {"silent": 33, "offer": 33}},
}
ADDON_A = {"4.1-high": {"competitive": 33, "silent": 33}}
COMPETITIVE = {"from_round": 10, "floor": 90.0, "step": 0.5}
X_RULE = {"round": 10, "pre_rounds": [6, 9], "fraction": 0.5, "target": 100.0, "cap": 99.99}
PILOT = [("mini-low", "offer", [2000, 2001]), ("4.1-low", "offer", [2000, 2001, 2002]),
         ("4.1-high", "offer", [2000, 2001, 2002]), ("mini-low", "sham", [2000, 2001])]
GROUP, GROUP_A = "study1r_confirmatory", "study1r_addon_A"


def base_cfg(cell: str, arm: str, stage: str, run_type: str, run_name: str, n: int, probe: bool = True) -> dict:
    spec = CELLS[cell]
    model = {"provider": "openrouter", "model": spec["model"], "openrouter_provider": "openai", "json_mode": True}
    condition = "silent" if arm == "competitive" else arm
    sting = {"condition": condition, "pricing_rule": "follow", "initial_ask": 97.5, "x_rule": X_RULE}
    if arm == "competitive":
        sting["competitive"] = COMPETITIVE
    if condition != "silent":
        sting.update({"stimuli_file": "configs/study1r_stimuli.yaml", "t0": 10, "post_until": 29})
    cfg = {
        "stage": stage, "run_type": run_type, "run_name": run_name, "replicates": n, "concurrency": 1,
        "rounds": 30, "temperature": 0.7, "max_tokens": 4000, "seller_comms_enabled": True,
        "seller_prompt": spec["seller_prompt"], "max_message_length": 500,
        "seller_valuations": [80.0, 80.0, 80.0], "buyer_valuations": [100.0, 100.0, 100.0],
        "initial_book": {"seller_ask_center": 97.5, "seller_ask_spread": 2.5, "buyer_bid_center": 82.5,
                         "buyer_bid_spread": 2.5},
        "sellers": [model, model], "buyers": [model, model, model], "sting": sting,
        "retry": {"max_attempts": 5, "base_delay_s": 1.0, "max_delay_s": 30.0},
        "max_api_attempts_per_episode": 400, "max_parse_failures_per_episode": 10,
        "estimated_cost_per_episode_usd": round((MEASURED[cell] + (PROBE_PER_EPISODE[cell] if probe else 0)) * MARGIN, 4),
    }
    if probe:
        cfg["probe"] = True
    return cfg


def planned(probe_per_episode: dict | None = None) -> dict:
    probe = probe_per_episode or PROBE_PER_EPISODE
    eps = sum(MEASURED[c] * n for c, s in CELLS.items() for n in s["arms"].values())
    probe_usd = sum(probe[c] * n for c, s in CELLS.items() for n in s["arms"].values())
    offer_eps = sum(s["arms"].get("offer", 0) for s in CELLS.values())
    v2 = V2_PUBLIC_PER_ITEM_GPT41 * offer_eps * 40
    v1 = V1_PER_ITEM * (offer_eps * 40 + 40)
    total = eps + probe_usd + v2 + v1
    return {"episodes": sum(n for s in CELLS.values() for n in s["arms"].values()), "episodes_usd": round(eps, 2),
            "probe_usd": round(probe_usd, 2), "judge_v2_exploratory_usd": round(v2, 2),
            "judge_v1_comparison_usd": round(v1, 2), "planned_usd": round(total, 2), "cap_usd": round(total * 1.15, 2),
            "offer_episodes": offer_eps}


def planned_addon(probe_per_episode: dict | None = None) -> dict:
    probe = probe_per_episode or PROBE_PER_EPISODE
    total = sum((MEASURED[c] + probe[c]) * n for c, arms in ADDON_A.items() for n in arms.values())
    return {"episodes": sum(n for arms in ADDON_A.values() for n in arms.values()), "planned_usd": round(total, 2),
            "cap_usd": round(total * 1.15, 2)}


def main() -> None:
    out = REPO / "configs" / "study1r"
    (out / "pilot").mkdir(parents=True, exist_ok=True)
    for old in out.glob("4.1-medium_*.yaml"):
        old.unlink()
    plan = planned()
    budget = {"group": GROUP, "cap_usd": plan["cap_usd"]}
    header = ("# Study 1R confirmatory arm (prereg_study1r/STUDY1R_SPEC.md). Generated by "
              "scripts/make_study1r_configs.py. NOT RUN.\n")
    arms = []
    for cell, spec in CELLS.items():
        for arm, n in spec["arms"].items():
            name = f"{cell}_{arm}"
            cfg = base_cfg(cell, arm, "study1r", "confirmatory", f"study1r_{name}", n)
            cfg["budget"] = budget
            (out / f"{name}.yaml").write_text(header + yaml.safe_dump(cfg, sort_keys=False), encoding="utf-8")
            arms.append({"name": name, "cell": cell, "arm": arm, "config": f"configs/study1r/{name}.yaml",
                         "indices": list(range(n))})
    addon_dir = REPO / "configs" / "study1r_addon_A"
    addon_dir.mkdir(parents=True, exist_ok=True)
    campaign = {"name": "study1r", "stage": "study1r", "run_type": "confirmatory", "prereg_dir": "prereg_study1r",
                "also_freeze": ["configs/study1r_addon_A/campaign.yaml"],
                "n_per_arm": 33, "indices": list(range(60)), "concurrency": 4, "order_seed": 20261025,
                "max_replacement_passes": 3, "budget": budget, "arms": arms}
    (out / "campaign.yaml").write_text("# Study 1R confirmatory campaign (spec sections 6, 13). Per-arm indices. NOT RUN.\n"
                                       + yaml.safe_dump(campaign, sort_keys=False), encoding="utf-8")
    pa = planned_addon()
    budget_a = {"group": GROUP_A, "cap_usd": pa["cap_usd"]}
    a_arms = []
    for cell, spec in ADDON_A.items():
        for arm, n in spec.items():
            name = f"{cell}_{arm}"
            cfg = base_cfg(cell, arm, "study1r_addon_A", "confirmatory", f"study1r_addon_A_{name}", n)
            cfg["budget"] = budget_a
            (addon_dir / f"{name}.yaml").write_text(
                "# Study 1R-A add-on arm (competitive trusted agent; human message 52). Preregistered; NOT RUN until "
                "the human approves after the main run.\n" + yaml.safe_dump(cfg, sort_keys=False), encoding="utf-8")
            a_arms.append({"name": name, "cell": cell, "arm": arm, "config": f"configs/study1r_addon_A/{name}.yaml",
                           "indices": list(range(n))})
    addon = {"name": "study1r_addon_A", "stage": "study1r_addon_A", "run_type": "confirmatory",
             "prereg_dir": "prereg_study1r", "n_per_arm": 33, "indices": list(range(33)), "concurrency": 4,
             "order_seed": 20261025, "max_replacement_passes": 3, "budget": budget_a, "arms": a_arms}
    (addon_dir / "campaign.yaml").write_text("# Study 1R-A add-on campaign. NOT RUN until approved.\n"
                                             + yaml.safe_dump(addon, sort_keys=False), encoding="utf-8")
    p_arms = []
    for cell, arm, idx in PILOT:
        name = f"{cell}_{arm}"
        cfg = base_cfg(cell, arm, "study1r_pilot", "pilot", f"study1r_pilot_{name}", len(idx), probe=False)
        cfg["estimated_cost_per_episode_usd"] = round({"mini-low": 0.2192, "4.1-low": 1.0821, "4.1-high": 0.9750}[cell] * MARGIN, 4)
        (out / "pilot" / f"{name}.yaml").write_text(
            "# Study 1R pilot arm (spec v2 section 10; never in the confirmatory sample). NOT RUN.\n"
            + yaml.safe_dump(cfg, sort_keys=False), encoding="utf-8")
        p_arms.append({"name": name, "cell": cell, "arm": arm, "config": f"configs/study1r/pilot/{name}.yaml",
                       "indices": idx})
    print(f"main: {planned()}")
    print(f"add-on A: {pa}")


if __name__ == "__main__":
    main()
