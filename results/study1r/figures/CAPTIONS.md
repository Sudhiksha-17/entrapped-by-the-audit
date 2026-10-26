# Draft figure captions (Study 1R)

Facts only; draft wording for the paper. All figures are 300 dpi PNGs. Figures 1 and 4: `scripts/study1r_figures_paper.py` (5.5 in wide, for a text column). Figures 2 and 3: `scripts/study1r_figures.py` (7.2 in wide; numbered 1 and 2 before human message 77, images unchanged). Data behind the figures: `figure_data.json`.

## Figure 1. `fig1_methods_schematic.png` (methods; no title text in the image)

**Draft caption.** Study design. (a) The market: a continuous double auction (Agrawal et al., 2025; upstream code unmodified) with two LLM sellers (Seller A, Seller B), one scripted sting seller (Seller C) and three LLM buyers. Sellers post asks and buyers post bids. Seller messages go to a broadcast channel that only sellers read, delivered in the next round; buyers have no message channel. Seller cost $80, buyer value $100, 30 rounds. (b) Timeline: pre is the mean LLM-seller ask over rounds 6-9; Seller C's proposed price X is computed from pre at round 10 and fixed for the episode; in the message arms (Sham, Anchor, Offer) Seller C posts a message each round 10-29, visible to the LLM sellers in rounds 11-30; the outcome (change score) is the mean LLM-seller ask over rounds 11-30 minus pre. Silent and Competitive arms post no message. (c) Completed episodes analysed per cell and arm; the 4.1-high Study 1R-A row (preregistered add-on) is a separate concurrent run with its own Silent arm. One mini-low Anchor episode failed and was replaced as preregistered.

Sources: `prereg_study1r/PREREG.md` sections 3, 4, 6, 7 and 14; upstream `market.py` (seller messages passed to sellers only, from the previous round); `results/study1r/RESULTS.md` and `results/study1r/RESULTS_1RA.md` (N).

## Figure 2. `fig2_headline_comparison.png` (exploratory; was Figure 1)

**Draft caption.** Share of Offer episodes counted as accepting the sting offer, by measure and cell, in Study 1R. Judge v1: any seller-round labeled accept by the Study 1 judge (gpt-4.1-mini). Judge v2: any public message labeled accept or conditional_accept by judge v2 prompt r1 (gpt-4.1), used as the screener. Human-confirmed: inclusive acceptance (accept or conditional_accept) in the human-coded verification set, rounds 11-30 (option A; mini-low was not human-coded). Behavioral flag: preregistered behavioral acceptance flag. Bars show k/n episodes; error bars are Wilson 95% CIs. N = 60 Offer episodes in mini-low, 33 in 4.1-low and 33 in 4.1-high. Neither judge passed validation (gate G3), so judge readings are exploratory.

Values (k/n): mini-low 37/60, 2/60, not coded, 3/60; 4.1-low 5/33, 5/33, 2/33, 0/33; 4.1-high 32/33, 13/33, 12/33, 1/33 (judge v1, judge v2, human-confirmed, behavioral flag). Source: `results/study1r/results.json`, "Judge comparison figure".

## Figure 3. `fig3_price_paths_4.1-high.png` (exploratory, descriptive; layout provisionally approved, D-120; was Figure 2)

**Draft caption.** Mean ask of the two LLM sellers per round in the 4.1-high cell of Study 1R. Offer episodes are split by human-confirmed inclusive acceptance (12 with, 21 without), and Silent episodes are shown for reference (33). Lines are means over episodes; bands are 95% percentile bootstrap CIs over episodes (2,000 resamples). The shaded band marks the pre window (rounds 6-9) of the change score. The dashed line marks round 10, the first round of Seller C's proposal in the Offer arm. Seller C's proposed price X in Offer episodes: mean $98.37 (range $97.55 to $98.95).

Values: round 30 mean ask $97.92 (95% CI 97.42, 98.34) with confirmed acceptance; $96.47 (95.93, 96.92) without; $95.98 (95.59, 96.32) Silent. Means of the per-round means: rounds 6-9 $96.90, $96.65, $96.64; rounds 11-30 $97.15, $96.42, $96.32. Source: `figure_data.json`. The acceptance groups come from the frozen analysis' episode coding on completed episodes. Window changes from pre and X - pre per group: `results/study1r/NUMBERS_FOR_PAPER.md` section 5.

## Figure 4. `fig4_change_contrasts.png` (preregistered contrasts; forest plot)

**Draft caption.** Differences in the change score (mean LLM-seller ask over rounds 11-30 minus pre, in dollars) between arms, with bootstrap 95% CIs (10,000 resamples within arm, seed 20261025); the vertical line marks zero. Status: preregistered primary (mini-low Offer minus Anchor, T1); preregistered secondary, the Holm family of five (mini-low Offer minus Sham, Anchor minus Sham, Sham minus Silent; 4.1-low Offer minus Anchor; 4.1-high Offer minus Silent, the talking sting); preregistered add-on (4.1-high Competitive minus Silent, Study 1R-A, a separate concurrent run below the dotted line). n = completed episodes per arm.

Values (estimate, 95% CI; Holm-adjusted permutation p for the secondary family): T1 +0.23 (-0.18, +0.66); Offer - Sham +0.81 (+0.33, +1.27), p_Holm 0.013; Anchor - Sham +0.58 (+0.17, +0.97), p_Holm 0.031; Sham - Silent -0.12 (-0.52, +0.29), p_Holm 1.0; 4.1-low Offer - Anchor +0.07 (-0.48, +0.64), p_Holm 1.0; 4.1-high Offer - Silent +0.26 (+0.02, +0.50), p_Holm 0.112; Competitive - Silent -0.54 (-0.87, -0.19). Sources: `results/study1r/results.json` ("T1 primary", "T1 secondary, Holm family of five"); `results/study1r_addon_A/analysis/results.json` (disruption).

## Note (2026-10-25)

Final figures in the order of human message 82 (headline = Figure 1, schematic = Figure 2, price paths = Figure 3, forest plot = Figure 4) and their captions: `final/` (`final/CAPTIONS.md`). The draft figures and captions above are kept unchanged.
