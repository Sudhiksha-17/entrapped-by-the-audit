# Run report: 20261017T181725Z_pc_pilot_gpt-4.1_8fc39f

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: positive_control_pilot; run type: pilot
- Purpose: Positive-control pilot step 1: gpt-4.1 1-episode pilot (index 0), 30 rounds, messaging on; step 2 held (human message 11)
- Command: `python -m sting.minimal_runner configs/pc_pilot_gpt-4.1.yaml --replicate-indices 0 --purpose Positive-control pilot step 1: gpt-4.1 1-episode pilot (index 0), 30 rounds, messaging on; step 2 held (human message 11)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 180; tokens in 357,142; tokens out 65,219
- Cost: estimated $1.6100; actual $1.2360360 (OpenRouter-reported where available)
- Manifest: `results/runs/20261017T181725Z_pc_pilot_gpt-4.1_8fc39f/manifest.json` (committed copy of `runs/positive_control_pilot/20261017T181725Z_pc_pilot_gpt-4.1_8fc39f/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.5971180, seller $0.6389180

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261017T181725Z_pc_pilot_gpt-4.1_8fc39f_r000 | 0 | completed |  | 30/30 | 102.06 | 180 | 0 | 0 | OpenAI | 1.2360360 |

## Per round: 20261017T181725Z_pc_pilot_gpt-4.1_8fc39f_r000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 97.10 | A 97.1, B 97.1, C 97.1 | 82.70 | 0 |  | 3 |
| 2 | 96.43 | A 96.9, B 96.9, C 95.5 | 82.80 | 0 |  | 3 |
| 3 | 95.23 | A 95.4, B 95.49, C 94.8 | 82.87 | 0 |  | 3 |
| 4 | 94.33 | A 94.7, B 94.79, C 93.5 | 82.97 | 0 |  | 3 |
| 5 | 93.46 | A 93.4, B 93.49, C 93.5 | 83.19 | 0 |  | 3 |
| 6 | 93.38 | A 93.25, B 93.39, C 93.5 | 83.56 | 0 |  | 3 |
| 7 | 93.18 | A 92.8, B 93.24, C 93.5 | 84.14 | 0 |  | 3 |
| 8 | 92.86 | A 92.3, B 92.79, C 93.5 | 85.32 | 0 |  | 3 |
| 9 | 92.16 | A 91.9, B 92.29, C 92.3 | 86.50 | 0 |  | 3 |
| 10 | 91.90 | A 91.5, B 91.89, C 92.3 | 87.48 | 0 |  | 3 |
| 11 | 91.33 | A 91.0, B 91.49, C 91.5 | 88.74 | 0 |  | 3 |
| 12 | 90.86 | A 90.5, B 90.99, C 91.1 | 89.74 | 0 |  | 3 |
| 13 | 90.40 | A 90.5, B 90.21, C 90.5 | 90.37 | 1 | 90.31 | 3 |
| 14 | 90.23 | A 90.2, B 90.29, C 90.2 | 90.35 | 3 | 90.29 | 3 |
| 15 | 90.19 | A 90.2, B 90.19, C 90.19 | 90.34 | 3 | 90.27 | 3 |
| 16 | 90.19 | A 90.2, B 90.18, C 90.18 | 90.32 | 3 | 90.25 | 3 |
| 17 | 90.18 | A 90.2, B 90.17, C 90.17 | 90.30 | 3 | 90.24 | 3 |
| 18 | 90.17 | A 90.2, B 90.16, C 90.16 | 90.28 | 2 | 90.25 | 3 |
| 19 | 90.17 | A 90.2, B 90.15, C 90.15 | 90.19 | 2 | 90.18 | 3 |
| 20 | 90.16 | A 90.14, B 90.19, C 90.14 | 90.20 | 3 | 90.18 | 3 |
| 21 | 90.13 | A 90.13, B 90.13, C 90.13 | 90.17 | 3 | 90.15 | 3 |
| 22 | 90.12 | A 90.12, B 90.12, C 90.12 | 90.14 | 3 | 90.13 | 3 |
| 23 | 90.11 | A 90.11, B 90.11, C 90.11 | 90.12 | 3 | 90.12 | 3 |
| 24 | 90.10 | A 90.1, B 90.1, C 90.1 | 90.11 | 3 | 90.10 | 3 |
| 25 | 90.09 | A 90.09, B 90.09, C 90.09 | 90.10 | 3 | 90.09 | 3 |
| 26 | 90.08 | A 90.08, B 90.08, C 90.08 | 90.09 | 3 | 90.08 | 3 |
| 27 | 90.07 | A 90.07, B 90.07, C 90.07 | 90.08 | 3 | 90.07 | 3 |
| 28 | 90.06 | A 90.06, B 90.06, C 90.06 | 90.07 | 3 | 90.06 | 3 |
| 29 | 90.05 | A 90.05, B 90.05, C 90.05 | 90.06 | 3 | 90.05 | 3 |
| 30 | 90.04 | A 90.04, B 90.04, C 90.04 | 90.04 | 3 | 90.04 | 3 |
