# Run report: 20261024T064858Z_study1r_probe_check_mini-low_silent_13d5a2

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_probe_check; run type: exploratory
- Purpose: Study 1R final pre-freeze probe check (human message 66): final probe (Q1 shortened, Q1 400 tokens), one mini-low Silent episode, exploratory
- Command: `python -m sting.minimal_runner configs/study1r/probe_check/mini-low_silent.yaml --replicate-indices 3002 --purpose Study 1R final pre-freeze probe check (human message 66): final probe (Q1 shortened, Q1 400 tokens), one mini-low Silent episode, exploratory`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 154; tokens in 365,194; tokens out 51,274
- Cost: estimated $0.2481; actual $0.2260424 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T064858Z_study1r_probe_check_mini-low_silent_13d5a2/manifest.json` (committed copy of `runs/study1r_probe_check/20261024T064858Z_study1r_probe_check_mini-low_silent_13d5a2/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1338500, probe $0.0042576, seller $0.0879348

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T064858Z_study1r_probe_check_mini-low_silent_13d5a2_r3002 | 3002 | completed |  | 30/30 | 184.03 | 154 | 0 | 0 | OpenAI | 0.2260424 |

## Per round: 20261024T064858Z_study1r_probe_check_mini-low_silent_13d5a2_r3002

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 87.83 | A 83.0, B 83.0, C 97.5 | 91.63 | 2 | 89.47 | 2 |
| 2 | 83.67 | A 83.0, B 85.0, C 83.0 | 92.13 | 3 | 87.90 | 2 |
| 3 | 84.00 | A 83.0, B 85.0, C 84.0 | 90.17 | 3 | 87.08 | 2 |
| 4 | 84.00 | A 83.0, B 85.0, C 84.0 | 91.00 | 3 | 87.50 | 2 |
| 5 | 84.00 | A 83.0, B 85.0, C 84.0 | 91.00 | 3 | 87.50 | 2 |
| 6 | 84.00 | A 83.0, B 85.0, C 84.0 | 90.25 | 3 | 87.13 | 2 |
| 7 | 83.83 | A 83.0, B 84.5, C 84.0 | 90.17 | 3 | 87.00 | 2 |
| 8 | 83.75 | A 83.0, B 84.5, C 83.75 | 90.17 | 3 | 86.96 | 2 |
| 9 | 83.75 | A 83.0, B 84.5, C 83.75 | 90.17 | 3 | 86.96 | 2 |
| 10 | 83.83 | A 83.25, B 84.5, C 83.75 | 90.17 | 3 | 87.00 | 2 |
| 11 | 83.88 | A 83.5, B 84.25, C 83.88 | 90.50 | 3 | 87.19 | 2 |
| 12 | 83.88 | A 83.75, B 84.0, C 83.88 | 90.50 | 3 | 87.19 | 2 |
| 13 | 83.84 | A 83.75, B 83.9, C 83.88 | 90.50 | 3 | 87.17 | 2 |
| 14 | 83.78 | A 83.75, B 83.75, C 83.83 | 90.50 | 3 | 87.14 | 2 |
| 15 | 83.75 | A 83.75, B 83.75, C 83.75 | 90.83 | 3 | 87.29 | 2 |
| 16 | 83.75 | A 83.75, B 83.75, C 83.75 | 91.17 | 3 | 87.46 | 2 |
| 17 | 83.75 | A 83.75, B 83.75, C 83.75 | 91.50 | 3 | 87.63 | 2 |
| 18 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.00 | 3 | 87.87 | 2 |
| 19 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.25 | 3 | 88.00 | 2 |
| 20 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.25 | 3 | 88.00 | 2 |
| 21 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.25 | 3 | 88.00 | 2 |
| 22 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.25 | 3 | 88.00 | 2 |
| 23 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.30 | 3 | 88.02 | 2 |
| 24 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.32 | 3 | 88.03 | 2 |
| 25 | 83.75 | A 83.75, B 83.75, C 83.75 | 92.32 | 3 | 88.03 | 2 |
| 26 | 85.00 | A 87.5, B 83.75, C 83.75 | 92.32 | 3 | 88.65 | 2 |
| 27 | 86.50 | A 90.12, B 83.75, C 85.62 | 92.23 | 2 | 89.03 | 2 |
| 28 | 87.99 | A 90.12, B 86.9, C 86.94 | 90.06 | 2 | 88.52 | 2 |
| 29 | 89.04 | A 90.12, B 88.5, C 88.51 | 90.17 | 2 | 89.39 | 2 |
| 30 | 89.58 | A 90.12, B 89.3, C 89.31 | 90.20 | 2 | 89.81 | 2 |
