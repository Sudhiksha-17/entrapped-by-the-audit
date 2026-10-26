# Run report: 20261025T195837Z_study1r_addon_D_screening_kimi-k2-0905_silent_399aa1

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B screening, pilot episode (exploratory, index 1000; amendment section 8; human message 86)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/kimi-k2-0905_silent.yaml --purpose Study 1R-D Cell B screening, pilot episode (exploratory, index 1000; amendment section 8; human message 86) --replicate-indices 1000`
- Models: openrouter:moonshotai/kimi-k2-0905@novita
- Calls: 160; tokens in 391,803; tokens out 99,985
- Cost: estimated $0.3772; actual $0.4850443 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T195837Z_study1r_addon_D_screening_kimi-k2-0905_silent_399aa1/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T195837Z_study1r_addon_D_screening_kimi-k2-0905_silent_399aa1/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 2
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.2861629, probe $0.0116001, seller $0.1872813

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T195837Z_study1r_addon_D_screening_kimi-k2-0905_silent_399aa1_r1000 | 1000 | completed |  | 30/30 | 538.21 | 160 | 2 | 0 | Novita | 0.4850443 |

## Per round: 20261025T195837Z_study1r_addon_D_screening_kimi-k2-0905_silent_399aa1_r1000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 92.33 | A 83.5, B 96.0, C 97.5 | 82.91 | 0 |  | 2 |
| 2 | 85.58 | A 82.99, B 84.0, C 89.75 | 83.10 | 1 | 83.04 | 1 |
| 3 | 83.52 | A 83.55, B 83.5, C 83.5 | 83.42 | 1 | 83.75 | 2 |
| 4 | 83.43 | A 83.25, B 83.5, C 83.53 | 83.40 | 2 | 83.44 | 2 |
| 5 | 83.37 | A 83.37, B 83.35, C 83.38 | 83.51 | 3 | 83.44 | 2 |
| 6 | 83.40 | A 83.5, B 83.35, C 83.36 | 83.48 | 2 | 83.44 | 2 |
| 7 | 83.42 | A 83.42, B 83.41, C 83.42 | 83.46 | 3 | 83.44 | 2 |
| 8 | 83.46 | A 83.48, B 83.5, C 83.41 | 83.26 | 1 | 83.41 | 2 |
| 9 | 83.41 | A 83.39, B 83.35, C 83.49 | 83.47 | 2 | 83.42 | 1 |
| 10 | 83.42 | A 83.44, B 83.44, C 83.37 | 83.47 | 3 | 83.44 | 2 |
| 11 | 83.45 | A 83.42, B 83.5, C 83.44 | 83.42 | 2 | 83.44 | 2 |
| 12 | 83.41 | A 83.39, B 83.39, C 83.46 | 83.48 | 3 | 83.45 | 2 |
| 13 | 83.42 | A 83.38, B 83.5, C 83.39 | 83.43 | 2 | 83.41 | 2 |
| 14 | 83.41 | A 83.43, B 83.37, C 83.44 | 83.45 | 2 | 83.44 | 2 |
| 15 | 83.41 | A 83.43, B 83.39, C 83.4 | 83.44 | 3 | 83.42 | 2 |
| 16 | 83.44 | A 83.42, B 83.5, C 83.41 | 83.42 | 2 | 83.42 | 2 |
| 17 | 83.42 | A 83.4, B 83.4, C 83.46 | 83.43 | 2 | 83.42 | 2 |
| 18 | 83.41 | A 83.44, B 83.39, C 83.4 | 83.43 | 2 | 83.42 | 2 |
| 19 | 83.41 | A 83.41, B 83.41, C 83.41 | 83.43 | 3 | 83.42 | 2 |
| 20 | 83.45 | A 83.43, B 83.5, C 83.41 | 83.43 | 2 | 83.43 | 2 |
| 21 | 83.45 | A 83.43, B 83.46, C 83.47 | 83.43 | 1 | 83.43 | 2 |
| 22 | 83.45 | A 83.44, B 83.47, C 83.44 | 83.44 | 2 | 83.44 | 2 |
| 23 | 83.45 | A 83.44, B 83.45, C 83.45 | 83.45 | 2 | 83.45 | 2 |
| 24 | 83.44 | B 83.44, C 83.44 | 83.45 | 2 | 83.44 | 1 |
| 25 | 83.43 | A 83.43, B 83.43, C 83.44 | 83.44 | 2 | 83.44 | 2 |
| 26 | 83.43 | A 83.43, B 83.42, C 83.43 | 83.44 | 3 | 83.44 | 2 |
| 27 | 83.45 | A 83.43, B 83.5, C 83.43 | 83.44 | 2 | 83.44 | 2 |
| 28 | 83.47 | A 83.43, B 83.5, C 83.47 | 83.44 | 1 | 83.44 | 2 |
| 29 | 83.44 | A 83.43, B 83.43, C 83.47 | 83.45 | 2 | 83.44 | 2 |
| 30 | 83.43 | A 83.43, B 83.43, C 83.43 | 83.47 | 3 | 83.45 | 0 |
