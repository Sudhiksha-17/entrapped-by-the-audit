# Study 1R-C results (pricing-control add-on)

Preregistered add-on (prereg_study1r/AMENDMENT_1RC.md; lock prereg_study1r/FROZEN_1RC.json). Facts only. Completed episodes through the completed-episodes wrapper's staging. Script: `scripts/study1r_results_1rc.py`.

Excluded Study 1R-C episodes (status not completed): none. Excluded Study 1R main-study episodes (secondary only): 20261024T091014Z_study1r_mini-low_anchor_a761c2_r028.

## Primary (preregistered; Holm family of two): Silent-floor minus Silent, change score

Rule (amendment section 6.1): a pricing effect is reported as present in a cell only if the bootstrap 95% CI (10,000 resamples, seed 20261025) excludes zero and the Holm-adjusted permutation p (across the 2 cells) is below 0.05.

| Cell | Estimate | 95% CI | Permutation p (two-sided) | Holm p | n Silent-floor | n Silent | CI excludes zero | Pricing effect present |
|---|---|---|---|---|---|---|---|---|
| mini-low | +0.817 | +0.240, +1.467 | 0.0096 | 0.0192 | 33 | 33 | True | True |
| 4.1-high | +0.168 | -0.123, +0.413 | 0.2344 | 0.2344 | 33 | 33 | False | False |

## Stability check (preregistered, descriptive, non-concurrent): Study 1R-C Silent minus Study 1R main-study Silent, change score

Bootstrap 95% CI only; no test.

| Cell | Estimate | 95% CI | n 1R-C Silent | n main-study Silent |
|---|---|---|---|---|
| mini-low | -0.114 | -0.495, +0.271 | 33 | 33 |
| 4.1-high | -0.005 | -0.207, +0.198 | 33 | 33 |

## Secondary, descriptive, non-concurrent: Study 1R main-study arm minus Study 1R-C Silent-floor

Not concurrent (different campaigns and dates); bootstrap 95% CI only; no test.

| Contrast | Estimate | 95% CI | n main arm | n Silent-floor |
|---|---|---|---|---|
| mini-low Anchor minus Silent-floor | -0.246 | -0.908, +0.332 | 60 | 33 |
| mini-low Offer minus Silent-floor | -0.015 | -0.703, +0.609 | 60 | 33 |
| 4.1-high Offer minus Silent-floor | +0.097 | -0.179, +0.401 | 33 | 33 |

## Secondary: propensity per arm (Wilson 95% CI)

| Arm | above $92.70 | above $91.80 (sensitivity) | above $94.50 (sensitivity) |
|---|---|---|---|
| mini-low/silent_floor | 1/33 (0.005, 0.153) | 1/33 (0.005, 0.153) | 0/33 (0.000, 0.104) |
| mini-low/silent | 0/33 (0.000, 0.104) | 1/33 (0.005, 0.153) | 0/33 (0.000, 0.104) |
| 4.1-high/silent_floor | 32/33 (0.847, 0.995) | 32/33 (0.847, 0.995) | 31/33 (0.804, 0.983) |
| 4.1-high/silent | 32/33 (0.847, 0.995) | 32/33 (0.847, 0.995) | 32/33 (0.847, 0.995) |

## Descriptive per arm

| Arm | Episodes | Mean change (95% CI) | Mean X - pre | Seller C mean ask, rounds 11-30 | Floor binding (rounds 10-30) | G2 passed | Probe Q2 YES (sellers; Wilson CI) |
|---|---|---|---|---|---|---|---|
| mini-low/silent_floor | 33 | +0.880 (+0.369, +1.488) | 7.60 | $92.40 | 693/693 | 33/33 | 31/66 (0.354, 0.588); unparseable 0 |
| mini-low/silent | 33 | +0.063 (-0.190, +0.350) | 7.35 | $85.37 | 0/693 | 33/33 | 50/66 (0.642, 0.845); unparseable 0 |
| 4.1-high/silent_floor | 33 | -0.155 (-0.416, +0.035) | 1.79 | $98.21 | 689/693 | 33/33 | 66/66 (0.945, 1.000); unparseable 0 |
| 4.1-high/silent | 33 | -0.323 (-0.470, -0.197) | 1.72 | $96.25 | 0/693 | 33/33 | 66/66 (0.945, 1.000); unparseable 0 |
