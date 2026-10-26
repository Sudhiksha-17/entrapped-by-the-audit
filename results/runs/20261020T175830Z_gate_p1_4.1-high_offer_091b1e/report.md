# Run report: 20261020T175830Z_gate_p1_4.1-high_offer_091b1e

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2_gate; run type: pilot
- Purpose: Gate P1 (X = $98 clears), second episode, index 1001, after reading the first episode's log (human message 19)
- Command: `python -m sting.minimal_runner configs/stage2_gate/p1_4.1-high_offer.yaml --replicate-indices 1001 --purpose Gate P1 (X = $98 clears), second episode, index 1001, after reading the first episode's log (human message 19)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 150; tokens in 257,464; tokens out 54,658
- Cost: estimated $1.0623; actual $0.9521920 (OpenRouter-reported where available)
- Manifest: `results/runs/20261020T175830Z_gate_p1_4.1-high_offer_091b1e/manifest.json` (committed copy of `runs/stage2_gate/20261020T175830Z_gate_p1_4.1-high_offer_091b1e/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.5544020, seller $0.3977900

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261020T175830Z_gate_p1_4.1-high_offer_091b1e_r1001 | 1001 | completed |  | 30/30 | 618.08 | 150 | 0 | 0 | OpenAI | 0.9521920 |

## Per round: 20261020T175830Z_gate_p1_4.1-high_offer_091b1e_r1001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 96.88 | A 97.14, B 95.99, C 97.5 | 82.75 | 0 |  | 2 |
| 2 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.06 | 0 |  | 2 |
| 3 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.10 | 0 |  | 2 |
| 4 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.21 | 0 |  | 2 |
| 5 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.25 | 0 |  | 2 |
| 6 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.30 | 0 |  | 2 |
| 7 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.34 | 0 |  | 2 |
| 8 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.37 | 0 |  | 2 |
| 9 | 96.56 | A 97.14, B 95.99, C 96.56 | 83.39 | 0 |  | 2 |
| 10 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.47 | 0 |  | 3 |
| 11 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.48 | 0 |  | 2 |
| 12 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.55 | 0 |  | 2 |
| 13 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.55 | 0 |  | 2 |
| 14 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.55 | 0 |  | 2 |
| 15 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.55 | 0 |  | 2 |
| 16 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.55 | 0 |  | 2 |
| 17 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.55 | 0 |  | 2 |
| 18 | 97.04 | A 97.14, B 95.99, C 98.0 | 83.82 | 0 |  | 2 |
| 19 | 97.04 | A 97.14, B 95.99, C 98.0 | 84.07 | 0 |  | 2 |
| 20 | 97.04 | A 97.14, B 95.99, C 98.0 | 85.27 | 0 |  | 2 |
| 21 | 97.04 | A 97.14, B 95.99, C 98.0 | 86.38 | 0 |  | 2 |
| 22 | 97.04 | A 97.14, B 95.99, C 98.0 | 87.77 | 0 |  | 2 |
| 23 | 97.04 | A 97.14, B 95.99, C 98.0 | 89.13 | 0 |  | 2 |
| 24 | 97.04 | A 97.14, B 95.99, C 98.0 | 90.67 | 0 |  | 2 |
| 25 | 97.04 | A 97.14, B 95.99, C 98.0 | 93.93 | 0 |  | 2 |
| 26 | 97.04 | A 97.14, B 95.99, C 98.0 | 95.58 | 1 | 96.00 | 2 |
| 27 | 96.83 | A 96.5, B 95.99, C 98.0 | 96.77 | 2 | 96.70 | 2 |
| 28 | 96.82 | A 95.98, B 96.49, C 98.0 | 96.87 | 2 | 96.65 | 2 |
| 29 | 97.16 | A 96.5, B 96.98, C 98.0 | 97.69 | 2 | 97.32 | 2 |
| 30 | 97.65 | A 97.45, B 97.5, C 98.0 | 98.04 | 3 | 97.84 | 2 |
