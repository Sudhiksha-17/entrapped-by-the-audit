# Run report: 20261024T061119Z_study1r_probe_check_mini-low_silent_be88db

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_probe_check; run type: exploratory
- Purpose: Study 1R probe check 2 (human message 64): fixed probe wording (plain-text prefix, new Q2), one mini-low Silent episode, exploratory
- Command: `python -m sting.minimal_runner configs/study1r/probe_check/mini-low_silent.yaml --replicate-indices 3001 --purpose Study 1R probe check 2 (human message 64): fixed probe wording (plain-text prefix, new Q2), one mini-low Silent episode, exploratory`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 154; tokens in 362,100; tokens out 50,555
- Cost: estimated $0.2481; actual $0.2236544 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T061119Z_study1r_probe_check_mini-low_silent_be88db/manifest.json` (committed copy of `runs/study1r_probe_check/20261024T061119Z_study1r_probe_check_mini-low_silent_be88db/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1299512, probe $0.0043524, seller $0.0893508

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T061119Z_study1r_probe_check_mini-low_silent_be88db_r3001 | 3001 | completed |  | 30/30 | 93.82 | 154 | 0 | 0 | OpenAI | 0.2236544 |

## Per round: 20261024T061119Z_study1r_probe_check_mini-low_silent_be88db_r3001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 88.53 | A 85.0, B 83.1, C 97.5 | 91.67 | 2 | 89.53 | 2 |
| 2 | 84.72 | A 85.0, B 85.1, C 84.05 | 92.00 | 3 | 88.36 | 2 |
| 3 | 85.03 | A 85.0, C 85.05 | 90.67 | 2 | 88.52 | 2 |
| 4 | 87.07 | A 88.05, B 88.1, C 85.05 | 90.83 | 3 | 88.95 | 2 |
| 5 | 87.97 | A 87.75, B 88.1, C 88.07 | 90.50 | 3 | 89.24 | 2 |
| 6 | 87.94 | A 87.9, B 88.0, C 87.92 | 90.67 | 3 | 89.30 | 2 |
| 7 | 87.95 | A 87.9, B 88.0, C 87.95 | 90.67 | 3 | 89.31 | 2 |
| 8 | 87.92 | A 87.85, B 87.96, C 87.95 | 90.67 | 3 | 89.29 | 2 |
| 9 | 87.88 | A 87.8, B 87.93, C 87.91 | 90.67 | 3 | 89.27 | 2 |
| 10 | 87.85 | A 87.8, B 87.89, C 87.87 | 90.67 | 3 | 89.26 | 2 |
| 11 | 87.81 | A 87.75, B 87.83, C 87.84 | 90.67 | 3 | 89.23 | 2 |
| 12 | 87.79 | A 87.74, B 87.83, C 87.79 | 90.67 | 3 | 89.23 | 2 |
| 13 | 87.76 | A 87.73, B 87.77, C 87.78 | 90.67 | 3 | 89.21 | 2 |
| 14 | 87.74 | A 87.74, B 87.74, C 87.75 | 90.67 | 3 | 89.20 | 2 |
| 15 | 87.73 | A 87.73, B 87.73, C 87.74 | 90.67 | 3 | 89.20 | 2 |
| 16 | 87.73 | A 87.73, B 87.72, C 87.73 | 90.67 | 3 | 89.20 | 2 |
| 17 | 88.31 | A 89.5, B 87.71, C 87.72 | 90.67 | 2 | 89.73 | 2 |
| 18 | 88.70 | A 89.0, B 88.49, C 88.6 | 89.50 | 2 | 89.28 | 2 |
| 19 | 88.91 | A 89.0, B 88.99, C 88.75 | 89.42 | 1 | 89.88 | 2 |
| 20 | 88.99 | A 89.0, B 88.98, C 89.0 | 89.50 | 1 | 89.99 | 2 |
| 21 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 22 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 23 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 24 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 25 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 26 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 27 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 28 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 29 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.50 | 1 | 89.99 | 2 |
| 30 | 88.99 | A 89.0, B 88.98, C 88.99 | 89.58 | 2 | 89.49 | 2 |
