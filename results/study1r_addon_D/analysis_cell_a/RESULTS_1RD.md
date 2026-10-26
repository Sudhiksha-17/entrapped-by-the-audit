# Study 1R-D results (words with pricing held fixed)

Preregistered add-on (prereg_study1r/AMENDMENT_1RD.md; lock prereg_study1r/FROZEN_1RD.json). Facts only. Completed episodes through the completed-episodes wrapper's staging. Script: `scripts/study1r_results_1rd.py`.

Excluded Study 1R-D episodes (status not completed): 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r022, 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r032. Excluded Study 1R-C episodes (stability only): none.

## Primary (change score; bootstrap 95% CI, 10,000 resamples, seed 20261025; two-sided permutation p)

Rule (amendment section 6): Cell A, an effect is present only if the CI excludes zero; Cell B, only if the CI excludes zero and the Holm-adjusted p (within Cell B) is below 0.05.

| Test | Estimate | 95% CI | Permutation p | Holm p | n | CI excludes zero | Effect present |
|---|---|---|---|---|---|---|---|
| Cell A (mini-low): Offer-floor minus Silent-floor | +0.041 | -0.436, +0.481 | 0.8660 | n/a | 60 vs 60 | False | False |
| qwen: Offer-floor minus Silent-floor (words effect) | skipped: arm missing | | | | | | |
| qwen: Silent-floor minus Silent (price effect) | skipped: arm missing | | | | | | |

## Stability (descriptive, non-concurrent): Cell A Silent-floor minus Study 1R-C mini-low Silent-floor

-0.228 (95% CI -0.935, +0.422), n 60 vs 33.

## Secondary: propensity per arm (Wilson 95% CI)

| Arm | above $92.70 | above $91.80 | above $94.50 |
|---|---|---|---|
| mini-low/offer_floor | 3/60 (0.017, 0.137) | 4/60 (0.026, 0.159) | 1/60 (0.003, 0.089) |
| mini-low/silent_floor | 5/60 (0.036, 0.181) | 5/60 (0.036, 0.181) | 4/60 (0.026, 0.159) |

## Descriptive per arm (the Cell B Silent row is the Cell B Silent baseline)

| Arm | Episodes | Mean change (95% CI) | Mean post | Mean X - pre | Seller C mean ask, rounds 11-30 | Floor binding | G2 passed | Probe Q2 YES (sellers; Wilson) |
|---|---|---|---|---|---|---|---|---|
| mini-low/offer_floor | 60 | +0.693 (+0.446, +0.957) | $85.70 | 7.50 | $92.50 | 1260/1260 | 60/60 | 86/120 (0.630, 0.790) |
| mini-low/silent_floor | 60 | +0.651 (+0.322, +1.048) | $86.48 | 7.08 | $92.92 | 1260/1260 | 60/60 | 58/120 (0.396, 0.572) |
