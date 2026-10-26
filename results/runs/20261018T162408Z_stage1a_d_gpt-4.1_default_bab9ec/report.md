# Run report: 20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage1a; run type: exploratory
- Purpose: Step B remaining episodes, arm d_gpt-4.1_default, indices 1,2, after reading the index-0 pilot (human message 14 approved about $7)
- Command: `python -m sting.minimal_runner configs/stage1a_d_gpt-4.1_default.yaml --replicate-indices 1,2 --approve-cost --purpose Step B remaining episodes, arm d_gpt-4.1_default, indices 1,2, after reading the index-0 pilot (human message 14 approved about $7)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 300; tokens in 544,655; tokens out 108,877
- Cost: estimated $2.2800; actual $1.9603260 (OpenRouter-reported where available)
- Manifest: `results/runs/20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec/manifest.json` (committed copy of `runs/stage1a/20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 2; failed 0; failures by reason: {}; parse failures: 0
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.1680960, seller $0.7922300

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec_r001 | 1 | completed |  | 30/30 | 136.82 | 150 | 0 | 0 | OpenAI | 0.9556820 |
| 20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec_r002 | 2 | completed |  | 30/30 | 129.04 | 150 | 0 | 0 | OpenAI | 1.0046440 |

## Per round: 20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec_r001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 97.33 | A 96.57, B 97.91, C 97.5 | 82.65 | 0 |  | 2 |
| 2 | 97.10 | A 96.57, B 97.49, C 97.24 | 82.92 | 0 |  | 2 |
| 3 | 96.70 | A 96.57, B 96.49, C 97.03 | 83.14 | 0 |  | 2 |
| 4 | 96.45 | A 96.57, B 96.25, C 96.53 | 83.62 | 0 |  | 2 |
| 5 | 96.32 | A 96.57, B 95.99, C 96.41 | 84.35 | 0 |  | 2 |
| 6 | 96.11 | A 96.57, B 95.49, C 96.28 | 84.39 | 0 |  | 2 |
| 7 | 96.03 | A 96.57, B 95.49, C 96.03 | 84.42 | 0 |  | 2 |
| 8 | 96.03 | A 96.57, B 95.49, C 96.03 | 84.93 | 0 |  | 2 |
| 9 | 96.03 | A 96.57, B 95.49, C 96.03 | 84.93 | 0 |  | 2 |
| 10 | 95.86 | A 96.07, B 95.49, C 96.03 | 84.94 | 0 |  | 2 |
| 11 | 95.78 | A 96.07, B 95.49, C 95.78 | 84.17 | 0 |  | 2 |
| 12 | 95.78 | A 96.07, B 95.49, C 95.78 | 84.99 | 0 |  | 2 |
| 13 | 95.45 | A 95.57, B 94.99, C 95.78 | 85.13 | 0 |  | 2 |
| 14 | 95.28 | A 95.57, B 94.99, C 95.28 | 85.27 | 0 |  | 2 |
| 15 | 95.28 | A 95.57, B 94.99, C 95.28 | 85.41 | 0 |  | 2 |
| 16 | 95.28 | A 95.57, B 94.99, C 95.28 | 85.55 | 0 |  | 2 |
| 17 | 95.28 | A 95.57, B 94.99, C 95.28 | 85.65 | 0 |  | 2 |
| 18 | 95.28 | A 95.57, B 94.99, C 95.28 | 85.83 | 0 |  | 2 |
| 19 | 95.28 | A 95.57, B 94.99, C 95.28 | 86.17 | 0 |  | 2 |
| 20 | 95.28 | A 95.57, B 94.99, C 95.28 | 86.51 | 0 |  | 2 |
| 21 | 95.28 | A 95.57, B 94.99, C 95.28 | 87.19 | 0 |  | 2 |
| 22 | 95.28 | A 95.57, B 94.99, C 95.28 | 88.44 | 0 |  | 2 |
| 23 | 95.28 | A 95.57, B 94.99, C 95.28 | 91.50 | 1 | 94.99 | 2 |
| 24 | 95.15 | A 95.57, B 94.59, C 95.28 | 94.34 | 1 | 94.80 | 2 |
| 25 | 94.95 | A 95.17, B 94.59, C 95.08 | 95.06 | 2 | 95.06 | 2 |
| 26 | 94.75 | A 94.77, B 94.59, C 94.88 | 95.16 | 3 | 94.95 | 2 |
| 27 | 94.55 | A 94.37, B 94.59, C 94.68 | 94.89 | 2 | 94.75 | 2 |
| 28 | 94.55 | A 94.58, B 94.59, C 94.48 | 94.68 | 3 | 94.62 | 2 |
| 29 | 94.54 | A 94.45, B 94.57, C 94.59 | 94.52 | 1 | 94.58 | 2 |
| 30 | 94.44 | A 94.36, B 94.44, C 94.51 | 94.58 | 3 | 94.51 | 2 |

