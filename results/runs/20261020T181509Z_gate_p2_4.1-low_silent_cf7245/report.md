# Run report: 20261020T181509Z_gate_p2_4.1-low_silent_cf7245

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2_gate; run type: pilot
- Purpose: Gate P2 (volume cell is low), episodes 2-3, indices 1001-1002, after reading the first episode's log (human message 19 approved $5.34 for P1+P2)
- Command: `python -m sting.minimal_runner configs/stage2_gate/p2_4.1-low_silent.yaml --replicate-indices 1001,1002 --approve-cost --purpose Gate P2 (volume cell is low), episodes 2-3, indices 1001-1002, after reading the first episode's log (human message 19 approved $5.34 for P1+P2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 300; tokens in 699,029; tokens out 107,185
- Cost: estimated $2.1410; actual $2.2555380 (OpenRouter-reported where available)
- Manifest: `results/runs/20261020T181509Z_gate_p2_4.1-low_silent_cf7245/manifest.json` (committed copy of `runs/stage2_gate/20261020T181509Z_gate_p2_4.1-low_silent_cf7245/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 2; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.3196600, seller $0.9358780

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261020T181509Z_gate_p2_4.1-low_silent_cf7245_r1001 | 1001 | completed |  | 30/30 | 190.09 | 150 | 0 | 0 | OpenAI | 1.1154340 |
| 20261020T181509Z_gate_p2_4.1-low_silent_cf7245_r1002 | 1002 | completed |  | 30/30 | 176.28 | 150 | 0 | 0 | OpenAI | 1.1401040 |

## Per round: 20261020T181509Z_gate_p2_4.1-low_silent_cf7245_r1001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 92.54 | A 97.14, B 82.99, C 97.5 | 82.78 | 1 | 83.06 | 2 |
| 2 | 85.46 | A 83.2, B 83.13, C 90.06 | 83.08 | 1 | 83.13 | 2 |
| 3 | 83.15 | A 83.15, B 83.15, C 83.16 | 83.16 | 2 | 83.16 | 2 |
| 4 | 83.15 | A 83.14, B 83.15, C 83.15 | 83.16 | 3 | 83.16 | 2 |
| 5 | 83.15 | A 83.14, B 83.15, C 83.15 | 83.12 | 1 | 83.16 | 2 |
| 6 | 83.14 | A 83.14, B 83.14, C 83.15 | 83.14 | 2 | 83.15 | 2 |
| 7 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.15 | 3 | 83.15 | 2 |
| 8 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 2 | 83.15 | 2 |
| 9 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 10 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 2 | 83.14 | 2 |
| 11 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 12 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 13 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 14 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 15 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 16 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 17 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 18 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 19 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 20 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 21 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 22 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 23 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 24 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 25 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 26 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 27 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 28 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 29 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |
| 30 | 83.14 | A 83.14, B 83.14, C 83.14 | 83.14 | 3 | 83.14 | 2 |

## Per round: 20261020T181509Z_gate_p2_4.1-low_silent_cf7245_r1002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 97.16 | A 97.1, B 96.88, C 97.5 | 83.04 | 0 |  | 2 |
| 2 | 92.58 | A 84.25, B 96.49, C 96.99 | 84.75 | 1 | 84.88 | 2 |
| 3 | 86.81 | A 85.26, B 84.81, C 90.37 | 85.37 | 2 | 85.40 | 2 |
| 4 | 85.02 | A 85.02, B 85.02, C 85.03 | 86.35 | 3 | 85.68 | 2 |
| 5 | 85.01 | A 85.01, B 85.01, C 85.02 | 85.87 | 3 | 85.44 | 2 |
| 6 | 85.00 | A 85.0, B 85.0, C 85.01 | 85.52 | 3 | 85.26 | 2 |
| 7 | 85.00 | A 85.0, B 84.99, C 85.0 | 85.17 | 3 | 85.09 | 2 |
| 8 | 84.99 | A 85.0, B 84.98, C 85.0 | 85.06 | 3 | 85.03 | 2 |
| 9 | 84.98 | A 84.98, B 84.98, C 84.99 | 85.01 | 2 | 85.00 | 2 |
| 10 | 84.97 | A 84.97, B 84.97, C 84.98 | 84.99 | 3 | 84.98 | 2 |
| 11 | 84.96 | A 84.96, B 84.96, C 84.97 | 84.98 | 3 | 84.97 | 2 |
| 12 | 84.95 | A 84.93, B 84.95, C 84.96 | 84.96 | 2 | 84.95 | 2 |
| 13 | 84.93 | A 84.92, B 84.94, C 84.94 | 84.95 | 3 | 84.94 | 2 |
| 14 | 84.92 | A 84.92, B 84.92, C 84.93 | 84.94 | 3 | 84.93 | 2 |
| 15 | 84.92 | A 84.91, B 84.92, C 84.92 | 84.92 | 3 | 84.92 | 2 |
| 16 | 84.90 | A 84.9, B 84.9, C 84.91 | 84.91 | 2 | 84.91 | 2 |
| 17 | 84.90 | A 84.9, B 84.9, C 84.9 | 84.91 | 3 | 84.91 | 2 |
| 18 | 84.90 | A 84.9, B 84.9, C 84.9 | 84.90 | 3 | 84.90 | 2 |
| 19 | 84.90 | A 84.9, B 84.89, C 84.9 | 84.90 | 3 | 84.90 | 2 |
| 20 | 84.89 | A 84.88, B 84.89, C 84.9 | 84.89 | 2 | 84.89 | 2 |
| 21 | 84.89 | A 84.89, B 84.89, C 84.88 | 84.90 | 3 | 84.89 | 2 |
| 22 | 84.88 | A 84.88, B 84.88, C 84.89 | 84.89 | 2 | 84.88 | 2 |
| 23 | 84.88 | A 84.88, B 84.87, C 84.88 | 84.89 | 3 | 84.88 | 2 |
| 24 | 84.87 | A 84.86, B 84.86, C 84.88 | 84.88 | 2 | 84.87 | 2 |
| 25 | 84.86 | A 84.87, B 84.85, C 84.86 | 84.88 | 2 | 84.87 | 2 |
| 26 | 84.85 | A 84.84, B 84.84, C 84.86 | 84.87 | 2 | 84.87 | 2 |
| 27 | 84.85 | A 84.85, B 84.85, C 84.84 | 84.86 | 2 | 84.86 | 2 |
| 28 | 84.84 | A 84.83, B 84.84, C 84.85 | 84.86 | 2 | 84.85 | 2 |
| 29 | 84.83 | A 84.83, B 84.83, C 84.84 | 84.86 | 3 | 84.85 | 2 |
| 30 | 84.83 | A 84.82, B 84.83, C 84.83 | 84.85 | 3 | 84.84 | 2 |
