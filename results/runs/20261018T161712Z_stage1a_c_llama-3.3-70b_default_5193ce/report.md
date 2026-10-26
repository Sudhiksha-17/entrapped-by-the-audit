# Run report: 20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage1a; run type: exploratory
- Purpose: Step A: Llama remaining episodes, indices 1,2 (human message 14)
- Command: `python -m sting.minimal_runner configs/stage1a_c_llama-3.3-70b_default.yaml --replicate-indices 1,2 --purpose Step A: Llama remaining episodes, indices 1,2 (human message 14)`
- Models: openrouter:meta-llama/llama-3.3-70b-instruct@novita/bf16
- Calls: 112; tokens in 64,517; tokens out 16,597
- Cost: estimated $0.1800; actual $0.0153486 (OpenRouter-reported where available)
- Manifest: `results/runs/20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce/manifest.json` (committed copy of `runs/stage1a/20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 0; failed 2; failures by reason: {'api_failure': 2}; parse failures: 12
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0099495, seller $0.0053990

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce_r001 | 1 | failed | api_failure | 6/30 | 87.83 | 59 | 4 | 0 | Novita | 0.0091637 |
| 20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce_r002 | 2 | failed | api_failure | 4/30 | 80.84 | 53 | 8 | 0 | Novita | 0.0061849 |

## Per round: 20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce_r001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 97.50 | A 96.0, B 99.0, C 97.5 | 86.67 | 0 |  | 1 |
| 2 | 96.17 | A 94.0, B 97.0, C 97.5 | 88.00 | 1 | 94.75 | 2 |
| 3 | 95.00 | A 93.5, B 96.0, C 95.5 | 88.67 | 1 | 94.75 | 2 |
| 4 | 94.08 | A 92.5, B 95.0, C 94.75 | 89.42 | 1 | 94.38 | 2 |
| 5 | 93.42 | A 92.0, B 94.5, C 93.75 | 90.00 | 1 | 94.25 | 2 |
| 6 | 92.92 | A 91.5, B 94.0, C 93.25 | 89.67 | 1 | 92.75 | 2 |

## Per round: 20261018T161712Z_stage1a_c_llama-3.3-70b_default_5193ce_r002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 96.28 | A 96.33, B 95.0, C 97.5 | 87.00 | 0 |  | 0 |
| 2 | 95.22 | A 95.5, B 94.5, C 95.66 | 88.17 | 1 | 94.50 | 2 |
| 3 | 92.33 | A 94.99, B 87.0, C 95.0 | 89.17 | 1 | 91.00 | 2 |
| 4 | 90.33 | A 93.5, B 86.5, C 91.0 | 89.75 | 1 | 90.88 | 2 |
