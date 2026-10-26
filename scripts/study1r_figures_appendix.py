"""Appendix figures (human message 86, Part 6; labels of human message 90). No API calls; no new analyses.

E2 `figE2_audit_error_rates.png` (was A1): flagged share of Offer episodes by reader and group, Wilson 95% CIs, with the group's
   sting-free propensity (Silent-arm share above $92.70) as a dashed marker (data: part2.json, section (a)).
E3 `figE3_time_to_acceptance.png` (was A2): Kaplan-Meier time-to-event curves, shown as the cumulative share of Offer episodes
   that reached each event by the number of asks (1 - S(t)), for the volume and CEO cells (data: part2.json, (b)).
E4 `figE4_one_episode.png` (was A3): one episode (the seller fixed in notes/ANALYSIS_PLACEMENT.md, Part 1): per-round posted
   asks of Seller A, Seller B and Seller C, the offered level X, the seller's first human-confirmed acceptance round,
   and the Plan B window with both labelers' Plan B labels (committed coding, D-139).

Usage: python scripts/study1r_figures_appendix.py <out_dir>
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from sting.stage2_measures import rounds_of  # noqa: E402

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
BLUE, ORANGE, GREEN, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
CELL_LABEL = {"mini-low": "mini group (gpt-4.1-mini, default)", "4.1-low": "volume group (gpt-4.1, volume prompt)",
              "4.1-high": "CEO group (gpt-4.1, CEO prompt)"}
P2 = REPO / "results" / "study1r" / "exploratory" / "final_part2" / "part2.json"
EPISODE = "20261024T074633Z_study1r_4.1-high_offer_d8a720_r014"   # notes/ANALYSIS_PLACEMENT.md (Part 1)
SELLER, FIRST_CONFIRMED = "Seller B", 26
plt.rcParams.update({"font.family": "DejaVu Sans"})


def style(ax) -> None:
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
    ax.tick_params(colors=INK2, labelsize=7)
    ax.yaxis.grid(True, color=GRID, lw=0.5)
    ax.set_axisbelow(True)


def fig_a1(p2: dict, out: Path) -> dict:
    a = p2["a_audit_error_rates"]
    readers = [("judge v1", BLUE, "o"), ("judge v2 screener", ORANGE, "s"), ("human-confirmed", GREEN, "D")]
    cells = list(CELL_LABEL)
    fig, ax = plt.subplots(figsize=(5.5, 3.6), dpi=300, facecolor=SURFACE)
    style(ax)
    for i, c in enumerate(cells):
        for j, (r, col, mk) in enumerate(readers):
            d = a["cells"][c][r]
            x = i + (j - 1) * 0.22
            if not d.get("n"):
                ax.text(x + 0.04, 0.16, "human:\nnot coded", ha="center", va="bottom", fontsize=6, color=INK2)
                continue
            ax.plot([x, x], d["ci"], color=col, lw=1.6, solid_capstyle="round", zorder=2)
            ax.plot([x], [d["share"]], marker=mk, ms=5.5, color=col, mec=SURFACE, mew=1.0, zorder=3)
            ax.text(x + 0.05, d["share"], f"{d['k']}/{d['n']}", fontsize=6, color=INK, va="center", zorder=4,
                    bbox={"boxstyle": "square,pad=0.1", "fc": SURFACE, "ec": "none"})
        sp = a["reference_standard"][c]["silent_propensity"]
        ax.plot([i - 0.36, i + 0.36], [sp["share"]] * 2, color=INK, lw=1.1, ls=(0, (4, 2)), zorder=1)
    ax.set_xticks(range(3))
    ax.set_xticklabels([CELL_LABEL[c].replace(" (", "\n(") + "\nsting-free propensity: "
                        f"{a['reference_standard'][c]['silent_propensity']['k']}/"
                        f"{a['reference_standard'][c]['silent_propensity']['n']}"
                        + ("\nno human labels; judge vs judge only" if c == "mini-low" else "") for c in cells],
                       fontsize=6.6, color=INK)
    ax.set_ylim(-0.02, 1.05)
    ax.set_ylabel("Share of Offer episodes flagged\n(Wilson 95% CI)", fontsize=7.5, color=INK)
    handles = [Line2D([], [], color=c, marker=m, lw=0, ms=5, label=r) for r, c, m in readers] + \
        [Line2D([], [], color=INK, lw=1.1, ls=(0, (4, 2)), label="sting-free propensity")]
    ax.legend(handles=handles, fontsize=6.8, frameon=False, loc="upper center", ncol=4, bbox_to_anchor=(0.5, -0.36))
    fig.subplots_adjust(left=0.13, right=0.97, top=0.97, bottom=0.36)
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)
    return a


def fig_a2(p2: dict, out: Path) -> dict:
    b = p2["b_time_to_acceptance"]["cells"]
    events = [("first human-confirmed acceptance", GREEN, "-"),
              ("first screener flag (accept or conditional_accept)", ORANGE, "--"),
              ("first detector engagement", BLUE, ":")]
    fig, axes = plt.subplots(1, 2, figsize=(5.5, 3.0), dpi=300, facecolor=SURFACE, sharey=True)
    data = {}
    for ax, c in zip(axes, ("4.1-low", "4.1-high")):
        style(ax)
        for ev, col, ls in events:
            cur = b[c][ev]["curve"]
            xs = [0] + [p["asks"] for p in cur]
            ys = [0.0] + [1 - p["survival"] for p in cur]
            ax.step(xs, ys, where="post", color=col, lw=1.5, ls=ls)
            data[f"{c}/{ev}"] = {"median_asks": b[c][ev]["median_asks"], "share_reaching": b[c][ev]["share_reaching"]}
        ax.axhline(0.5, color=INK2, lw=0.6, ls=(0, (1, 2)))
        ax.set_xlim(0, 20)
        ax.set_ylim(0, 1.02)
        ax.set_xticks([0, 5, 10, 15, 20])
        ax.set_xlabel("Asks (round minus 10)", fontsize=7.2, color=INK)
        ax.set_title(f"{CELL_LABEL[c]}, n = {b[c][events[0][0]]['n']}", fontsize=6.4, color=INK, loc="left")
    axes[0].set_ylabel("Share of Offer episodes\nthat reached the event", fontsize=7.2, color=INK)
    fig.legend(handles=[Line2D([], [], color=col, lw=1.5, ls=ls, label=ev) for ev, col, ls in events],
               loc="lower center", ncol=1, fontsize=6.6, frameon=False, bbox_to_anchor=(0.5, 0.0))
    fig.subplots_adjust(left=0.13, right=0.98, top=0.9, bottom=0.36, wspace=0.12)
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)
    return data


def plan_b_label(name: str) -> tuple[str, list[int]] | None:
    key = json.loads((REPO / "results/study1r/labeling_keys" / name / "labeling_key.json").read_text(encoding="utf-8"))
    rows = {r["item_id"]: r for r in csv.DictReader((REPO / "results/study1r/labeling" / name /
                                                    "labels_template.csv").open(encoding="utf-8"))}
    for iid, k in key.items():
        if k["replicate_id"] == EPISODE and k["seller"] == SELLER:
            return rows[iid]["response"], k["rounds"]
    return None


def fig_a3(out: Path) -> dict:
    rep = next((REPO / "runs" / "study1r").glob(f"*/{EPISODE}"))
    sl = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
    x = sl["x"]["x"]
    rounds = rounds_of(rep)
    series = {s: [(r["round_number"], r["seller_asks"].get(s)) for r in rounds] for s in ("Seller A", "Seller B", "Seller C")}
    la, lb = plan_b_label("plan_b"), plan_b_label("plan_b_labeler_b")
    window = (la or lb)[1]
    fig, ax = plt.subplots(figsize=(5.5, 3.2), dpi=300, facecolor=SURFACE)
    style(ax)
    ax.axvspan(window[0] - 0.5, window[-1] + 0.5, color=GRID, alpha=0.7, lw=0, zorder=0)
    for s, col, lw in (("Seller A", BLUE, 1.4), ("Seller B", ORANGE, 2.0), ("Seller C", INK2, 1.0)):
        pts = [(r, a) for r, a in series[s] if isinstance(a, (int, float))]
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=col, lw=lw,
                ls="-" if s != "Seller C" else (0, (3, 2)), label=s + (" (sting)" if s == "Seller C" else ""), zorder=2)
    ax.axhline(x, color=YELLOW, lw=1.2, ls=(0, (5, 2)), zorder=1)
    ax.text(1.2, x + 0.04, f"offered level X = ${x:.2f}", fontsize=6.5, color=INK, va="bottom")
    ax.axvline(10, color=INK2, lw=0.7, ls=(0, (2, 2)))
    ax.text(10.2, ax.get_ylim()[0], "first offer\n(round 10)", fontsize=6, color=INK2, va="bottom")
    ax.axvline(FIRST_CONFIRMED, color=ORANGE, lw=0.9, ls=(0, (1, 1)))
    lo, hi = ax.get_ylim()
    ax.set_ylim(lo, hi + 0.3)
    ylim = ax.get_ylim()
    labels = f"Plan B, {SELLER}'s private notes, rounds {window[0]}-{window[-1]}:\n" \
             f"Labeler A: {la[0] if la else 'n/a'}; Labeler B: {lb[0] if lb else 'not in subset'}"
    ax.text(11, ylim[1] - 0.02, labels, fontsize=6.2, color=INK, ha="left", va="top")
    ax.text(FIRST_CONFIRMED - 0.7, ylim[0] + 0.02, f"{SELLER}: first human-confirmed\nacceptance (round {FIRST_CONFIRMED})",
            fontsize=6, color=INK, va="bottom", ha="right")
    ax.set_xlim(1, 30)
    ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax.set_xlabel("Round", fontsize=7.5, color=INK)
    ax.set_ylabel("Posted ask ($)", fontsize=7.5, color=INK)
    ax.legend(fontsize=6.6, frameon=False, loc="upper center", ncol=3, bbox_to_anchor=(0.5, -0.2))
    fig.subplots_adjust(left=0.11, right=0.98, top=0.97, bottom=0.27)
    fig.savefig(out, dpi=300, facecolor=SURFACE)
    plt.close(fig)
    return {"episode": EPISODE, "seller": SELLER, "x": x, "first_confirmed_round": FIRST_CONFIRMED,
            "plan_b_window": window, "plan_b_labeler_a": la[0] if la else None, "plan_b_labeler_b": lb[0] if lb else None,
            "asks": series}


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    p2 = json.loads(P2.read_text(encoding="utf-8"))
    data = {"label": "appendix figures (exploratory, post hoc); data from part2.json, the run logs and the committed "
                     "Plan B coding", "E2": fig_a1(p2, out / "figE2_audit_error_rates.png"),
            "E3": fig_a2(p2, out / "figE3_time_to_acceptance.png"), "E4": fig_a3(out / "figE4_one_episode.png")}
    (out / "appendix_figure_data.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main()
