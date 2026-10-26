# Plan B: private-plan sincerity (EXPLORATORY, post hoc, descriptive)

Plan `notes/EXPLORATORY_PLAN_B_C.md` section B (committed `1e32de1` before any text was seen); D-126. Coding: Labeler A (34 items) and Labeler B (random 50% subset, 17 items), blind sheets; file hashes in D-139. No tests. Script `scripts/study1r_plan_b_results.py`. Facts only.

## 1. Label counts (Labeler A)

| Group / cell | N | honor | defect | mixed | not_mentioned |
|---|---|---|---|---|---|
| accepting/4.1-low | 3 | 0 | 1 | 2 | 0 |
| accepting/4.1-high | 14 | 8 | 0 | 5 | 1 |
| accepting/pooled | 17 | 8 | 1 | 7 | 1 |
| control/4.1-low | 3 | 0 | 3 | 0 | 0 |
| control/4.1-high | 14 | 0 | 7 | 0 | 7 |
| control/pooled | 17 | 0 | 10 | 0 | 7 |

## 2. Change score and behavioral flag by label (Labeler A)

Change score: episode level (post rounds 11-30 minus pre rounds 6-9, LLM sellers), mean with percentile bootstrap 95% CI over sellers (10,000 resamples, seed 20261025). Both sellers of an episode share its change score and flag, so N sellers can exceed N episodes. Flag: change >= 0.5 x (X - pre).

| Group / label | N sellers | N episodes | Mean change (95% CI) | Behavioral flag |
|---|---|---|---|---|
| accepting/honor | 8 | 7 | +0.448 (+0.195, +0.792) | 1/8 |
| accepting/defect | 1 | 1 | -1.239 (-1.239, -1.239) | 0/1 |
| accepting/mixed | 7 | 5 | -1.102 (-2.634, -0.022) | 0/7 |
| accepting/not_mentioned | 1 | 1 | +0.139 (+0.139, +0.139) | 0/1 |
| control/honor | 0 | 0 | n/a | 0/0 |
| control/defect | 10 | 10 | -0.100 (-0.169, -0.027) | 0/10 |
| control/mixed | 0 | 0 | n/a | 0/0 |
| control/not_mentioned | 7 | 6 | -0.727 (-1.198, -0.320) | 0/7 |

## 3. Agreement, Labeler A vs Labeler B (overlapping items)

Items: Labeler A 34, Labeler B 17, overlap 17 (matched by replicate id and seller; groups in the overlap {'control': 9, 'accepting': 8}). Raw agreement 0.471; Cohen's kappa 0.292 (95% CI 0.068, 0.560; percentile bootstrap over items, 10,000 resamples, seed 20261025).

| Labeler A \ Labeler B | honor | defect | mixed | not_mentioned |
|---|---|---|---|---|
| honor | 1 | 0 | 3 | 0 |
| defect | 0 | 5 | 0 | 0 |
| mixed | 0 | 1 | 2 | 0 |
| not_mentioned | 1 | 4 | 0 | 0 |
