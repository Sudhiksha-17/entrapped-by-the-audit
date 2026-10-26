# Run report: 20261025T204603Z_s1rd_scr_qwen_offer_check_5c8651

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B manipulation check, 1 Offer-floor episode on the chosen model (exploratory; prices not reported or used; amendment section 8.6)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/qwen_offer_check.yaml --purpose Study 1R-D Cell B manipulation check, 1 Offer-floor episode on the chosen model (exploratory; prices not reported or used; amendment section 8.6) --replicate-indices 1000`
- Models: openrouter:qwen/qwen3-235b-a22b-2507@deepinfra
- Calls: 157; tokens in 417,184; tokens out 70,525
- Cost: estimated $0.0664; actual $0.0763353 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T204603Z_s1rd_scr_qwen_offer_check_5c8651/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T204603Z_s1rd_scr_qwen_offer_check_5c8651/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0443682, probe $0.0019147, seller $0.0300524

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T204603Z_s1rd_scr_qwen_offer_check_5c8651_r1000 | 1000 | completed |  | 30/30 | 1172.61 | 157 | 0 | 0 | DeepInfra | 0.0763353 |

## Per round: 20261025T204603Z_s1rd_scr_qwen_offer_check_5c8651_r1000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 87.77 | A 83.01, B 82.8, C 97.5 | 87.34 | 1 | 89.59 | 2 |
| 2 | 82.85 | A 82.83, B 82.81, C 82.91 | 83.00 | 3 | 82.92 | 2 |
| 3 | 82.86 | A 82.95, B 82.82, C 82.82 | 82.92 | 2 | 82.89 | 2 |
| 4 | 82.87 | A 82.88, B 82.84, C 82.88 | 82.91 | 2 | 82.90 | 2 |
| 5 | 82.88 | A 82.92, B 82.87, C 82.86 | 82.88 | 2 | 82.88 | 2 |
| 6 | 82.89 | A 82.9, B 82.87, C 82.9 | 82.90 | 1 | 82.90 | 2 |
| 7 | 82.89 | A 82.9, B 82.87, C 82.89 | 82.90 | 2 | 82.90 | 2 |
| 8 | 82.89 | A 82.89, B 82.89, C 82.89 | 82.91 | 3 | 82.90 | 2 |
| 9 | 82.89 | A 82.88, B 82.89, C 82.89 | 82.91 | 3 | 82.90 | 2 |
| 10 | 85.74 | A 82.88, B 82.89, C 91.44 | 82.91 | 2 | 82.90 | 3 |
| 11 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.91 | 2 | 82.91 | 3 |
| 12 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.89 | 2 | 82.91 | 3 |
| 13 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 14 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 15 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.90 | 2 | 82.91 | 3 |
| 16 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.90 | 2 | 82.91 | 3 |
| 17 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.91 | 2 | 82.91 | 3 |
| 18 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 19 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 20 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.91 | 2 | 82.91 | 3 |
| 21 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.91 | 2 | 82.91 | 3 |
| 22 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.91 | 2 | 82.91 | 3 |
| 23 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 24 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 25 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.91 | 2 | 82.91 | 3 |
| 26 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 27 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 28 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 29 | 85.74 | A 82.89, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 3 |
| 30 | 85.75 | A 82.92, B 82.89, C 91.44 | 82.92 | 2 | 82.91 | 2 |
