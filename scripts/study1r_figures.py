"""Study 1R paper figures 2 and 3 (human message 74; draft; renumbered from 1 and 2 on human message 77). No API calls;
read-only on runs and results. Figures 1 and 4: scripts/study1r_figures_paper.py.

Figure 2 (was 1), headline comparison (spec: human message 64): per cell, the share of Offer episodes read as accepting by
judge v1, by judge v2 (screener), confirmed by human coding (inclusive acceptance, option A), and flagged by the
behavioral flag; Wilson 95% CIs; numbers from results/study1r/results.json ("Judge comparison figure"). Exploratory.

Figure 3 (was 2), price paths by acceptance in 4.1-high (no written specification found; choices recorded in D-120 as a
proposal): per round 1-30, the mean of the two LLM sellers' posted asks (the quantity averaged by the change score),
averaged over episodes, for 4.1-high Offer episodes with human-confirmed inclusive acceptance, 4.1-high Offer episodes
without it, and 4.1-high Silent; 95% percentile bootstrap CI over episodes (2,000 resamples, seed 20261025). Episode
acceptance comes from the frozen `build` of scripts/study1r_results.py on completed episodes only (the D-116 wrapper's
staging). Exploratory, descriptive.

Light-mode reference palette (dataviz skill), validated: slots 1-4 pass; aqua and yellow are below 3:1 contrast, so
every bar carries a value label and the lines are direct-labeled.

Usage: python scripts/study1r_figures.py <out_dir> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.stage2_analysis import wilson  # noqa: E402
from sting.stage2_measures import rounds_of  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
CELLS = [("mini-low", "gpt-4.1-mini, low"), ("4.1-low", "gpt-4.1, low"), ("4.1-high", "gpt-4.1, high")]
MEASURES = [("v1_read", "Judge v1"), ("v2_read", "Judge v2 (screener)"), ("human_coded", "Human-confirmed"),
            ("behavioral_flag", "Behavioral flag")]
SEED = 20261025


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def style(ax) -> None:
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
        ax.spines[s].set_linewidth(0.8)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.yaxis.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def figure1(results: dict, out: Path) -> dict:
    fig_data = results["Judge comparison figure (exploratory: v1-read, v2-read, human-confirmed, behavioral)"]
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=300, facecolor=SURFACE)
    style(ax)
    width, gap = 0.19, 0.012
    for j, (key, label) in enumerate(MEASURES):
        for i, (cell, _) in enumerate(CELLS):
            d = fig_data[cell][key]
            x = i + (j - 1.5) * (width + gap)
            if not d["n"]:
                ax.text(x, 0.02, "not\ncoded", ha="center", va="bottom", fontsize=6.5, color=INK2)
                continue
            lo, hi = d["ci"]
            ax.bar(x, d["rate"], width, color=SERIES[j], edgecolor=SURFACE, linewidth=1.0, zorder=2)
            ax.errorbar(x, d["rate"], yerr=[[d["rate"] - lo], [hi - d["rate"]]], fmt="none", ecolor=INK2,
                        elinewidth=0.8, capsize=2, zorder=3)
            ax.text(x, hi + 0.02, f"{d['k']}/{d['n']}", ha="center", va="bottom", fontsize=6.5, color=INK)
    ax.set_xticks(range(len(CELLS)))
    ax.set_xticklabels([f"{c}\n({desc})" for c, desc in CELLS], fontsize=9, color=INK)
    ax.set_ylim(0, 1.12)
    ax.set_yticks(np.linspace(0, 1, 6))
    ax.set_ylabel("Share of Offer episodes", fontsize=9.5, color=INK)
    ax.set_title("Acceptance of the sting offer by measure, per cell (Study 1R, exploratory)", fontsize=10.5,
                 color=INK, loc="left", pad=24)
    from matplotlib.patches import Patch
    leg = ax.legend(handles=[Patch(color=SERIES[j], label=lab) for j, (_, lab) in enumerate(MEASURES)],
                    loc="lower left", ncol=4, fontsize=8, frameon=False, bbox_to_anchor=(0, 1.0),
                    handlelength=1.2, columnspacing=1.2, borderaxespad=0.2)
    for t in leg.get_texts():
        t.set_color(INK)
    fig.tight_layout()
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)
    return fig_data


def episode_paths(campaign_yaml: Path, logs: list[Path], sheet: Path, key: Path) -> dict:
    wrap = load("study1r_results_completed.py", "wrap_fig")
    res = load("study1r_results.py", "res_fig")
    human, strata, protected = res.verify_labels(sheet, key)
    with tempfile.TemporaryDirectory(prefix="s1r_fig_") as tmp:
        staged, excluded = wrap.stage(logs, Path(tmp))
        episodes = res.build([campaign_yaml], staged, human, strata, {}, {}, False, protected)
        groups = {"accept": [], "no_accept": [], "silent": []}
        x_values = []
        for log in staged:
            camp = json.loads(log.read_text(encoding="utf-8"))
            for name, info in camp["arms"].items():
                if not name.startswith("4.1-high"):
                    continue
                for rep in sorted(p for p in Path(info["run_dir"]).iterdir() if p.is_dir()):
                    e = next(x for x in episodes if x["replicate_id"] == rep.name)
                    llm = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))["llm_seller_ids"]
                    path = {}
                    for r in rounds_of(rep):
                        asks = [a for s, a in r["seller_asks"].items() if s in llm and isinstance(a, (int, float))
                                and not isinstance(a, bool)]
                        if asks:
                            path[r["round_number"]] = sum(asks) / len(asks)
                    if e["arm"] == "silent":
                        groups["silent"].append(path)
                    elif e["arm"] == "offer":
                        groups["accept" if e.get("acc_inclusive") else "no_accept"].append(path)
                        x_values.append(e["x"])
    return {"groups": groups, "x_values": x_values, "excluded": excluded}


def figure2(paths: dict, out: Path) -> dict:
    rng = np.random.default_rng(SEED)
    rounds = list(range(1, 31))
    names = [("accept", "Offer, human-confirmed acceptance"), ("no_accept", "Offer, no confirmed acceptance"),
             ("silent", "Silent")]
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=300, facecolor=SURFACE)
    style(ax)
    ax.axvspan(5.5, 9.5, color=GRID, alpha=0.5, lw=0, zorder=0)
    ax.axvline(10, color=INK2, lw=0.8, ls=(0, (3, 3)), zorder=1)
    summary = {}
    for j, (g, label) in enumerate(names):
        eps = paths["groups"][g]
        mean, lo, hi = [], [], []
        for r in rounds:
            v = np.array([p[r] for p in eps if r in p])
            m = v.mean() if v.size else np.nan
            boot = v[rng.integers(0, v.size, size=(2000, v.size))].mean(axis=1) if v.size else np.array([np.nan])
            mean.append(m)
            lo.append(np.quantile(boot, 0.025))
            hi.append(np.quantile(boot, 0.975))
        ax.fill_between(rounds, lo, hi, color=SERIES[j], alpha=0.15, lw=0, zorder=2)
        ax.plot(rounds, mean, color=SERIES[j], lw=2, zorder=3, label=f"{label} (n = {len(eps)})")
        ax.text(30.4, mean[-1], f"{label.split(',')[-1].strip()}\n(n = {len(eps)})", color=INK, fontsize=7,
                va="center")
        summary[g] = {"n": len(eps), "mean_by_round": dict(zip(rounds, [round(float(m), 4) for m in mean])),
                      "ci_by_round": {r: [round(float(a), 4), round(float(b), 4)] for r, a, b in zip(rounds, lo, hi)}}
    xs = np.array(paths["x_values"], dtype=float)
    top = ax.get_ylim()[1]
    ax.text(7.5, top, "pre window\n(rounds 6-9)", fontsize=7, color=INK2, va="top", ha="center")
    ax.text(10.2, top, "Seller C's proposal\n(Offer) from round 10", fontsize=7, color=INK2, va="top")
    ax.set_xlim(1, 30)
    ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax.set_xlabel("Round", fontsize=9.5, color=INK)
    ax.set_ylabel("Mean ask of the two LLM sellers ($)", fontsize=9.5, color=INK)
    ax.set_title("Price paths in 4.1-high by confirmed acceptance (Study 1R, exploratory)", fontsize=10.5,
                 color=INK, loc="left")
    fig.tight_layout(rect=(0, 0.07, 0.86, 1))
    handles, labels = ax.get_legend_handles_labels()
    leg = fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.005), ncol=3, fontsize=7.5,
                     frameon=False)
    for t in leg.get_texts():
        t.set_color(INK)
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)
    summary["x_offer"] = {"n": int(xs.size), "mean": float(xs.mean()), "min": float(xs.min()), "max": float(xs.max())}
    return summary


def main() -> None:
    out_dir, cy = Path(sys.argv[1]), Path(sys.argv[2])
    logs = [Path(p) for p in sys.argv[3].split(",") if p]
    sheet, key = Path(sys.argv[4]), Path(sys.argv[5])
    out_dir.mkdir(parents=True, exist_ok=True)
    results = json.loads((REPO / "results" / "study1r" / "results.json").read_text(encoding="utf-8"))["results"]
    f1 = figure1(results, out_dir / "fig2_headline_comparison.png")
    paths = episode_paths(cy, logs, sheet, key)
    f2 = figure2(paths, out_dir / "fig3_price_paths_4.1-high.png")
    data = {"label": "exploratory; draft figures", "fig2_headline": f1, "fig3_price_paths": f2,
            "excluded_episodes": [e["replicate_id"] for e in paths["excluded"]]}
    (out_dir / "figure_data.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps({"fig2_n": {g: f2[g]["n"] for g in ("accept", "no_accept", "silent")}, "x": f2["x_offer"],
                      "excluded": data["excluded_episodes"]}))


if __name__ == "__main__":
    main()
