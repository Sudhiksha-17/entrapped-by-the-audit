# Run report: 20261025T231643Z_s1rd_spd_parasail_3309e9

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_speedtest; run type: exploratory
- Purpose: Study 1R-D Cell B provider speed test (exploratory, index 2000; addendum 1; human message 88)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/speedtest/parasail_silent.yaml --purpose Study 1R-D Cell B provider speed test (exploratory, index 2000; addendum 1; human message 88) --replicate-indices 2000`
- Models: openrouter:qwen/qwen3-235b-a22b-2507@parasail
- Calls: 154; tokens in 410,962; tokens out 63,938
- Cost: estimated $0.0664; actual $0.0996059 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T231643Z_s1rd_spd_parasail_3309e9/manifest.json` (committed copy of `runs/study1r_addon_D_speedtest/20261025T231643Z_s1rd_spd_parasail_3309e9/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0590508, probe $0.0022295, seller $0.0383257

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T231643Z_s1rd_spd_parasail_3309e9_r2000 | 2000 | completed |  | 30/30 | 294.11 | 154 | 0 | 0 | Parasail | 0.0996059 |

## Per round: 20261025T231643Z_s1rd_spd_parasail_3309e9_r2000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 92.70 | A 97.49, B 83.1, C 97.5 | 82.89 | 0 |  | 2 |
| 2 | 85.50 | A 83.1, B 83.1, C 90.29 | 83.09 | 1 | 83.10 | 2 |
| 3 | 83.09 | A 83.09, B 83.09, C 83.1 | 83.10 | 3 | 83.10 | 2 |
| 4 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 2 | 83.09 | 2 |
| 5 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.10 | 3 | 83.09 | 2 |
| 6 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.10 | 3 | 83.09 | 2 |
| 7 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 8 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 9 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 10 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 11 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 2 | 83.09 | 2 |
| 12 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 13 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 14 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 15 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 16 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 17 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 18 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 19 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 20 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 21 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 2 | 83.09 | 2 |
| 22 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 23 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 24 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 25 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 26 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 27 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 28 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 29 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
| 30 | 83.09 | A 83.09, B 83.09, C 83.09 | 83.09 | 3 | 83.09 | 2 |
