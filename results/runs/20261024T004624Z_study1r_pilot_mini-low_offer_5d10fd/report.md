# Run report: 20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_pilot; run type: pilot
- Purpose: Study 1R pilot, remaining episodes part 1 (mini-low offer 2001), human message 40
- Command: `python -m sting.stage2_runner configs/study1r/pilot/campaign.yaml --arms mini-low_offer --indices 2001 --purpose Study 1R pilot, remaining episodes part 1 (mini-low offer 2001), human message 40`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 150; tokens in 350,585; tokens out 52,914
- Cost: estimated $0.2411; actual $0.2248964 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd/manifest.json` (committed copy of `runs/study1r_pilot/20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1316576, seller $0.0932388

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd_r2001 | 2001 | completed |  | 30/30 | 95.08 | 150 | 0 | 0 | OpenAI | 0.2248964 |

## Per round: 20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd_r2001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 88.83 | A 85.0, B 84.0, C 97.5 | 91.50 | 2 | 89.88 | 2 |
| 2 | 84.33 | A 84.5, B 84.0, C 84.5 | 92.33 | 3 | 88.33 | 2 |
| 3 | 84.17 | A 84.25, B 84.0, C 84.25 | 93.08 | 3 | 88.63 | 2 |
| 4 | 84.04 | A 84.0, B 84.0, C 84.12 | 93.33 | 3 | 88.69 | 2 |
| 5 | 84.00 | A 84.0, B 84.0, C 84.0 | 93.50 | 3 | 88.75 | 2 |
| 6 | 84.00 | A 84.0, B 84.0, C 84.0 | 92.25 | 3 | 88.13 | 2 |
| 7 | 84.00 | A 84.0, B 84.0, C 84.0 | 89.92 | 3 | 86.96 | 2 |
| 8 | 84.00 | A 84.0, B 84.0, C 84.0 | 89.54 | 3 | 86.77 | 2 |
| 9 | 84.00 | A 84.0, B 84.0, C 84.0 | 88.75 | 3 | 86.38 | 2 |
| 10 | 86.67 | A 84.0, B 84.0, C 92.0 | 87.92 | 2 | 86.44 | 3 |
| 11 | 86.67 | A 84.0, B 84.0, C 92.0 | 88.08 | 2 | 86.56 | 3 |
| 12 | 86.83 | A 84.5, B 84.0, C 92.0 | 88.17 | 2 | 86.75 | 3 |
| 13 | 86.83 | A 84.5, B 84.0, C 92.0 | 88.21 | 2 | 86.78 | 3 |
| 14 | 87.00 | A 85.0, B 84.0, C 92.0 | 88.25 | 2 | 86.94 | 3 |
| 15 | 87.00 | A 85.0, B 84.0, C 92.0 | 88.33 | 2 | 87.00 | 3 |
| 16 | 87.17 | A 85.5, B 84.0, C 92.0 | 88.42 | 2 | 87.19 | 3 |
| 17 | 87.25 | A 85.75, B 84.0, C 92.0 | 88.50 | 2 | 87.31 | 3 |
| 18 | 87.29 | A 85.88, B 84.0, C 92.0 | 88.58 | 2 | 87.41 | 3 |
| 19 | 87.58 | A 85.75, B 85.0, C 92.0 | 88.67 | 2 | 87.69 | 3 |
| 20 | 87.50 | A 85.5, B 85.0, C 92.0 | 88.75 | 2 | 87.69 | 3 |
| 21 | 87.42 | A 85.25, B 85.0, C 92.0 | 88.83 | 2 | 87.69 | 3 |
| 22 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.87 | 2 | 87.65 | 3 |
| 23 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 24 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 25 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 26 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 27 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 28 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 29 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 3 |
| 30 | 87.33 | A 85.0, B 85.0, C 92.0 | 88.88 | 2 | 87.66 | 2 |
