# Study 1R-A results (preregistered add-on)

Preregistered in `prereg_study1r/PREREG.md` section 14, frozen at `a1a7dd6`; run approved in human message 71. Facts and numbers only.

## Run

- Campaign `configs/study1r_addon_A/campaign.yaml`, cell 4.1-high, arms Competitive and Silent (concurrent fresh run), indices 0-32, budget group study1r_addon_A.
- Campaign logs: `20261024T184841Z_study1r_addon_A_9b61e6`, `20261024T185208Z_study1r_addon_A_a5e459`, `20261024T191057Z_study1r_addon_A_02149c`, `20261024T192936Z_study1r_addon_A_fb636f`, `20261024T194540Z_study1r_addon_A_003f61`.
- Episodes analysed: 66 (33 per arm); excluded: 0 (no episode failed; no replacements).
- Health: `results/study1r_addon_A/health/CHECKPOINT_blocks_0-32.md` (no stop condition at any checkpoint). Cost $66.1173 (cap $76.49).
- Analysis: `scripts/study1r_results_completed.py` (D-116 wrapper) calling the frozen `scripts/study1r_results.py` on the add-on campaign logs only; full output `results/study1r_addon_A/analysis/RESULTS.md` and `results.json` (main-study analyses there are skipped: no main-study arms in the input).

## Disruption test (preregistered add-on; Competitive minus Silent, change score)

Rule: supported only if the bootstrap 95% CI (10,000 resamples, seed 20261025) lies entirely below zero.

| Estimate | 95% CI | Bootstrap p | n Competitive | n Silent | CI excludes zero | Verdict |
|---|---|---|---|---|---|---|
| -0.5442 | -0.8677, -0.1876 | 0.0052 | 33 | 33 | True | supported |

## Propensity per arm (preregistered add-on, secondary; share of episodes above $92.70, Wilson 95% CI)

| Arm | Propensity |
|---|---|
| competitive | 31/33 = 0.939 (95% CI 0.804, 0.983) |
| silent | 32/33 = 0.970 (95% CI 0.847, 0.995) |

## Probe measures (preregistered add-on; awareness probe Q2, unit: seller)

| Arm | Sellers | YES | Unparseable | Rate (95% CI) |
|---|---|---|---|---|
| 4.1-high/competitive | 66 | 66 | 0 | 1.000 (0.945, 1.000) |
| 4.1-high/silent | 66 | 66 | 0 | 1.000 (0.945, 1.000) |

## Raw output of the frozen add-on section

```json
{
 "disruption": {
  "estimate": -0.5442499999999997,
  "ci_low": -0.867655492424244,
  "ci_high": -0.18760511363636204,
  "level": 0.95,
  "p_bootstrap": 0.0052,
  "n_a": 33,
  "n_b": 33,
  "excludes_zero": true,
  "verdict": "supported"
 },
 "propensity": {
  "competitive": {
   "k": 31,
   "n": 33,
   "rate": 0.9393939393939394,
   "ci": [
    0.8039375519135219,
    0.9832191169128082
   ]
  },
  "silent": {
   "k": 32,
   "n": 33,
   "rate": 0.9696969696969697,
   "ci": [
    0.846812746178811,
    0.9946305894631283
   ]
  }
 }
}
```
