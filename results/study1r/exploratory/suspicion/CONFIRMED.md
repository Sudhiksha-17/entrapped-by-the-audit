# Study 1R confirmed probe Q1 category (c) (exploratory, post hoc)

Human messages 74/75. Not preregistered. Confirmed (c): a keyword (c) hit in a seller's probe Q1 answer that the human coded real_suspicion on the blind Q1 check sheet (`results/study1r/labeling/suspicion_check_q1/labels_template.csv`). Same episodes and denominators as the keyword rates in SUSPICION.md (unit: LLM seller). Script: `scripts/study1r_suspicion_confirmed.py`. Facts only.

Coded items: 92 (34 real_suspicion, 58 false_positive).

## Per arm (Wilson 95% CI)

| Arm | Episodes | Keyword (c) | Coded real / false positive | Confirmed (c) |
|---|---|---|---|---|
| 4.1-high/offer | 33 | 14/66 = 0.212 (0.131, 0.325) | 6 / 8 | 6/66 = 0.091 (0.042, 0.184) |
| 4.1-low/offer | 33 | 13/66 = 0.197 (0.119, 0.308) | 6 / 7 | 6/66 = 0.091 (0.042, 0.184) |
| mini-low/offer | 60 | 2/120 = 0.017 (0.005, 0.059) | 0 / 2 | 0/120 = 0.000 (0.000, 0.031) |
| 4.1-high/silent | 33 | 16/66 = 0.242 (0.155, 0.358) | 6 / 10 | 6/66 = 0.091 (0.042, 0.184) |
| 4.1-low/anchor | 33 | 27/66 = 0.409 (0.299, 0.530) | 11 / 16 | 11/66 = 0.167 (0.096, 0.274) |
| 4.1-low/silent | 33 | 18/66 = 0.273 (0.180, 0.390) | 5 / 13 | 5/66 = 0.076 (0.033, 0.165) |
| mini-low/anchor | 60 | 1/120 = 0.008 (0.001, 0.046) | 0 / 1 | 0/120 = 0.000 (0.000, 0.031) |
| mini-low/sham | 33 | 1/66 = 0.015 (0.003, 0.081) | 0 / 1 | 0/66 = 0.000 (0.000, 0.055) |
| mini-low/silent | 33 | 0/66 = 0.000 (0.000, 0.055) | 0 / 0 | 0/66 = 0.000 (0.000, 0.055) |

## Offer minus Silent per cell (confirmed (c); seller-level rate difference; episode-cluster bootstrap 95% CI, 10,000 resamples, seed 20261025)

| Cell | Offer episodes | Silent episodes | Difference (95% CI) |
|---|---|---|---|
| mini-low | 60 | 33 | +0.000 (+0.000, +0.000) |
| 4.1-low | 33 | 33 | +0.015 (-0.076, +0.106) |
| 4.1-high | 33 | 33 | +0.000 (-0.106, +0.106) |
