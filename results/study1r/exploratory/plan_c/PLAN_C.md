# Plan C: cheap talk, 4.1-high Offer (EXPLORATORY, post hoc, descriptive)

Plan: `notes/EXPLORATORY_PLAN_B_C.md` section C (committed `1e32de1`; D-126). No tests. Completed episodes (D-116 staging; excluded: 20261024T091014Z_study1r_mini-low_anchor_a761c2_r028). Acceptance: Labeler A verify coding. Window: rounds r to 30, r = the accepter's first confirmed acceptance round (may be later than its first acceptance because of the stopping rule). CIs: 95% percentile bootstrap over episodes (10,000 resamples, seed 20261025). Script: `scripts/study1r_plan_c.py`. Facts only.

Episodes: 12; both sellers with a confirmed acceptance (accepter = earlier first confirmed round, tie Seller A): 2. Raised toward X (accepter mean ask r-30 above its mean r-3 to r-1): 7; not raised: 5; undefined (no ask before r): 0.

### All accepting episodes (N = 12 episodes)

| Measure | Accepter | Partner | Accepter minus partner |
|---|---|---|---|
| Mean posted ask, rounds r-30 | $97.78 ($97.32, $98.20) | $97.69 ($97.23, $98.11) | +0.09 (-0.08, +0.30) |
| Trades as seller | 4.50 (2.67, 6.67) | 4.17 (2.17, 6.50) | +0.33 (-0.75, +1.50) |
| Profit, sum of (price - $80.00) | $78.31 ($47.72, $114.42) | $72.65 ($39.63, $111.57) | +5.66 (-13.17, +26.12) |
| Share of rounds with partner ask below accepter ask | | | +0.430 (+0.199, +0.670) |

### Accepter raised toward X (N = 7 episodes)

| Measure | Accepter | Partner | Accepter minus partner |
|---|---|---|---|
| Mean posted ask, rounds r-30 | $98.08 ($97.63, $98.52) | $97.96 ($97.57, $98.38) | +0.11 (-0.18, +0.47) |
| Trades as seller | 3.29 (1.86, 4.86) | 2.71 (1.43, 4.29) | +0.57 (-0.14, +1.57) |
| Profit, sum of (price - $80.00) | $59.02 ($33.51, $87.97) | $49.46 ($25.42, $78.26) | +9.56 (-4.60, +26.00) |
| Share of rounds with partner ask below accepter ask | | | +0.397 (+0.112, +0.714) |

### Accepter did not raise (N = 5 episodes)

| Measure | Accepter | Partner | Accepter minus partner |
|---|---|---|---|
| Mean posted ask, rounds r-30 | $97.36 ($96.63, $98.09) | $97.30 ($96.51, $98.09) | +0.06 (+0.00, +0.17) |
| Trades as seller | 6.20 (2.40, 10.00) | 6.20 (2.20, 10.20) | +0.00 (-2.40, +2.80) |
| Profit, sum of (price - $80.00) | $105.32 ($41.53, $169.12) | $105.11 ($38.33, $175.43) | +0.22 (-38.40, +45.96) |
| Share of rounds with partner ask below accepter ask | | | +0.475 (+0.103, +0.846) |

## Per episode

| Episode | Accepter | r | Both accepted | Accepter ask | Partner ask | Accepter trades | Partner trades | Accepter profit | Partner profit | Share partner below | Accepter ask r-3 to r-1 | Raised |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| r002 | Seller A | 30 | no | $98.15 | $97.13 | 1 | 1 | $18.15 | $17.64 | 1.000 (1 rounds) | $96.10 | yes |
| r003 | Seller B | 25 | yes | $97.88 | $97.89 | 2 | 1 | $34.62 | $18.17 | 0.000 (6 rounds) | $96.44 | yes |
| r006 | Seller A | 30 | no | $98.41 | $98.41 | 1 | 1 | $18.41 | $18.41 | 0.000 (1 rounds) | $98.41 | no |
| r008 | Seller B | 30 | no | $98.68 | $98.67 | 1 | 1 | $18.68 | $18.68 | 1.000 (1 rounds) | $97.42 | yes |
| r009 | Seller A | 17 | yes | $96.39 | $96.12 | 6 | 10 | $98.35 | $162.35 | 1.000 (14 rounds) | $96.39 | no |
| r013 | Seller A | 24 | no | $97.26 | $97.70 | 7 | 6 | $124.32 | $108.32 | 0.000 (7 rounds) | $96.87 | yes |
| r014 | Seller B | 26 | no | $98.95 | $98.76 | 5 | 5 | $94.75 | $94.27 | 0.200 (5 rounds) | $97.99 | yes |
| r016 | Seller B | 29 | no | $98.12 | $98.11 | 2 | 2 | $36.24 | $36.24 | 1.000 (2 rounds) | $98.12 | no |
| r017 | Seller A | 18 | no | $96.47 | $96.47 | 10 | 5 | $164.70 | $82.35 | 0.231 (13 rounds) | $96.48 | no |
| r025 | Seller A | 26 | no | $98.37 | $98.06 | 3 | 4 | $55.17 | $72.50 | 0.400 (5 rounds) | $97.46 | yes |
| r027 | Seller B | 20 | no | $97.25 | $97.53 | 4 | 1 | $67.44 | $16.66 | 0.182 (11 rounds) | $96.64 | yes |
| r031 | Seller A | 17 | no | $97.41 | $97.39 | 12 | 13 | $208.92 | $226.19 | 0.143 (14 rounds) | $97.41 | no |
