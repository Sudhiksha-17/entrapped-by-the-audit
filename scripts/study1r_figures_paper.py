"""Study 1R paper figures 1 and 4 (human message 77; cosmetic and descriptive; no new tests or analyses). No API calls.

Figure 1, methods schematic: left, the market (2 LLM sellers, Seller C, 3 LLM buyers; the seller message channel
reaches sellers only and delivers the next round, upstream `market.py`); right, a timeline of rounds 1-30 (pre
rounds 6-9; Seller C's first message round 10; messages visible rounds 11-30; outcome window rounds 11-30); below, cells
x arms with N (completed episodes analysed; PREREG sections 4 and 14, RESULTS.md, RESULTS_1RA.md). No title text.

Figure 4, forest plot of change-score contrasts with 95% bootstrap CIs, read from results/study1r/results.json and
results/study1r_addon_A/analysis/results.json; each row labeled with its preregistered status (primary; secondary,
Holm family of five; preregistered add-on).

Sized for a 5.5 in text column (fonts 7-8.5 pt at 100%); 300 dpi. Light palette from the dataviz skill (validated
earlier for D-120): status is also encoded by marker shape and written on every row.

Usage: python scripts/study1r_figures_paper.py <out_dir>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
BLUE, ORANGE, GREEN = "#2a78d6", "#eb6834", "#1baf7a"
LLM_FILL, STING_FILL = "#e3eefb", "#fde6da"
MINUS = "−"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 7.5})

ARMS = ["Silent", "Sham", "Anchor", "Offer", "Competitive"]
N_TABLE = [  # PREREG section 4 (main) and 14 (add-on); completed episodes analysed (RESULTS.md, RESULTS_1RA.md)
    ("mini-low: gpt-4.1-mini, default prompt", {"Silent": 33, "Sham": 33, "Anchor": 60, "Offer": 60}),
    ("4.1-low: gpt-4.1, volume prompt", {"Silent": 33, "Anchor": 33, "Offer": 33}),
    ("4.1-high: gpt-4.1, CEO prompt", {"Silent": 33, "Offer": 33}),
    ("4.1-high, Study 1R-A (add-on)", {"Silent": 33, "Competitive": 33}),
]


def box(ax, x, y, w, h, text, fill, edge, fs=7.5, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.25", fc=fill, ec=edge, lw=0.9))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=INK, weight=weight)


def arrow(ax, x0, y0, x1, y1, both=False):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops={"arrowstyle": "<->" if both else "->", "color": INK2, "lw": 0.8, "shrinkA": 0, "shrinkB": 0})


def market(ax) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    # seller message channel (sellers only, next round)
    ax.add_patch(FancyBboxPatch((0.15, 1.0), 0.9, 8.4, boxstyle="round,pad=0.02,rounding_size=0.3", fc=GRID, ec=INK2,
                                lw=0.8))
    ax.text(0.6, 5.2, "Seller message channel\n(sellers only; next round)", rotation=90, ha="center", va="center",
            fontsize=7, color=INK)
    sellers = [(7.3, "Seller A\nLLM", LLM_FILL, BLUE), (4.5, "Seller B\nLLM", LLM_FILL, BLUE),
               (1.7, "Seller C\nscripted\nsting", STING_FILL, ORANGE)]
    for y, t, f, e in sellers:
        box(ax, 1.6, y, 2.4, 1.6, t, f, e)
        arrow(ax, 1.05, y + 0.8, 1.6, y + 0.8, both=True)
        arrow(ax, 4.0, y + 0.8, 4.75, y + 0.8)
    box(ax, 4.75, 1.7, 1.7, 7.2, "Double\nauction\n\nasks,\nbids,\ntrades", "#f3f2ef", INK2, fs=7.5)
    for y, t in [(7.3, "Buyer 1\nLLM"), (4.5, "Buyer 2\nLLM"), (1.7, "Buyer 3\nLLM")]:
        box(ax, 7.2, y, 2.4, 1.6, t, LLM_FILL, BLUE)
        arrow(ax, 7.2, y + 0.8, 6.45, y + 0.8)
    ax.text(4.37, 9.25, "asks", fontsize=7, color=INK2, ha="center")
    ax.text(6.83, 9.25, "bids", fontsize=7, color=INK2, ha="center")
    ax.text(0.15, 0.3, r"Sellers: cost \$80. Buyers: value \$100. 30 rounds.", fontsize=7, color=INK2)


def timeline(ax) -> None:
    ax.set_xlim(0.5, 30.5)
    ax.set_ylim(0, 10)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(INK2)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.set_yticks([])
    ax.set_xticks([1, 6, 10, 15, 20, 25, 30])
    ax.tick_params(axis="x", colors=INK2, labelsize=7, length=2.5)
    ax.set_xlabel("Round", fontsize=7.5, color=INK)
    ax.set_facecolor(SURFACE)
    for r in range(1, 31):
        ax.axvline(r, color=GRID, lw=0.4, zorder=0)
    rows = [  # (y, label, start, end, color, kind)
        (8.3, "pre: rounds 6-9 (X fixed at round 10)", 5.5, 9.5, INK2, "bar"),
        (6.1, "Seller C's first message: round 10", 10, 10, ORANGE, "point"),
        (3.9, "Seller C's messages visible: rounds 11-30", 10.5, 30.5, ORANGE, "bar"),
        (1.7, "Outcome window: rounds 11-30", 10.5, 30.5, BLUE, "bar"),
    ]
    for y, label, a, b, c, kind in rows:
        if kind == "bar":
            ax.add_patch(FancyBboxPatch((a, y - 0.45), b - a, 0.9, boxstyle="round,pad=0,rounding_size=0.2", fc=c,
                                        ec="none", alpha=0.85))
        else:
            ax.plot([a], [y], marker="D", ms=6, color=c, mec=SURFACE, mew=1.0)
        ax.text(1.0, y + 0.85, label, fontsize=7.3, color=INK, va="bottom")


def n_table(ax) -> None:
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(N_TABLE) + 1.6)
    x_label, xs = 0.05, [4.55 + i * 1.15 for i in range(len(ARMS))]
    top = len(N_TABLE) + 0.6
    ax.text(x_label, top, "Cell", fontsize=7.5, weight="bold", color=INK, va="center")
    for x, a in zip(xs, ARMS):
        ax.text(x, top, a, fontsize=7.5, weight="bold", color=INK, ha="center", va="center")
    ax.plot([0, 10], [top - 0.45] * 2, color=INK2, lw=0.6)
    for i, (cell, ns) in enumerate(N_TABLE):
        y = top - 1 - i
        if i == len(N_TABLE) - 1:
            ax.plot([0, 10], [y + 0.5] * 2, color=INK2, lw=0.5, ls=(0, (2, 2)))
        ax.text(x_label, y, cell, fontsize=7.5, color=INK, va="center")
        for x, a in zip(xs, ARMS):
            ax.text(x, y, str(ns[a]) if a in ns else "–", fontsize=7.5, color=INK if a in ns else INK2,
                    ha="center", va="center")
    ax.plot([0, 10], [top - 0.5 - len(N_TABLE)] * 2, color=INK2, lw=0.6)


def figure1(out: Path) -> None:
    fig = plt.figure(figsize=(5.5, 4.4), dpi=300, facecolor=SURFACE)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.6, 1], width_ratios=[1, 1.05], left=0.02, right=0.98, top=0.98,
                          bottom=0.02, hspace=0.12, wspace=0.08)
    ax_m = fig.add_subplot(gs[0, 0])
    ax_t = fig.add_subplot(gs[0, 1])
    ax_n = fig.add_subplot(gs[1, :])
    for a in (ax_m, ax_n):
        a.set_facecolor(SURFACE)
    market(ax_m)
    timeline(ax_t)
    pos = ax_t.get_position()
    ax_t.set_position([pos.x0 + 0.02, pos.y0 + 0.07, pos.width - 0.03, pos.height - 0.07])
    n_table(ax_n)
    for a, t in ((ax_m, "a"), (ax_t, "b"), (ax_n, "c")):
        a.text(-0.03 if a is ax_t else 0.0, 1.0, t, transform=a.transAxes, fontsize=9, weight="bold", color=INK,
               va="top", ha="right" if a is ax_t else "left")
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)


def contrasts() -> list[dict]:
    r = json.loads((REPO / "results/study1r/results.json").read_text(encoding="utf-8"))["results"]
    holm = r["T1 secondary, Holm family of five (permutation p)"]
    add = json.loads((REPO / "results/study1r_addon_A/analysis/results.json").read_text(encoding="utf-8"))["results"]
    add = add["Study 1R-A add-on (preregistered; run only on the entrant's approval)"]["disruption"]
    rows = [(f"mini-low Offer {MINUS} Anchor (T1)", r["T1 primary (mini-low Offer minus Anchor, change score)"],
             "primary"),
            (f"mini-low Offer {MINUS} Sham", holm["mini-low Offer minus Sham"], "secondary"),
            (f"mini-low Anchor {MINUS} Sham", holm["mini-low Anchor minus Sham"], "secondary"),
            (f"mini-low Sham {MINUS} Silent", holm["mini-low Sham minus Silent"], "secondary"),
            (f"4.1-low Offer {MINUS} Anchor", holm["4.1-low Offer minus Anchor (secondary T1)"], "secondary"),
            (f"4.1-high Offer {MINUS} Silent (talking sting)", holm["4.1-high Offer minus Silent (disruption)"],
             "secondary"),
            (f"4.1-high Competitive {MINUS} Silent", add, "add-on")]
    return [{"label": l, "estimate": d["estimate"], "ci": [d["ci_low"], d["ci_high"]], "n": [d["n_a"], d["n_b"]],
             "p_holm": d.get("p_holm"), "status": s} for l, d, s in rows]


STATUS = {"primary": ("Primary", BLUE, "o"), "secondary": ("Secondary (Holm family of five)", ORANGE, "s"),
          "add-on": ("Add-on (Study 1R-A)", GREEN, "D")}
ROW_STATUS = {"primary": "primary", "secondary": "secondary", "add-on": "add-on, Study 1R-A"}


def num(v: float) -> str:
    return f"{v:+.2f}".replace("-", MINUS)


def figure4(rows: list[dict], out: Path) -> None:
    fig, ax = plt.subplots(figsize=(5.5, 3.3), dpi=300, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    ys = list(range(len(rows)))[::-1]
    ys = [y + (0.4 if i < len(rows) - 1 else 0) for i, y in enumerate(ys)]
    for y, d in zip(ys, rows):
        name, color, marker = STATUS[d["status"]]
        ax.plot(d["ci"], [y, y], color=color, lw=1.6, solid_capstyle="round", zorder=2)
        ax.plot([d["estimate"]], [y], marker=marker, ms=6, color=color, mec=SURFACE, mew=1.0, zorder=3)
        ax.text(1.62, y, f"{num(d['estimate'])} ({num(d['ci'][0])}, {num(d['ci'][1])})", fontsize=7.3, color=INK,
                va="center", ha="left")
    ax.axvline(0, color=INK, lw=0.8, zorder=1)
    ax.axhline((ys[-1] + ys[-2]) / 2, color=INK2, lw=0.5, ls=(0, (2, 2)))
    ax.set_yticks(ys)
    ax.set_yticklabels([f"{d['label']}\n{ROW_STATUS[d['status']]}, n ={d['n'][0]} vs {d['n'][1]}" for d in rows], fontsize=7.3,
                       color=INK)
    for t, d in zip(ax.get_yticklabels(), rows):
        t.set_linespacing(1.25)
    ax.set_xlim(-1.0, 1.6)
    ax.set_ylim(ys[-1] - 0.7, ys[0] + 0.7)
    ax.set_xticks([-1.0, -0.5, 0, 0.5, 1.0, 1.5])
    ax.set_xticklabels([num(v) if v else "0" for v in [-1.0, -0.5, 0, 0.5, 1.0, 1.5]])
    ax.text(1.62, ys[0] + 0.62, "Estimate (95% CI)", fontsize=7.3, color=INK2, va="bottom")
    ax.set_xlabel("Difference in change score, $ (bootstrap 95% CI)", fontsize=7.5, color=INK)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(INK2)
    ax.tick_params(axis="x", colors=INK2, labelsize=7)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.grid(True, color=GRID, lw=0.5)
    ax.set_axisbelow(True)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], color=c, marker=m, lw=0, ms=5, mec=SURFACE, label=n) for n, c, m in STATUS.values()]
    leg = fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=7, frameon=False, title="Preregistered:",
                     title_fontsize=7, bbox_to_anchor=(0.5, 0.0), handlelength=1.0, columnspacing=1.2)
    leg.get_title().set_color(INK)
    for t in leg.get_texts():
        t.set_color(INK)
    fig.subplots_adjust(left=0.37, right=0.78, top=0.94, bottom=0.24)
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    figure1(out / "fig1_methods_schematic.png")
    rows = contrasts()
    figure4(rows, out / "fig4_change_contrasts.png")
    data_path = out / "figure_data.json"
    data = json.loads(data_path.read_text(encoding="utf-8")) if data_path.is_file() else {}
    data["fig1_n_table"] = {cell: ns for cell, ns in N_TABLE}
    data["fig4"] = rows
    data_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
