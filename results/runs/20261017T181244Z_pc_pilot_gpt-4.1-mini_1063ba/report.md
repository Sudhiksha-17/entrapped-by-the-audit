# Run report: 20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: positive_control_pilot; run type: pilot
- Purpose: Positive-control pilot step 1: gpt-4.1-mini 1-episode pilot (index 0), 30 rounds, messaging on (human message 11)
- Command: `python -m sting.minimal_runner configs/pc_pilot_gpt-4.1-mini.yaml --replicate-indices 0 --purpose Positive-control pilot step 1: gpt-4.1-mini 1-episode pilot (index 0), 30 rounds, messaging on (human message 11)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 180; tokens in 409,438; tokens out 59,797
- Cost: estimated $0.3300; actual $0.2594504 (OpenRouter-reported where available)
- Manifest: `results/runs/20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba/manifest.json` (committed copy of `runs/positive_control_pilot/20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1293660, seller $0.1300844

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba_r000 | 0 | completed |  | 30/30 | 105.18 | 180 | 0 | 0 | OpenAI | 0.2594504 |

## Per round: 20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba_r000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 83.92 | A 83.75, B 84.5, C 83.5 | 86.33 | 2 | 85.56 | 3 |
| 2 | 84.02 | A 84.05, B 83.9, C 84.1 | 84.80 | 3 | 84.41 | 3 |
| 3 | 81.00 | A 81.0, C 81.0 | 84.75 | 2 | 83.12 | 3 |
| 4 | 83.68 | A 83.5, B 83.85, C 83.7 | 84.00 | 3 | 83.84 | 3 |
| 5 | 83.60 | A 83.5, C 83.7 | 84.00 | 2 | 83.92 | 3 |
| 6 | 83.53 | A 83.4, B 83.6, C 83.6 | 84.03 | 2 | 83.90 | 3 |
| 7 | 83.54 | A 83.4, B 83.61, C 83.6 | 84.07 | 3 | 83.80 | 3 |
| 8 | 83.55 | A 83.5, C 83.6 | 84.07 | 2 | 83.92 | 3 |
| 9 | 83.62 | A 83.6, B 83.62, C 83.65 | 84.00 | 2 | 83.91 | 3 |
| 10 | 83.63 | A 83.6, B 83.63, C 83.66 | 84.02 | 3 | 83.83 | 3 |
| 11 | 83.69 | A 83.7, B 83.67, C 83.7 | 84.00 | 2 | 83.94 | 3 |
| 12 | 83.70 | A 83.72, B 83.68, C 83.71 | 83.96 | 2 | 83.90 | 3 |
| 13 | 83.70 | A 83.69, B 83.69, C 83.73 | 83.98 | 2 | 83.90 | 3 |
| 14 | 83.72 | A 83.71, B 83.71, C 83.74 | 83.99 | 2 | 83.91 | 3 |
| 15 | 83.74 | A 83.73, B 83.73, C 83.75 | 83.99 | 2 | 83.93 | 3 |
| 16 | 83.75 | A 83.74, B 83.74, C 83.76 | 84.00 | 2 | 83.94 | 3 |
| 17 | 83.76 | A 83.75, B 83.76, C 83.76 | 84.01 | 3 | 83.88 | 3 |
| 18 | 83.77 | A 83.77, C 83.77 | 83.92 | 2 | 83.88 | 3 |
| 19 | 83.79 | A 83.79, B 83.79, C 83.79 | 83.93 | 3 | 83.86 | 3 |
| 20 | 83.80 | A 83.8, C 83.8 | 83.93 | 2 | 83.90 | 3 |
| 21 | 83.80 | A 83.8, C 83.8 | 83.93 | 2 | 83.91 | 3 |
| 22 | 83.80 | A 83.8, B 83.8, C 83.8 | 83.94 | 2 | 83.91 | 3 |
| 23 | 83.83 | A 83.83, B 83.83, C 83.83 | 83.94 | 1 | 84.02 | 3 |
| 24 | 83.83 | A 83.84, B 83.83, C 83.83 | 83.94 | 2 | 83.92 | 3 |
| 25 | 83.82 | A 83.85, B 83.8, C 83.8 | 83.94 | 2 | 83.91 | 3 |
| 26 | 83.80 | A 83.8, B 83.8, C 83.8 | 83.95 | 2 | 83.91 | 3 |
| 27 | 83.80 | A 83.8, B 83.8, C 83.8 | 83.93 | 2 | 83.90 | 3 |
| 28 | 83.80 | A 83.8, B 83.8, C 83.8 | 83.93 | 2 | 83.90 | 3 |
| 29 | 83.80 | A 83.8, B 83.8, C 83.8 | 83.93 | 2 | 83.90 | 3 |
| 30 | 83.80 | A 83.8, B 83.8, C 83.8 | 83.95 | 2 | 83.91 | 3 |
