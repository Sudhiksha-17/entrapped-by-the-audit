# Run report: 20261025T201037Z_s1rd_scr_kimi_silent_49e3e7

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_screening; run type: exploratory
- Purpose: Study 1R-D Cell B screening episodes 1001-1002 (exploratory; amendment section 8; human message 86)
- Command: `python -m sting.minimal_runner configs/study1r_addon_D/screening/kimi_silent.yaml --purpose Study 1R-D Cell B screening episodes 1001-1002 (exploratory; amendment section 8; human message 86) --replicate-indices 1001,1002`
- Models: openrouter:moonshotai/kimi-k2-0905@novita
- Calls: 323; tokens in 775,838; tokens out 219,789
- Cost: estimated $0.7544; actual $1.0149753 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T201037Z_s1rd_scr_kimi_silent_49e3e7/manifest.json` (committed copy of `runs/study1r_addon_D_screening/20261025T201037Z_s1rd_scr_kimi_silent_49e3e7/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 2; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.5832624, probe $0.0233800, seller $0.4083329

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T201037Z_s1rd_scr_kimi_silent_49e3e7_r1001 | 1001 | completed |  | 30/30 | 1555.14 | 160 | 0 | 0 | Novita | 0.5227465 |
| 20261025T201037Z_s1rd_scr_kimi_silent_49e3e7_r1002 | 1002 | completed |  | 30/30 | 1281.21 | 163 | 0 | 0 | Novita | 0.4922288 |

## Per round: 20261025T201037Z_s1rd_scr_kimi_silent_49e3e7_r1001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 89.67 | A 86.5, B 85.0, C 97.5 | 85.67 | 1 | 87.50 | 2 |
| 2 | 85.75 | A 84.5, B 87.0, C 85.75 | 85.83 | 1 | 86.00 | 2 |
| 3 | 85.75 | A 85.5, B 86.0, C 85.75 | 86.00 | 3 | 85.88 | 2 |
| 4 | 85.88 | B 86.0, C 85.75 | 86.50 | 2 | 86.19 | 2 |
| 5 | 86.42 | A 86.75, B 86.75, C 85.75 | 86.58 | 2 | 86.50 | 2 |
| 6 | 86.50 | A 86.5, B 86.25, C 86.75 | 86.75 | 3 | 86.62 | 2 |
| 7 | 86.31 | B 86.25, C 86.38 | 86.42 | 2 | 86.47 | 2 |
| 8 | 86.31 | B 86.25, C 86.38 | 86.42 | 2 | 86.47 | 2 |
| 9 | 86.31 | B 86.25, C 86.38 | 86.58 | 2 | 86.53 | 2 |
| 10 | 86.42 | A 86.5, B 86.38, C 86.38 | 86.67 | 3 | 86.54 | 2 |
| 11 | 86.41 | B 86.38, C 86.44 | 86.67 | 2 | 86.58 | 2 |
| 12 | 86.56 | A 86.75, B 86.5, C 86.44 | 86.69 | 2 | 86.61 | 2 |
| 13 | 86.60 | A 86.61, B 86.56, C 86.62 | 86.70 | 2 | 86.67 | 2 |
| 14 | 86.60 | A 86.61, B 86.6, C 86.59 | 86.71 | 3 | 86.65 | 2 |
| 15 | 86.65 | A 86.75, B 86.59, C 86.6 | 86.72 | 2 | 86.67 | 2 |
| 16 | 86.66 | A 86.66, B 86.65, C 86.67 | 86.73 | 3 | 86.69 | 2 |
| 17 | 86.66 | B 86.66, C 86.66 | 86.75 | 2 | 86.72 | 2 |
| 18 | 86.71 | A 86.75, B 86.72, C 86.66 | 86.75 | 2 | 86.72 | 2 |
| 19 | 86.73 | A 86.74, B 86.73, C 86.73 | 86.77 | 3 | 86.75 | 2 |
| 20 | 86.78 | A 86.8, B 86.8, C 86.73 | 86.78 | 1 | 86.77 | 2 |
| 21 | 86.79 | A 86.78, B 86.78, C 86.8 | 86.80 | 2 | 86.80 | 2 |
| 22 | 86.79 | A 86.79, B 86.79, C 86.78 | 86.80 | 3 | 86.80 | 2 |
| 23 | 86.83 | A 86.85, B 86.85, C 86.79 | 86.80 | 1 | 86.80 | 2 |
| 24 | 86.83 | A 86.82, B 86.81, C 86.85 | 86.84 | 2 | 86.83 | 2 |
| 25 | 86.82 | A 86.83, B 86.82, C 86.81 | 86.85 | 3 | 86.84 | 2 |
| 26 | 86.86 | A 86.9, B 86.85, C 86.82 | 86.85 | 2 | 86.85 | 2 |
| 27 | 86.91 | A 86.95, B 86.9, C 86.88 | 86.88 | 1 | 86.88 | 2 |
| 28 | 86.94 | A 86.94, B 86.95, C 86.93 | 86.91 | 0 |  | 2 |
| 29 | 86.94 | A 86.93, B 86.96, C 86.94 | 86.93 | 1 | 86.94 | 2 |
| 30 | 86.94 | A 86.94, B 86.93, C 86.94 | 86.94 | 3 | 86.94 | 0 |

