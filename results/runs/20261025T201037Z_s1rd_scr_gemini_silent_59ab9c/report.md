# Run report: 20261025T201037Z_s1rd_scr_gemini_silent_59ab9c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B screening episodes 1001-1002 (exploratory; amendment section 8; human message 86)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/gemini_silent.yaml --purpose Study 1R-D Cell B screening episodes 1001-1002 (exploratory; amendment section 8; human message 86) --replicate-indices 1001,1002`
- Models: openrouter:google/gemini-2.5-flash-lite@google-ai-studio
- Calls: 160; tokens in 226,469; tokens out 79,323
- Cost: estimated $0.1238; actual $0.0542864 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T201037Z_s1rd_scr_gemini_silent_59ab9c/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T201037Z_s1rd_scr_gemini_silent_59ab9c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 0; failed 2; failures by reason: {'api_failure': 2}; parse failures: 2
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0298437, seller $0.0244427

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T201037Z_s1rd_scr_gemini_silent_59ab9c_r1001 | 1001 | failed | api_failure | 7/30 | 35.37 | 45 | 1 | 0 | Google AI Studio | 0.0158887 |
| 20261025T201037Z_s1rd_scr_gemini_silent_59ab9c_r1002 | 1002 | failed | api_failure | 16/30 | 73.44 | 115 | 1 | 0 | Google AI Studio | 0.0383977 |

## Per round: 20261025T201037Z_s1rd_scr_gemini_silent_59ab9c_r1001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 92.50 | A 85.0, B 95.0, C 97.5 | 87.20 | 1 | 90.00 | 0 |
| 2 | 89.83 | A 92.0, B 87.5, C 90.0 | 88.00 | 1 | 91.25 | 1 |
| 3 | 86.58 | A 87.0, B 83.0, C 89.75 | 88.13 | 2 | 87.72 | 2 |
| 4 | 85.17 | A 85.0, B 85.5, C 85.0 | 88.32 | 2 | 87.86 | 2 |
| 5 | 85.08 | A 84.0, B 86.0, C 85.25 | 87.75 | 2 | 87.38 | 2 |
| 6 | 84.50 | A 83.0, B 85.5, C 85.0 | 87.00 | 1 | 87.00 | 2 |
| 7 | 84.67 | A 84.0, B 85.75, C 84.25 | 87.25 | 1 | 87.75 | 2 |

## Per round: 20261025T201037Z_s1rd_scr_gemini_silent_59ab9c_r1002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 91.42 | A 81.75, B 95.0, C 97.5 | 80.17 | 1 | 83.62 | 1 |
| 2 | 89.96 | A 86.5, B 95.0, C 88.38 | 89.00 | 2 | 89.22 | 2 |
| 3 | 90.50 | A 85.75, B 95.0, C 90.75 | 90.33 | 2 | 90.38 | 2 |
| 4 | 88.54 | A 85.25, B 90.0, C 90.38 | 91.83 | 2 | 91.19 | 2 |
| 5 | 87.54 | A 85.0, B 90.0, C 87.62 | 94.17 | 3 | 90.85 | 2 |
| 6 | 88.00 | A 85.0, B 91.5, C 87.5 | 93.13 | 2 | 90.38 | 2 |
| 7 | 87.83 | A 85.25, B 90.0, C 88.25 | 91.83 | 3 | 89.83 | 2 |
| 8 | 87.62 | A 85.0, B 90.25, C 87.62 | 91.00 | 2 | 89.03 | 2 |
| 9 | 88.96 | A 89.75, B 89.5, C 87.62 | 88.75 | 1 | 88.69 | 2 |
| 10 | 89.32 | A 89.6, B 88.75, C 89.62 | 89.33 | 1 | 89.38 | 2 |
| 11 | 89.06 | A 89.0, B 89.0, C 89.17 | 89.75 | 2 | 89.62 | 2 |
| 12 | 88.88 | A 88.9, B 88.75, C 89.0 | 89.67 | 2 | 89.66 | 2 |
| 13 | 89.36 | A 90.5, B 88.75, C 88.83 | 90.33 | 2 | 89.90 | 2 |
| 14 | 89.29 | A 89.75, B 88.5, C 89.62 | 91.00 | 3 | 90.14 | 2 |
| 15 | 88.71 | A 89.0, B 88.0, C 89.12 | 92.00 | 3 | 90.35 | 2 |
| 16 | 88.83 | A 89.5, B 88.5, C 88.5 | 91.83 | 3 | 90.33 | 2 |
