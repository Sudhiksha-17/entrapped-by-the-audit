# Run report: 20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: positive_control_pilot; run type: pilot
- Purpose: Positive-control pilot step 1: gpt-4.1-mini episodes 2-3 (indices 1,2) after reading the index-0 pilot log (human message 11)
- Command: `python -m sting.minimal_runner configs/pc_pilot_gpt-4.1-mini.yaml --replicate-indices 1,2 --purpose Positive-control pilot step 1: gpt-4.1-mini episodes 2-3 (indices 1,2) after reading the index-0 pilot log (human message 11)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 360; tokens in 806,874; tokens out 124,595
- Cost: estimated $0.6600; actual $0.5221016 (OpenRouter-reported where available)
- Manifest: `results/runs/20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41/manifest.json` (committed copy of `runs/positive_control_pilot/20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 2; failed 0; failures by reason: {}; parse failures: 0
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.2618156, seller $0.2602860

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41_r001 | 1 | completed |  | 30/30 | 126.9 | 180 | 0 | 0 | OpenAI | 0.2584540 |
| 20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41_r002 | 2 | completed |  | 30/30 | 102.28 | 180 | 0 | 0 | OpenAI | 0.2636476 |

## Per round: 20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41_r001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 91.17 | A 83.0, B 95.0, C 95.5 | 84.27 | 1 | 84.00 | 3 |
| 2 | 91.50 | A 85.1, B 94.5, C 94.9 | 88.37 | 1 | 87.55 | 3 |
| 3 | 92.17 | A 90.1, B 92.0, C 94.4 | 91.70 | 2 | 91.78 | 3 |
| 4 | 90.27 | A 90.2, B 90.5, C 90.1 | 92.93 | 3 | 91.60 | 3 |
| 5 | 94.40 | A 94.4, B 94.4, C 94.4 | 91.53 | 0 |  | 3 |
| 6 | 94.37 | A 94.5, B 94.4, C 94.2 | 93.97 | 0 |  | 3 |
| 7 | 94.20 | A 94.5, B 94.1, C 94.0 | 94.17 | 2 | 94.12 | 3 |
| 8 | 94.12 | A 94.5, B 93.9, C 93.95 | 94.25 | 2 | 94.09 | 3 |
| 9 | 94.23 | A 94.5, B 93.85, C 94.35 | 94.32 | 1 | 94.12 | 3 |
| 10 | 94.21 | A 94.4, B 93.95, C 94.28 | 94.32 | 2 | 94.22 | 3 |
| 11 | 94.33 | A 94.35, B 94.35, C 94.29 | 94.32 | 1 | 94.32 | 3 |
| 12 | 94.33 | A 94.35, B 94.35, C 94.3 | 94.32 | 1 | 94.32 | 3 |
| 13 | 94.34 | A 94.35, B 94.35, C 94.31 | 94.32 | 1 | 94.33 | 3 |
| 14 | 94.34 | A 94.35, B 94.35, C 94.32 | 94.33 | 1 | 94.33 | 3 |
| 15 | 94.34 | A 94.35, B 94.35, C 94.33 | 94.33 | 1 | 94.34 | 3 |
| 16 | 94.34 | A 94.35, B 94.35, C 94.33 | 94.33 | 1 | 94.34 | 3 |
| 17 | 94.34 | A 94.35, B 94.35, C 94.33 | 94.33 | 1 | 94.34 | 3 |
| 18 | 94.34 | A 94.35, B 94.35, C 94.33 | 94.33 | 1 | 94.34 | 3 |
| 19 | 94.34 | A 94.35, B 94.35, C 94.33 | 94.33 | 1 | 94.34 | 3 |
| 20 | 94.34 | A 94.35, B 94.35, C 94.33 | 94.33 | 1 | 94.34 | 3 |
| 21 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 22 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 23 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 24 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 25 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 26 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 27 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.33 | 2 | 94.34 | 3 |
| 28 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.34 | 2 | 94.34 | 3 |
| 29 | 94.34 | A 94.34, B 94.35, C 94.33 | 94.35 | 2 | 94.34 | 3 |
| 30 | 94.34 | A 94.34, B 94.36, C 94.33 | 94.35 | 2 | 94.34 | 3 |

## Per round: 20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41_r002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 84.20 | A 85.0, B 83.6, C 84.0 | 90.00 | 3 | 87.10 | 2 |
| 2 | 84.67 | A 85.0, B 87.0, C 82.0 | 88.17 | 3 | 86.42 | 3 |
| 3 | 85.17 | A 86.0, B 86.5, C 83.0 | 87.50 | 3 | 86.33 | 3 |
| 4 | 85.00 | A 85.5, B 85.5, C 84.0 | 87.33 | 3 | 86.17 | 3 |
| 5 | 85.08 | A 85.5, B 85.5, C 84.25 | 87.17 | 3 | 86.13 | 3 |
| 6 | 85.17 | A 85.5, B 85.5, C 84.5 | 87.17 | 3 | 86.17 | 3 |
| 7 | 85.25 | A 85.5, B 85.5, C 84.75 | 87.17 | 3 | 86.21 | 3 |
| 8 | 85.33 | A 85.5, B 85.5, C 85.0 | 87.17 | 3 | 86.25 | 3 |
| 9 | 85.42 | A 85.5, B 85.5, C 85.25 | 87.17 | 3 | 86.29 | 3 |
| 10 | 85.50 | A 85.5, B 85.5, C 85.5 | 87.17 | 3 | 86.33 | 3 |
| 11 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.17 | 3 | 86.38 | 3 |
| 12 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.17 | 3 | 86.38 | 3 |
| 13 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.17 | 3 | 86.38 | 3 |
| 14 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 15 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.33 | 3 | 86.46 | 3 |
| 16 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.42 | 3 | 86.50 | 3 |
| 17 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.42 | 3 | 86.50 | 3 |
| 18 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.42 | 3 | 86.50 | 3 |
| 19 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.62 | 2 | 86.56 | 3 |
| 20 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 21 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 22 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 23 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 24 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 25 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 26 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.25 | 3 | 86.42 | 3 |
| 27 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.17 | 3 | 86.38 | 3 |
| 28 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.17 | 3 | 86.38 | 3 |
| 29 | 85.58 | A 85.5, B 85.5, C 85.75 | 87.17 | 3 | 86.38 | 3 |
| 30 | 86.04 | A 86.88, B 85.5, C 85.75 | 87.33 | 2 | 86.81 | 3 |
