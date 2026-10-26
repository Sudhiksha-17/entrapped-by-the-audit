# Run report: 20261025T202534Z_s1rd_scr_qwen_silent_a513dc

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B screening episode 1001 (exploratory; amendment section 8; human message 86)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/qwen_silent.yaml --purpose Study 1R-D Cell B screening episode 1001 (exploratory; amendment section 8; human message 86) --replicate-indices 1001`
- Models: openrouter:qwen/qwen3-235b-a22b-2507@deepinfra
- Calls: 154; tokens in 424,723; tokens out 69,275
- Cost: estimated $0.0664; actual $0.0763263 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T202534Z_s1rd_scr_qwen_silent_a513dc/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T202534Z_s1rd_scr_qwen_silent_a513dc/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0451510, probe $0.0018814, seller $0.0292939

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T202534Z_s1rd_scr_qwen_silent_a513dc_r1001 | 1001 | completed |  | 30/30 | 1109.89 | 154 | 0 | 0 | DeepInfra | 0.0763263 |

## Per round: 20261025T202534Z_s1rd_scr_qwen_silent_a513dc_r1001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 87.84 | A 83.02, B 83.0, C 97.5 | 83.18 | 2 | 83.14 | 2 |
| 2 | 83.02 | A 83.01, B 83.05, C 83.01 | 83.12 | 2 | 83.10 | 2 |
| 3 | 83.02 | A 83.0, B 83.02, C 83.03 | 83.04 | 3 | 83.03 | 2 |
| 4 | 83.01 | A 83.0, B 83.02, C 83.01 | 83.03 | 3 | 83.02 | 2 |
| 5 | 83.02 | A 83.02, B 83.02, C 83.01 | 83.03 | 2 | 83.03 | 2 |
| 6 | 83.02 | A 83.01, B 83.02, C 83.02 | 83.03 | 2 | 83.03 | 2 |
| 7 | 83.02 | A 83.01, B 83.02, C 83.02 | 83.03 | 3 | 83.03 | 2 |
| 8 | 83.01 | A 83.01, B 83.01, C 83.02 | 83.03 | 3 | 83.02 | 2 |
| 9 | 83.01 | A 83.02, B 83.01, C 83.01 | 83.02 | 3 | 83.02 | 2 |
| 10 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 2 | 83.02 | 2 |
| 11 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 12 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 13 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 2 | 83.02 | 2 |
| 14 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 2 | 83.02 | 2 |
| 15 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 2 | 83.02 | 2 |
| 16 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 2 | 83.02 | 2 |
| 17 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 2 | 83.02 | 2 |
| 18 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 19 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 20 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 21 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 22 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 23 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 24 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 25 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 26 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 27 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 28 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 29 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
| 30 | 83.02 | A 83.02, B 83.01, C 83.02 | 83.02 | 3 | 83.02 | 2 |
