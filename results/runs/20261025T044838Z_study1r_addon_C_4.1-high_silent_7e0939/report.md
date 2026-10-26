# Run report: 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 17-24 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R-C confirmatory blocks 17-24 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,207,111; tokens out 435,813
- Cost: estimated $8.7608; actual $7.8498460 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.4872220, probe $0.1901240, seller $3.1725000

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r017 | 17 | completed |  | 30/30 | 102.93 | 154 | 0 | 0 | OpenAI | 0.9677760 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r018 | 18 | completed |  | 30/30 | 89.1 | 154 | 0 | 0 | OpenAI | 0.9667680 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r019 | 19 | completed |  | 30/30 | 90.93 | 154 | 0 | 0 | OpenAI | 1.0129360 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r020 | 20 | completed |  | 30/30 | 94.4 | 154 | 0 | 0 | OpenAI | 1.0018680 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r021 | 21 | completed |  | 30/30 | 93.94 | 154 | 0 | 0 | OpenAI | 0.9681960 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r022 | 22 | completed |  | 30/30 | 104.04 | 154 | 0 | 0 | OpenAI | 0.9916100 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r023 | 23 | completed |  | 30/30 | 101.9 | 154 | 0 | 0 | OpenAI | 0.9596480 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_7e0939_r024 | 24 | completed |  | 30/30 | 103.07 | 154 | 0 | 0 | OpenAI | 0.9810440 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
