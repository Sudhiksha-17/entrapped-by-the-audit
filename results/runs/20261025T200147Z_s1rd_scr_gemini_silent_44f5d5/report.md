# Run report: 20261025T200147Z_s1rd_scr_gemini_silent_44f5d5

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B screening, pilot episode (exploratory, index 1000; amendment section 8; human message 86)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/gemini_silent.yaml --purpose Study 1R-D Cell B screening, pilot episode (exploratory, index 1000; amendment section 8; human message 86) --replicate-indices 1000`
- Models: openrouter:google/gemini-2.5-flash-lite@google-ai-studio
- Calls: 178; tokens in 433,732; tokens out 94,197
- Cost: estimated $0.0619; actual $0.0778080 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T200147Z_s1rd_scr_gemini_silent_44f5d5/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T200147Z_s1rd_scr_gemini_silent_44f5d5/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 3
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0421807, probe $0.0019400, seller $0.0336873

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T200147Z_s1rd_scr_gemini_silent_44f5d5_r1000 | 1000 | completed |  | 30/30 | 120.27 | 178 | 3 | 0 | Google AI Studio | 0.0778080 |

## Per round: 20261025T200147Z_s1rd_scr_gemini_silent_44f5d5_r1000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 87.83 | A 82.5, B 83.5, C 97.5 | 83.00 | 1 | 83.00 | 0 |
| 2 | 83.12 | A 83.25, B 83.1, C 83.0 | 83.25 | 2 | 83.34 | 1 |
| 3 | 83.06 | A 83.0, B 83.0, C 83.17 | 83.33 | 2 | 83.25 | 1 |
| 4 | 82.88 | A 82.75, B 82.9, C 83.0 | 83.39 | 3 | 83.14 | 2 |
| 5 | 82.74 | A 82.5, B 82.9, C 82.83 | 83.75 | 3 | 83.25 | 2 |
| 6 | 82.57 | A 82.25, B 82.75, C 82.7 | 83.75 | 2 | 83.11 | 2 |
| 7 | 82.17 | A 81.5, B 82.5, C 82.5 | 83.12 | 2 | 82.56 | 2 |
| 8 | 82.00 | A 81.5, B 82.5, C 82.0 | 82.77 | 3 | 82.38 | 2 |
| 9 | 81.92 | A 81.5, B 82.25, C 82.0 | 82.50 | 2 | 82.38 | 2 |
| 10 | 81.69 | B 81.5, C 81.88 | 82.63 | 2 | 82.19 | 2 |
| 11 | 81.53 | A 81.6, B 81.5, C 81.5 | 82.97 | 3 | 82.25 | 2 |
| 12 | 81.85 | A 81.5, B 82.5, C 81.55 | 83.17 | 3 | 82.51 | 2 |
| 13 | 81.67 | A 81.0, B 82.0, C 82.0 | 82.62 | 2 | 82.06 | 2 |
| 14 | 81.25 | A 80.5, B 81.75, C 81.5 | 82.25 | 3 | 81.75 | 2 |
| 15 | 80.97 | A 80.25, B 81.55, C 81.12 | 82.12 | 2 | 81.41 | 2 |
| 16 | 80.72 | A 79.75, B 81.5, C 80.9 | 81.62 | 2 | 80.97 | 2 |
| 17 | 80.21 | A 79.0, B 81.0, C 80.62 | 81.88 | 2 | 80.84 | 2 |
| 18 | 79.92 | A 79.0, B 80.75, C 80.0 | 82.05 | 3 | 80.98 | 2 |
| 19 | 79.79 | A 79.0, B 80.5, C 79.88 | 81.33 | 3 | 80.56 | 2 |
| 20 | 80.17 | A 80.5, B 80.25, C 79.75 | 81.00 | 2 | 80.50 | 2 |
| 21 | 80.13 | A 80.0, B 80.0, C 80.38 | 80.12 | 1 | 80.62 | 2 |
| 22 | 80.00 | A 80.0, B 80.0, C 80.0 | 80.33 | 2 | 80.38 | 2 |
| 23 | 79.92 | A 79.75, B 80.0, C 80.0 | 80.46 | 3 | 80.19 | 2 |
| 24 | 79.46 | A 79.5, B 79.0, C 79.88 | 80.45 | 2 | 79.85 | 2 |
| 25 | 78.42 | A 79.0, B 77.0, C 79.25 | 80.33 | 2 | 79.16 | 2 |
| 26 | 77.67 | A 78.0, B 77.0, C 78.0 | 79.80 | 3 | 78.73 | 2 |
| 27 | 77.17 | A 77.0, B 77.0, C 77.5 | 79.77 | 3 | 78.47 | 2 |
| 28 | 76.83 | A 76.5, B 77.0, C 77.0 | 81.33 | 3 | 79.08 | 2 |
| 29 | 76.17 | A 75.0, B 76.75, C 76.75 | 84.77 | 3 | 80.47 | 2 |
| 30 | 74.13 | A 70.0, B 76.5, C 75.88 | 79.88 | 2 | 76.41 | 1 |
