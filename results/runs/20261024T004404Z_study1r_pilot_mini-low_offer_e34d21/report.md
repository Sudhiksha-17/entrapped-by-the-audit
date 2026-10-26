# Run report: 20261024T004404Z_study1r_pilot_mini-low_offer_e34d21

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_pilot; run type: pilot
- Purpose: Study 1R pilot, first episode (mini-low offer, index 2000), approved in human message 40
- Command: `python -m sting.stage2_runner configs/study1r/pilot/campaign.yaml --arms mini-low_offer --indices 2000 --purpose Study 1R pilot, first episode (mini-low offer, index 2000), approved in human message 40`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 150; tokens in 337,473; tokens out 52,877
- Cost: estimated $0.2411; actual $0.2195924 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T004404Z_study1r_pilot_mini-low_offer_e34d21/manifest.json` (committed copy of `runs/study1r_pilot/20261024T004404Z_study1r_pilot_mini-low_offer_e34d21/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1272928, seller $0.0922996

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T004404Z_study1r_pilot_mini-low_offer_e34d21_r2000 | 2000 | completed |  | 30/30 | 111.57 | 150 | 0 | 0 | OpenAI | 0.2195924 |

## Per round: 20261024T004404Z_study1r_pilot_mini-low_offer_e34d21_r2000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 92.50 | A 85.0, B 95.0, C 97.5 | 83.53 | 0 |  | 2 |
| 2 | 86.33 | A 84.5, B 84.5, C 90.0 | 84.53 | 2 | 84.62 | 2 |
| 3 | 84.42 | A 84.25, B 84.5, C 84.5 | 85.07 | 2 | 84.94 | 2 |
| 4 | 84.38 | A 84.25, B 84.5, C 84.38 | 84.38 | 1 | 84.38 | 2 |
| 5 | 84.38 | A 84.4, B 84.35, C 84.38 | 84.37 | 1 | 84.38 | 2 |
| 6 | 84.37 | A 84.37, B 84.35, C 84.38 | 84.38 | 2 | 84.38 | 2 |
| 7 | 84.36 | A 84.37, B 84.35, C 84.36 | 84.38 | 3 | 84.37 | 2 |
| 8 | 84.36 | A 84.37, B 84.35, C 84.36 | 84.37 | 2 | 84.37 | 2 |
| 9 | 84.36 | A 84.37, B 84.35, C 84.36 | 84.38 | 3 | 84.37 | 2 |
| 10 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.37 | 2 | 84.37 | 3 |
| 11 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 12 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 13 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 14 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 15 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 16 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 17 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 18 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 19 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 20 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 21 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 22 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 23 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 24 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 25 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 26 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 27 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 28 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 29 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.38 | 2 | 84.37 | 3 |
| 30 | 86.97 | A 84.37, B 84.35, C 92.18 | 84.44 | 2 | 84.40 | 2 |