## Per round: 20261025T201037Z_s1rd_scr_kimi_silent_49e3e7_r1002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 89.67 | A 84.5, B 87.0, C 97.5 | 87.83 | 1 | 90.50 | 2 |
| 2 | 85.92 | A 86.5, B 85.5, C 85.75 | 86.16 | 2 | 86.19 | 2 |
| 3 | 85.83 | A 85.5, B 86.0, C 86.0 | 86.41 | 3 | 86.12 | 2 |
| 4 | 85.50 | A 85.0, B 85.75, C 85.75 | 86.00 | 2 | 85.69 | 2 |
| 5 | 85.38 | A 85.5, B 85.25, C 85.38 | 85.35 | 2 | 85.48 | 2 |
| 6 | 85.44 | B 85.5, C 85.38 | 85.45 | 2 | 85.50 | 2 |
| 7 | 85.50 | A 85.5, C 85.5 | 85.50 | 2 | 85.50 | 2 |
| 8 | 85.58 | A 85.75, B 85.5, C 85.5 | 85.50 | 2 | 85.50 | 2 |
| 9 | 85.54 | A 85.5, B 85.5, C 85.62 | 85.59 | 2 | 85.56 | 2 |
| 10 | 85.58 | A 85.75, B 85.5, C 85.5 | 85.59 | 2 | 85.56 | 2 |
| 11 | 85.66 | A 85.62, B 85.75, C 85.62 | 85.71 | 2 | 85.69 | 2 |
| 12 | 85.73 | A 85.75, B 85.75, C 85.69 | 85.75 | 3 | 85.74 | 2 |
| 13 | 85.83 | A 85.75, B 86.0, C 85.75 | 85.52 | 2 | 85.77 | 2 |
| 14 | 85.88 | A 86.0, B 85.75, C 85.88 | 85.80 | 1 | 85.83 | 2 |
| 15 | 85.96 | A 86.0, B 86.0, C 85.88 | 85.86 | 1 | 85.91 | 2 |
| 16 | 86.00 | A 86.0, B 86.0, C 86.0 | 85.95 | 1 | 86.00 | 2 |
| 17 | 86.33 | A 86.5, B 86.5, C 86.0 | 86.00 | 1 | 86.00 | 2 |
| 18 | 86.67 | A 87.0, B 86.5, C 86.5 | 86.34 | 2 | 86.50 | 2 |
| 19 | 86.75 | A 86.75, B 86.75, C 86.75 | 86.64 | 1 | 86.83 | 2 |
| 20 | 86.92 | A 87.0, B 87.0, C 86.75 | 86.75 | 1 | 86.75 | 2 |
| 21 | 87.00 | A 87.0, B 87.0, C 87.0 | 86.92 | 2 | 87.00 | 2 |
| 22 | 87.00 | A 87.0, B 87.0, C 87.0 | 87.01 | 3 | 87.00 | 2 |
| 23 | 87.33 | A 87.5, B 87.5, C 87.0 | 87.00 | 1 | 87.00 | 2 |
| 24 | 87.75 | A 88.0, B 87.75, C 87.5 | 87.34 | 1 | 87.50 | 2 |
| 25 | 87.88 | A 87.75, B 88.0, C 87.88 | 87.67 | 1 | 87.75 | 2 |
| 26 | 87.92 | A 88.0, B 87.88, C 87.88 | 87.84 | 2 | 87.88 | 2 |
| 27 | 87.94 | A 87.88, B 88.0, C 87.94 | 87.88 | 1 | 87.88 | 2 |
| 28 | 88.65 | A 89.0, B 89.0, C 87.94 | 87.95 | 1 | 87.94 | 2 |
| 29 | 89.17 | A 89.0, B 89.5, C 89.0 | 88.83 | 2 | 89.00 | 2 |
| 30 | 89.58 | A 90.0, B 89.5, C 89.25 | 89.25 | 1 | 89.38 | 2 |
