# Run report: 20261020T180918Z_gate_p2_4.1-low_silent_36fa6c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2_gate; run type: pilot
- Purpose: Gate P2 (volume cell is low), first episode, index 1000 (human message 19)
- Command: `python -m sting.minimal_runner configs/stage2_gate/p2_4.1-low_silent.yaml --replicate-indices 1000 --purpose Gate P2 (volume cell is low), first episode, index 1000 (human message 19)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 150; tokens in 322,550; tokens out 54,852
- Cost: estimated $1.0705; actual $1.0839160 (OpenRouter-reported where available)
- Manifest: `results/runs/20261020T180918Z_gate_p2_4.1-low_silent_36fa6c/manifest.json` (committed copy of `runs/stage2_gate/20261020T180918Z_gate_p2_4.1-low_silent_36fa6c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.6249300, seller $0.4589860

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261020T180918Z_gate_p2_4.1-low_silent_36fa6c_r1000 | 1000 | completed |  | 30/30 | 282.58 | 150 | 0 | 0 | OpenAI | 1.0839160 |

## Per round: 20261020T180918Z_gate_p2_4.1-low_silent_36fa6c_r1000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 97.09 | A 96.29, B 97.49, C 97.5 | 82.86 | 0 |  | 2 |
| 2 | 93.29 | A 93.0, B 89.99, C 96.89 | 83.25 | 0 |  | 2 |
| 3 | 89.75 | A 89.75, B 87.99, C 91.5 | 84.10 | 0 |  | 2 |
| 4 | 87.54 | A 87.75, B 86.0, C 88.87 | 84.94 | 1 | 86.12 | 2 |
| 5 | 87.54 | A 88.86, B 86.87, C 86.88 | 85.34 | 0 |  | 2 |
| 6 | 86.99 | A 86.86, B 86.25, C 87.87 | 85.78 | 1 | 86.38 | 2 |
| 7 | 86.59 | A 86.37, B 86.85, C 86.56 | 86.28 | 1 | 86.51 | 2 |
| 8 | 86.59 | A 86.55, B 86.6, C 86.61 | 86.36 | 1 | 86.60 | 2 |
| 9 | 86.57 | A 86.59, B 86.56, C 86.57 | 86.47 | 1 | 86.62 | 2 |
| 10 | 86.57 | A 86.56, B 86.57, C 86.58 | 86.60 | 1 | 86.62 | 2 |
| 11 | 86.56 | A 86.56, B 86.55, C 86.56 | 86.61 | 3 | 86.58 | 2 |
| 12 | 86.55 | A 86.54, B 86.54, C 86.56 | 86.65 | 3 | 86.60 | 2 |
| 13 | 86.53 | A 86.53, B 86.53, C 86.54 | 86.63 | 3 | 86.58 | 2 |
| 14 | 86.52 | A 86.52, B 86.52, C 86.53 | 86.66 | 3 | 86.59 | 2 |
| 15 | 86.51 | A 86.51, B 86.51, C 86.52 | 86.66 | 3 | 86.59 | 2 |
| 16 | 86.50 | A 86.5, B 86.5, C 86.51 | 86.66 | 3 | 86.58 | 2 |
| 17 | 86.49 | A 86.49, B 86.49, C 86.5 | 86.59 | 3 | 86.54 | 2 |
| 18 | 86.48 | A 86.48, B 86.48, C 86.49 | 86.55 | 2 | 86.55 | 2 |
| 19 | 86.47 | A 86.47, B 86.47, C 86.48 | 86.57 | 2 | 86.55 | 2 |
| 20 | 86.46 | A 86.46, B 86.46, C 86.47 | 86.57 | 2 | 86.55 | 2 |
| 21 | 86.45 | A 86.45, B 86.45, C 86.46 | 86.58 | 3 | 86.52 | 2 |
| 22 | 86.42 | A 86.41, B 86.4, C 86.45 | 86.56 | 2 | 86.52 | 2 |
| 23 | 86.40 | A 86.39, B 86.39, C 86.41 | 86.57 | 3 | 86.48 | 2 |
| 24 | 86.38 | A 86.39, B 86.35, C 86.39 | 86.54 | 3 | 86.46 | 2 |
| 25 | 86.34 | A 86.34, B 86.32, C 86.37 | 86.53 | 2 | 86.47 | 2 |
| 26 | 86.32 | A 86.31, B 86.31, C 86.33 | 86.51 | 3 | 86.42 | 2 |
| 27 | 86.30 | A 86.3, B 86.3, C 86.31 | 86.49 | 3 | 86.40 | 2 |
| 28 | 86.29 | A 86.29, B 86.29, C 86.3 | 86.48 | 2 | 86.44 | 2 |
| 29 | 86.29 | A 86.29, B 86.29, C 86.29 | 86.48 | 2 | 86.44 | 2 |
| 30 | 86.29 | A 86.29, B 86.29, C 86.29 | 86.29 | 3 | 86.29 | 2 |
