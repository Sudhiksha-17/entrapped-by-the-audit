"""Final paper figures, 300 dpi, in the order of human message 82 step 5 (no new analyses; no API calls).

Figure 1 = headline acceptance comparison (`figure1` of scripts/study1r_figures.py, unchanged).
Figure 2 = design schematic (panels a and b from scripts/study1r_figures_paper.py, unchanged; panel c, the N table, now
           also lists the Study 1R-C cells, completed episodes from RESULTS_1RC.md).
Figure 3 = 4.1-high price paths (`figure2` of scripts/study1r_figures.py, unchanged).
Figure 4 = forest plot of change-score contrasts (the rows of scripts/study1r_figures_paper.py, plus the two Study 1R-C
           primary contrasts, Silent-floor minus Silent, read from results/study1r_addon_C/analysis/results_1rc.json).

Inputs are the committed results files and, for Figure 3, the run logs (as scripts/study1r_figures.py). The draft
figures in results/study1r/figures/ are kept unchanged.

Usage: python scripts/study1r_figures_final.py <out_dir> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


D = load("study1r_figures.py", "fig_draft")
P = load("study1r_figures_paper.py", "fig_paper")
SURFACE, INK, INK2, GRID, MINUS = P.SURFACE, P.INK, P.INK2, P.GRID, P.MINUS
YELLOW = "#eda100"  # categorical slot 4 of the dataviz reference palette (slots 1-4 validated, light mode)

# Display labels (human message 90): cells and add-ons by name; study codes only in the Figure 2 table.
CELL_LABEL = {"mini-low": "mini group (gpt-4.1-mini, default)", "4.1-low": "volume group (gpt-4.1, volume prompt)",
              "4.1-high": "CEO group (gpt-4.1, CEO prompt)"}
CELL_SHORT = {"mini-low": "mini group", "4.1-low": "volume group", "4.1-high": "CEO group"}
ARMS = ["Silent", "Sham", "Anchor", "Offer", "Competitive", "Silent-floor", "Offer-floor"]
N_TABLE = [  # completed episodes analysed (RESULTS.md, RESULTS_1RA.md, RESULTS_1RC.md, RESULTS_1RD.md)
    (CELL_LABEL["mini-low"], {"Silent": 33, "Sham": 33, "Anchor": 60, "Offer": 60}),
    (CELL_LABEL["4.1-low"], {"Silent": 33, "Anchor": 33, "Offer": 33}),
    (CELL_LABEL["4.1-high"], {"Silent": 33, "Offer": 33}),
    ("CEO group: competing seller\nadd-on, Study 1R-A, run 24 Oct", {"Silent": 33, "Competitive": 33}),
    ("mini group: price-only control\nadd-on, Study 1R-C, run 25 Oct", {"Silent": 33, "Silent-floor": 33}),
    ("CEO group: price-only control\nadd-on, Study 1R-C, run 25 Oct", {"Silent": 33, "Silent-floor": 33}),
    ("mini group: words-only test\nadd-on, Study 1R-D, run 25 Oct", {"Silent-floor": 60, "Offer-floor": 60}),
]
FIRST_ADDON_ROW = 3  # rows from here on are separate concurrent runs (1R-A, 1R-C, 1R-D)
ADDON_STARTS = (3, 4, 6)  # a dotted line above each separate run
RC_KEY = "primary (Silent-floor minus Silent, change score; Holm family of two)"


def n_table(ax) -> None:
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(N_TABLE) + 1.6)
    x_label, xs = 0.05, [4.3 + i * 0.88 for i in range(len(ARMS))]
    top = len(N_TABLE) + 0.6
    ax.text(x_label, top, "Group", fontsize=7.3, weight="bold", color=INK, va="center")
    for x, a in zip(xs, ARMS):
        ax.text(x, top, a.replace("-floor", "-\nfloor").replace("Competitive", "Compe-\ntitive"), fontsize=6.6,
                weight="bold", color=INK,
                ha="center", va="center", linespacing=1.0)
    ax.plot([0, 10], [top - 0.45] * 2, color=INK2, lw=0.6)
    for i, (cell, ns) in enumerate(N_TABLE):
        y = top - 1 - i
        if i in ADDON_STARTS:
            ax.plot([0, 10], [y + 0.5] * 2, color=INK2, lw=0.5, ls=(0, (2, 2)))
        ax.text(x_label, y, cell, fontsize=7.0, color=INK, va="center", linespacing=1.1)
        for x, a in zip(xs, ARMS):
            ax.text(x, y, str(ns[a]) if a in ns else "–", fontsize=7.3, color=INK if a in ns else INK2,
                    ha="center", va="center")
    ax.plot([0, 10], [top - 0.5 - len(N_TABLE)] * 2, color=INK2, lw=0.6)


def figure2(out: Path) -> None:
    fig = plt.figure(figsize=(5.5, 5.5), dpi=300, facecolor=SURFACE)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.6, 1.3], width_ratios=[1, 1.05], left=0.02, right=0.98, top=0.98,
                          bottom=0.02, hspace=0.12, wspace=0.08)
    ax_m, ax_t, ax_n = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, :])
    for a in (ax_m, ax_n):
        a.set_facecolor(SURFACE)
    P.market(ax_m)
    P.timeline(ax_t)
    pos = ax_t.get_position()
    ax_t.set_position([pos.x0 + 0.02, pos.y0 + 0.07, pos.width - 0.03, pos.height - 0.07])
    n_table(ax_n)
    for a, t in ((ax_m, "a"), (ax_t, "b"), (ax_n, "c")):
        a.text(-0.03 if a is ax_t else 0.0, 1.0, t, transform=a.transAxes, fontsize=9, weight="bold", color=INK,
               va="top", ha="right" if a is ax_t else "left")
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)


def contrasts() -> list[dict]:
    rows = P.contrasts()
    for r in rows:                                      # relabel cells (human message 90); values unchanged
        for code, short in CELL_SHORT.items():
            if r["label"].startswith(code + " "):
                r["label"] = f"{short}: " + r["label"][len(code) + 1:]
        r["label"] = r["label"].replace(" (talking sting)", "")
    rc = json.loads((REPO / "results/study1r_addon_C/analysis/results_1rc.json").read_text(encoding="utf-8"))[RC_KEY]
    for cell in ("mini-low", "4.1-high"):
        d = rc[cell]
        rows.append({"label": f"{CELL_SHORT[cell]}: Silent-floor {MINUS} Silent", "estimate": d["estimate"],
                     "ci": [d["ci_low"], d["ci_high"]], "n": [d["n_a"], d["n_b"]], "p_holm": d["p_holm"],
                     "status": "add-on C"})
    return rows


STATUS = {"primary": ("Primary", P.BLUE, "o"), "secondary": ("Secondary (Holm family of five)", P.ORANGE, "s"),
          "add-on": ("Add-on: competing seller", P.GREEN, "D"), "add-on C": ("Add-on: price-only control", YELLOW, "^"),
          "add-on D": ("Add-on: words-only test (separate panel)", "#e87ba4", "v")}
ROW_STATUS = {"primary": "primary", "secondary": "secondary", "add-on": "competing seller",
              "add-on C": "price-only control"}


MAGENTA = "#e87ba4"  # categorical slot 5 (slots 1-5 validated, light mode; every row also labeled in text)
RD_JSON = REPO / "results" / "study1r_addon_D" / "analysis_cell_a" / "results_1rd.json"
RD_KEY = "primary, Cell A (mini-low): Offer-floor minus Silent-floor (words effect)"


def contrast_1rd() -> dict | None:
    """Study 1R-D Cell A primary contrast (concurrent arms), or None before the analysis exists."""
    if not RD_JSON.is_file():
        return None
    d = json.loads(RD_JSON.read_text(encoding="utf-8"))[RD_KEY]
    return {"label": f"{CELL_SHORT['mini-low']}: Offer-floor {MINUS} Silent-floor", "estimate": d["estimate"],
            "ci": [d["ci_low"], d["ci_high"]], "n": [d["n_a"], d["n_b"]], "p_permutation": d["p_permutation"],
            "status": "add-on D"}


def figure4(rows: list[dict], out: Path, rd: dict | None = None) -> None:
    if rd is None:
        fig, ax = plt.subplots(figsize=(5.5, 3.9), dpi=300, facecolor=SURFACE)
    else:
        fig = plt.figure(figsize=(5.5, 5.5), dpi=300, facecolor=SURFACE)
        gs = fig.add_gridspec(2, 1, height_ratios=[4.6, 1.0], hspace=0.55)
        ax, ax2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    ax.set_facecolor(SURFACE)
    ys, y = [], 0.0
    for i, d in enumerate(rows):                       # top to bottom; a gap before each new run
        if i and d["status"] != rows[i - 1]["status"] and d["status"].startswith("add-on"):
            y -= 0.4
        ys.append(y)
        y -= 1.0
    for yy, d in zip(ys, rows):
        _, color, marker = STATUS[d["status"]]
        ax.plot(d["ci"], [yy, yy], color=color, lw=1.6, solid_capstyle="round", zorder=2)
        ax.plot([d["estimate"]], [yy], marker=marker, ms=6, color=color, mec=SURFACE, mew=1.0, zorder=3)
        ax.text(1.62, yy, f"{P.num(d['estimate'])} ({P.num(d['ci'][0])}, {P.num(d['ci'][1])})", fontsize=7.3,
                color=INK, va="center", ha="left")
    for i in range(1, len(rows)):
        if rows[i]["status"] != rows[i - 1]["status"] and rows[i]["status"].startswith("add-on"):
            ax.axhline((ys[i] + ys[i - 1]) / 2, color=INK2, lw=0.5, ls=(0, (2, 2)))
    ax.axvline(0, color=INK, lw=0.8, zorder=1)
    ax.set_yticks(ys)
    ax.set_yticklabels([f"{d['label']}\n{ROW_STATUS[d['status']]}, n = {d['n'][0]} vs {d['n'][1]}" for d in rows],
                       fontsize=7.3, color=INK)
    for t in ax.get_yticklabels():
        t.set_linespacing(1.25)
    ax.set_xlim(-1.0, 1.6)
    ax.set_ylim(ys[-1] - 0.7, ys[0] + 0.7)
    ticks = [-1.0, -0.5, 0, 0.5, 1.0, 1.5]
    ax.set_xticks(ticks)
    ax.set_xticklabels([P.num(v) if v else "0" for v in ticks])
    ax.text(1.62, ys[0] + 0.62, "Estimate (95% CI)", fontsize=7.3, color=INK2, va="bottom")
    ax.set_xlabel("Difference in change score, $ (bootstrap 95% CI)", fontsize=7.5, color=INK)
    axes = [ax]
    if rd is not None:
        axes.append(ax2)
        ax2.set_facecolor(SURFACE)
        _, color, marker = STATUS["add-on D"]
        ax2.plot(rd["ci"], [0, 0], color=color, lw=1.6, solid_capstyle="round", zorder=2)
        ax2.plot([rd["estimate"]], [0], marker=marker, ms=6, color=color, mec=SURFACE, mew=1.0, zorder=3)
        ax2.text(1.62, 0, f"{P.num(rd['estimate'])} ({P.num(rd['ci'][0])}, {P.num(rd['ci'][1])})", fontsize=7.3,
                 color=INK, va="center", ha="left")
        ax2.axvline(0, color=INK, lw=0.8, zorder=1)
        ax2.set_yticks([0])
        ax2.set_yticklabels([f"{rd['label']}\nwords-only test, n = {rd['n'][0]} vs {rd['n'][1]}"],
                            fontsize=7.3, color=INK)
        ax2.get_yticklabels()[0].set_linespacing(1.25)
        ax2.set_xlim(-1.0, 1.6)
        ax2.set_ylim(-0.8, 0.8)
        ax2.set_xticks(ticks)
        ax2.set_xticklabels([P.num(v) if v else "0" for v in ticks])
        ax2.set_title("Words-only test (separate concurrent run; mini group only)",
                      fontsize=7.3, color=INK,
                      loc="left", pad=4)
        ax2.set_xlabel("Difference in change score, $ (bootstrap 95% CI)", fontsize=7.5, color=INK)
    for a_ in axes:
        for s in ("top", "right", "left"):
            a_.spines[s].set_visible(False)
        a_.spines["bottom"].set_color(INK2)
        a_.tick_params(axis="x", colors=INK2, labelsize=7)
        a_.tick_params(axis="y", length=0)
        a_.xaxis.grid(True, color=GRID, lw=0.5)
        a_.set_axisbelow(True)
    shown = {k: v for k, v in STATUS.items() if k != "add-on D" or rd is not None}
    handles = [Line2D([], [], color=c, marker=m, lw=0, ms=5, mec=SURFACE, label=n) for n, c, m in shown.values()]
    leg = fig.legend(handles=handles, loc="lower center", ncol=2, fontsize=7, frameon=False, title="Preregistered:",
                     title_fontsize=7, bbox_to_anchor=(0.5, 0.0), handlelength=1.0, columnspacing=1.2)
    leg.get_title().set_color(INK)
    for t in leg.get_texts():
        t.set_color(INK)
    fig.subplots_adjust(left=0.37, right=0.78, top=0.95, bottom=0.22 if rd is None else 0.2)
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)


PROPENSITY_JSON = REPO / "results" / "study1r" / "exploratory" / "final_part2" / "part2.json"


def figure1(results: dict, out: Path) -> dict:
    """Figure 1: scripts/study1r_figures.py figure1 (same data, bars and CIs) with the cell labels of human message 90,
    no study code in the title, and per cell a horizontal marker at the share of Silent-arm episodes priced above
    $92.70 ("sting-free propensity"; part2.json reference standard: 1/33, 0/33, 33/33)."""
    import numpy as np
    from matplotlib.patches import Patch
    fig_data = results["Judge comparison figure (exploratory: v1-read, v2-read, human-confirmed, behavioral)"]
    prop = json.loads(PROPENSITY_JSON.read_text(encoding="utf-8"))["a_audit_error_rates"]["reference_standard"]
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=300, facecolor=D.SURFACE)
    D.style(ax)
    width, gap = 0.19, 0.012
    cells = [c for c, _ in D.CELLS]
    for j, (key, _) in enumerate(D.MEASURES):
        for i, cell in enumerate(cells):
            d = fig_data[cell][key]
            x = i + (j - 1.5) * (width + gap)
            if not d["n"]:
                ax.text(x, 0.07, "not\ncoded", ha="center", va="bottom", fontsize=6.5, color=D.INK2)
                continue
            lo, hi = d["ci"]
            ax.bar(x, d["rate"], width, color=D.SERIES[j], edgecolor=D.SURFACE, linewidth=1.0, zorder=2)
            ax.errorbar(x, d["rate"], yerr=[[d["rate"] - lo], [hi - d["rate"]]], fmt="none", ecolor=D.INK2,
                        elinewidth=0.8, capsize=2, zorder=3)
            ax.text(x, hi + 0.02, f"{d['k']}/{d['n']}", ha="center", va="bottom", fontsize=6.5, color=D.INK)
    half = 2 * (width + gap)
    for i, cell in enumerate(cells):
        sp = prop[cell]["silent_propensity"]
        ax.plot([i - half, i + half], [sp["share"]] * 2, color=D.INK, lw=1.2, ls=(0, (4, 2)), zorder=4)
    ax.set_xticks(range(len(cells)))
    ax.set_xticklabels([CELL_LABEL[c].replace(" (", "\n(") + "\nsting-free propensity: "
                        f"{prop[c]['silent_propensity']['k']}/{prop[c]['silent_propensity']['n']}" for c in cells],
                       fontsize=8.5, color=D.INK)
    ax.set_ylim(0, 1.12)
    ax.set_yticks(np.linspace(0, 1, 6))
    ax.set_ylabel("Share of Offer episodes", fontsize=9.5, color=D.INK)
    leg = ax.legend(handles=[Patch(color=D.SERIES[j], label=lab) for j, (_, lab) in enumerate(D.MEASURES)]
                    + [Line2D([], [], color=D.INK, lw=1.2, ls=(0, (4, 2)), label="Sting-free propensity")],
                    loc="lower left", ncol=5, fontsize=7.5, frameon=False, bbox_to_anchor=(0, 1.0),
                    handlelength=1.4, columnspacing=1.0, borderaxespad=0.2)
    for t in leg.get_texts():
        t.set_color(D.INK)
    fig.tight_layout()
    fig.savefig(out, dpi=300, facecolor=D.SURFACE)
    plt.close(fig)
    return {"bars": fig_data, "sting_free_propensity": {c: prop[c]["silent_propensity"] for c in cells}}


def figure_e1(paths: dict, out: Path) -> dict:
    """Appendix Figure E1 (price paths in the CEO group): scripts/study1r_figures.py figure2 (same data and seeds) with
    no in-image title (human message 93)."""
    orig = D.plt.Axes.set_title

    def set_title(self, label, *a, **k):
        if label == "Price paths in 4.1-high by confirmed acceptance (Study 1R, exploratory)":
            label = ""
        return orig(self, label, *a, **k)

    D.plt.Axes.set_title = set_title
    try:
        return D.figure2(paths, out)
    finally:
        D.plt.Axes.set_title = orig


def main() -> None:
    out, cy = Path(sys.argv[1]), Path(sys.argv[2])
    logs = [Path(p) for p in sys.argv[3].split(",") if p]
    out.mkdir(parents=True, exist_ok=True)
    results = json.loads((REPO / "results" / "study1r" / "results.json").read_text(encoding="utf-8"))["results"]
    f1 = figure1(results, out / "fig1_headline_comparison.png")
    figure2(out / "fig2_design_schematic.png")
    paths = D.episode_paths(cy, logs, Path(sys.argv[4]), Path(sys.argv[5]))
    (out / "appendix").mkdir(exist_ok=True)
    e1 = figure_e1(paths, out / "appendix" / "figE1_price_paths.png")
    rows = contrasts()
    rd = contrast_1rd()
    figure4(rows, out / "fig3_forest_contrasts.png", rd)
    data = {"label": "final figures (numbering of human message 93: 1 headline, 2 design, 3 forest plot; appendix E1 "
                     "price paths); facts as in the draft figure data",
            "fig1_headline": f1, "fig2_n_table": {cell: ns for cell, ns in N_TABLE}, "fig3_forest": rows,
            "fig3_study1rd_panel": rd, "figE1_price_paths": e1,
            "excluded_episodes": [e["replicate_id"] for e in paths["excluded"]]}
    (out / "figure_data.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps({"figE1_n": {g: e1[g]["n"] for g in ("accept", "no_accept", "silent")}, "fig3": rows}, indent=1))


if __name__ == "__main__":
    main()
