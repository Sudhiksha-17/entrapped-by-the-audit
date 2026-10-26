# Run report: 20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage1a; run type: exploratory
- Purpose: Stage 1a 1-episode pilot, arm c_llama-3.3-70b_default, index 0 (human message 13)
- Command: `python -m sting.minimal_runner configs/stage1a_c_llama-3.3-70b_default.yaml --replicate-indices 0 --purpose Stage 1a 1-episode pilot, arm c_llama-3.3-70b_default, index 0 (human message 13)`
- Models: openrouter:meta-llama/llama-3.3-70b-instruct@novita/bf16
- Calls: 153; tokens in 329,243; tokens out 40,567
- Cost: estimated $0.0900; actual $0.0606746 (OpenRouter-reported where available)
- Manifest: `results/runs/20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8/manifest.json` (committed copy of `runs/stage1a/20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 3
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0382246, seller $0.0224500

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8_r000 | 0 | completed |  | 30/30 | 231.57 | 153 | 3 | 0 | Novita | 0.0606746 |

## Per round: 20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8_r000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 96.17 | A 96.0, B 95.0, C 97.5 | 87.19 | 0 |  | 0 |
| 2 | 94.50 | A 94.0, B 94.0, C 95.5 | 88.08 | 0 |  | 2 |
| 3 | 93.77 | A 93.8, B 93.5, C 94.0 | 88.42 | 0 |  | 2 |
| 4 | 93.38 | A 93.25, B 93.25, C 93.65 | 89.00 | 0 |  | 2 |
| 5 | 92.92 | A 92.5, B 93.0, C 93.25 | 89.75 | 1 | 92.88 | 2 |
| 6 | 92.33 | A 91.75, B 92.5, C 92.75 | 90.25 | 1 | 92.25 | 2 |
| 7 | 91.71 | A 91.0, B 92.0, C 92.12 | 90.83 | 1 | 91.75 | 2 |
| 8 | 91.17 | A 90.5, B 91.5, C 91.5 | 90.92 | 1 | 91.12 | 2 |
| 9 | 90.75 | A 90.25, B 91.0, C 91.0 | 91.08 | 3 | 90.92 | 2 |
| 10 | 90.37 | A 90.0, B 90.5, C 90.62 | 91.08 | 2 | 90.81 | 2 |
| 11 | 90.08 | A 89.75, B 90.25, C 90.25 | 90.87 | 3 | 90.48 | 2 |
| 12 | 89.75 | A 89.25, B 90.0, C 90.0 | 90.58 | 3 | 90.17 | 2 |
| 13 | 89.62 | A 89.5, B 89.75, C 89.62 | 89.83 | 2 | 89.78 | 2 |
| 14 | 89.46 | A 89.25, B 89.5, C 89.62 | 89.50 | 2 | 89.50 | 2 |
| 15 | 89.21 | A 89.0, B 89.25, C 89.38 | 89.58 | 3 | 89.40 | 2 |
| 16 | 89.04 | A 88.88, B 89.12, C 89.12 | 89.21 | 3 | 89.12 | 2 |
| 17 | 88.85 | A 88.5, B 89.06, C 89.0 | 88.96 | 2 | 88.88 | 2 |
| 18 | 88.66 | A 88.25, B 88.94, C 88.78 | 88.86 | 2 | 88.72 | 2 |
| 19 | 88.58 | A 88.25, B 88.89, C 88.59 | 88.87 | 2 | 88.69 | 2 |
| 20 | 88.69 | A 88.69, B 88.8, C 88.57 | 88.94 | 3 | 88.81 | 2 |
| 21 | 88.73 | A 88.65, B 88.79, C 88.75 | 88.91 | 3 | 88.82 | 2 |
| 22 | 88.70 | A 88.6, B 88.78, C 88.72 | 88.89 | 2 | 88.82 | 2 |
| 23 | 88.68 | A 88.58, B 88.77, C 88.69 | 88.92 | 3 | 88.80 | 2 |
| 24 | 88.66 | A 88.55, B 88.76, C 88.67 | 88.92 | 3 | 88.79 | 2 |
| 25 | 88.64 | A 88.52, B 88.75, C 88.66 | 88.93 | 3 | 88.78 | 2 |
| 26 | 88.62 | A 88.5, B 88.74, C 88.63 | 88.88 | 3 | 88.75 | 2 |
| 27 | 88.61 | A 88.48, B 88.73, C 88.62 | 88.84 | 3 | 88.72 | 2 |
| 28 | 88.60 | A 88.46, B 88.72, C 88.61 | 88.72 | 3 | 88.66 | 2 |
| 29 | 88.58 | A 88.44, B 88.71, C 88.59 | 88.71 | 2 | 88.62 | 2 |
| 30 | 88.56 | A 88.42, B 88.7, C 88.57 | 88.71 | 3 | 88.63 | 2 |
