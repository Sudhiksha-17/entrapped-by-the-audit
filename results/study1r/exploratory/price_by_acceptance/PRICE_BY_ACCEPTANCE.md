# Study 1R, 4.1-high: price levels by confirmed acceptance (exploratory, descriptive)

Human message 76. No tests. Completed episodes, frozen `build` episode records (D-116 staging; excluded: 20261024T091014Z_study1r_mini-low_anchor_a761c2_r028). Ask = round mean of posted LLM-seller asks. CIs: 95% percentile bootstrap over episodes (10,000 resamples, seed 20261025). Script: `scripts/study1r_price_by_acceptance.py`. Facts only.

## Per group

| Group | N | Pre, rounds 6-9 | Change from pre, rounds 11-20 | Change from pre, rounds 21-30 | X - pre |
|---|---|---|---|---|---|
| Offer, human-confirmed acceptance | 12 | $96.90 ($96.59, $97.21) | +0.08 (-0.07, +0.30) | +0.42 (+0.13, +0.77) | +1.55 (+1.39, +1.71) |
| Offer, no confirmed acceptance | 21 | $96.65 ($96.41, $96.87) | -0.18 (-0.32, -0.08) | -0.29 (-0.66, +0.01) | +1.68 (+1.57, +1.79) |
| Silent | 33 | $96.64 ($96.47, $96.81) | -0.16 (-0.26, -0.09) | -0.47 (-0.71, -0.26) | +1.68 (+1.59, +1.76) |

Pre from the fallback (most recent asks before round 10): Offer, human-confirmed acceptance 0; Offer, no confirmed acceptance 0; Silent 0.

## Accepting episodes: first confirmed acceptance

First round with a human-confirmed acceptance (N = 12): 17, 17, 18, 20, 24, 25, 26, 26, 29, 30, 30, 30.

Mean ask, 3 rounds before vs 3 rounds after (round itself excluded; N = 9): before $97.15 ($96.75, $97.56); after $97.54 ($97.01, $98.09); after minus before +0.39 (+0.04, +0.80). Episodes without an after window (first confirmed round 30, excluded from these means): 3; with an after window shorter than 3 rounds (clipped at round 30): 1.

Coding order caveat: the verify sheet was coded in shuffled order under the hidden stopping rule. Episodes in which a verification (screener-positive) message in a round before the first confirmed acceptance was dropped uncoded: 7 of 12.

| Episode | First confirmed round | Earliest verification round | Dropped verification rounds before it | Ask before | Ask after |
|---|---|---|---|---|---|
| r002 | 30 | 30 | none | $96.10 | n/a |
| r003 | 25 | 19 | 19, 24 | $96.45 | $98.17 |
| r006 | 30 | 26 | 26, 27, 28, 29 | $98.41 | n/a |
| r008 | 30 | 13 | 14 | $97.43 | n/a |
| r009 | 17 | 13 | 14, 15, 16 | $96.25 | $96.25 |
| r013 | 24 | 12 | none | $97.08 | $97.08 |
| r014 | 26 | 26 | none | $97.98 | $98.95 |
| r016 | 29 | 29 | none | $98.12 | $98.12 |
| r017 | 18 | 12 | 12 | $96.47 | $96.47 |
| r025 | 26 | 26 | none | $97.35 | $98.23 |
| r027 | 20 | 16 | 16, 17, 18, 19 | $97.39 | $97.22 |
| r031 | 17 | 16 | 16 | $97.24 | $97.39 |
