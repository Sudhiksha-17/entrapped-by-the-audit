# Run report: 20261025T200147Z_s1rd_scr_qwen_silent_f7f8a8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B screening, pilot episode (exploratory, index 1000; amendment section 8; human message 86)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/qwen_silent.yaml --purpose Study 1R-D Cell B screening, pilot episode (exploratory, index 1000; amendment section 8; human message 86) --replicate-indices 1000`
- Models: openrouter:qwen/qwen3-235b-a22b-2507@deepinfra
- Calls: 154; tokens in 416,502; tokens out 69,001
- Cost: estimated $0.0664; actual $0.0754357 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T200147Z_s1rd_scr_qwen_silent_f7f8a8/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T200147Z_s1rd_scr_qwen_silent_f7f8a8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0454110, probe $0.0017845, seller $0.0282402

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T200147Z_s1rd_scr_qwen_silent_f7f8a8_r1000 | 1000 | completed |  | 30/30 | 1408.98 | 154 | 0 | 0 | DeepInfra | 0.0754357 |

## Per round: 20261025T200147Z_s1rd_scr_qwen_silent_f7f8a8_r1000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 92.23 | A 96.38, B 82.8, C 97.5 | 82.82 | 1 | 82.81 | 2 |
| 2 | 85.08 | A 82.83, B 82.81, C 89.59 | 82.89 | 2 | 82.87 | 2 |
| 3 | 82.83 | A 82.84, B 82.82, C 82.82 | 82.98 | 2 | 82.94 | 2 |
| 4 | 82.83 | A 82.85, B 82.82, C 82.83 | 82.97 | 3 | 82.90 | 2 |
| 5 | 82.84 | A 82.87, B 82.83, C 82.83 | 82.95 | 2 | 82.91 | 2 |
| 6 | 82.86 | A 82.89, B 82.85, C 82.85 | 82.89 | 2 | 82.88 | 2 |
| 7 | 82.86 | A 82.87, B 82.85, C 82.87 | 82.91 | 3 | 82.89 | 2 |
| 8 | 82.87 | A 82.91, B 82.85, C 82.86 | 82.89 | 2 | 82.88 | 2 |
| 9 | 82.88 | A 82.89, B 82.87, C 82.88 | 82.89 | 2 | 82.88 | 2 |
| 10 | 82.88 | A 82.89, B 82.87, C 82.88 | 82.89 | 2 | 82.88 | 2 |
| 11 | 82.88 | A 82.89, B 82.87, C 82.88 | 82.89 | 2 | 82.88 | 2 |
| 12 | 82.88 | A 82.89, B 82.88, C 82.88 | 82.89 | 2 | 82.88 | 2 |
| 13 | 82.88 | A 82.87, B 82.88, C 82.88 | 82.89 | 3 | 82.88 | 2 |
| 14 | 82.88 | A 82.87, B 82.88, C 82.88 | 82.88 | 2 | 82.88 | 2 |
| 15 | 82.88 | A 82.87, B 82.88, C 82.88 | 82.89 | 3 | 82.88 | 2 |
| 16 | 82.88 | A 82.87, B 82.88, C 82.88 | 82.89 | 3 | 82.88 | 2 |
| 17 | 82.88 | A 82.87, B 82.88, C 82.88 | 82.89 | 3 | 82.88 | 2 |
| 18 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.89 | 3 | 82.88 | 2 |
| 19 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 20 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 21 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 22 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 23 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 24 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.87 | 2 | 82.88 | 2 |
| 25 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 26 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 27 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 28 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 29 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
| 30 | 82.88 | A 82.88, B 82.88, C 82.88 | 82.88 | 3 | 82.88 | 2 |