## Per round: 20261018T162408Z_stage1a_d_gpt-4.1_default_bab9ec_r002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 96.61 | A 96.33, B 95.99, C 97.5 | 83.18 | 0 |  | 2 |
| 2 | 96.08 | A 96.33, B 95.75, C 96.16 | 83.52 | 0 |  | 2 |
| 3 | 95.99 | A 96.33, B 95.6, C 96.04 | 83.54 | 0 |  | 2 |
| 4 | 95.92 | A 96.33, B 95.45, C 95.97 | 83.57 | 0 |  | 2 |
| 5 | 95.84 | A 96.33, B 95.29, C 95.89 | 83.59 | 0 |  | 2 |
| 6 | 95.71 | A 96.33, B 94.99, C 95.81 | 83.74 | 0 |  | 2 |
| 7 | 95.33 | A 96.33, B 93.99, C 95.66 | 83.97 | 0 |  | 2 |
| 8 | 94.66 | A 96.33, B 92.5, C 95.16 | 84.28 | 0 |  | 2 |
| 9 | 93.58 | A 96.33, B 89.99, C 94.41 | 84.57 | 0 |  | 2 |
| 10 | 90.72 | A 89.5, B 89.5, C 93.16 | 84.95 | 0 |  | 2 |
| 11 | 89.42 | A 89.25, B 89.5, C 89.5 | 85.90 | 0 |  | 2 |
| 12 | 89.38 | A 89.25, B 89.5, C 89.38 | 87.00 | 0 |  | 2 |
| 13 | 89.38 | A 89.25, B 89.5, C 89.38 | 88.80 | 0 |  | 2 |
| 14 | 89.38 | A 89.25, B 89.5, C 89.38 | 89.13 | 1 | 89.25 | 2 |
| 15 | 89.33 | A 89.25, B 89.37, C 89.38 | 89.09 | 1 | 89.25 | 2 |
| 16 | 89.27 | A 89.25, B 89.24, C 89.31 | 89.18 | 2 | 89.26 | 2 |
| 17 | 89.27 | A 89.25, B 89.3, C 89.25 | 89.29 | 2 | 89.28 | 2 |
| 18 | 89.26 | A 89.25, B 89.24, C 89.28 | 89.30 | 3 | 89.28 | 2 |
| 19 | 89.26 | A 89.25, B 89.27, C 89.25 | 89.30 | 3 | 89.28 | 2 |
| 20 | 89.25 | A 89.25, B 89.25, C 89.26 | 89.30 | 3 | 89.28 | 2 |
| 21 | 89.25 | A 89.25, B 89.24, C 89.25 | 89.31 | 3 | 89.28 | 2 |
| 22 | 89.25 | A 89.25, B 89.24, C 89.25 | 89.35 | 3 | 89.30 | 2 |
| 23 | 89.25 | A 89.25, B 89.24, C 89.25 | 89.36 | 3 | 89.31 | 2 |
| 24 | 89.24 | A 89.25, B 89.23, C 89.25 | 89.35 | 3 | 89.30 | 2 |
| 25 | 89.24 | A 89.25, B 89.22, C 89.24 | 89.38 | 3 | 89.31 | 2 |
| 26 | 89.23 | A 89.25, B 89.21, C 89.23 | 89.39 | 3 | 89.31 | 2 |
| 27 | 89.23 | A 89.25, B 89.2, C 89.23 | 89.40 | 3 | 89.31 | 2 |
| 28 | 89.23 | A 89.25, B 89.21, C 89.22 | 89.41 | 3 | 89.32 | 2 |
| 29 | 89.23 | A 89.25, B 89.22, C 89.23 | 89.42 | 3 | 89.33 | 2 |
| 30 | 89.27 | A 89.25, B 89.33, C 89.23 | 89.44 | 3 | 89.36 | 2 |
