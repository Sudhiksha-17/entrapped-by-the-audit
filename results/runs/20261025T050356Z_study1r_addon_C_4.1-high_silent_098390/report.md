# Run report: 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 25-32 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-C confirmatory blocks 25-32 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,223,660; tokens out 444,305
- Cost: estimated $8.7608; actual $7.9725760 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T050356Z_study1r_addon_C_4.1-high_silent_098390/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T050356Z_study1r_addon_C_4.1-high_silent_098390/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5379280, probe $0.2166680, seller $3.2179800

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r025 | 25 | completed |  | 30/30 | 102.43 | 154 | 0 | 0 | OpenAI | 1.0328400 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r026 | 26 | completed |  | 30/30 | 95.98 | 154 | 0 | 0 | OpenAI | 0.9868240 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r027 | 27 | completed |  | 30/30 | 94.19 | 154 | 0 | 0 | OpenAI | 1.0017640 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r028 | 28 | completed |  | 30/30 | 90.08 | 154 | 0 | 0 | OpenAI | 0.9883440 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r029 | 29 | completed |  | 30/30 | 103.54 | 154 | 0 | 0 | OpenAI | 0.9846560 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r030 | 30 | completed |  | 30/30 | 105.06 | 154 | 0 | 0 | OpenAI | 0.9979000 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r031 | 31 | completed |  | 30/30 | 96.17 | 154 | 0 | 0 | OpenAI | 0.9942780 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_098390_r032 | 32 | completed |  | 30/30 | 94.47 | 154 | 0 | 0 | OpenAI | 0.9859700 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
