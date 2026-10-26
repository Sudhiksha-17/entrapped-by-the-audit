# Run report: 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 25-32 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-C confirmatory blocks 25-32 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,818,061; tokens out 418,156
- Cost: estimated $1.9624; actual $1.7825652 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0438804, probe $0.0403672, seller $0.6983176

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r025 | 25 | completed |  | 30/30 | 102.88 | 154 | 0 | 0 | OpenAI | 0.2189164 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r026 | 26 | completed |  | 30/30 | 97.54 | 154 | 0 | 0 | OpenAI | 0.2283532 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r027 | 27 | completed |  | 30/30 | 100.0 | 154 | 0 | 0 | OpenAI | 0.2163124 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r028 | 28 | completed |  | 30/30 | 93.73 | 154 | 0 | 0 | OpenAI | 0.2176152 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r029 | 29 | completed |  | 30/30 | 92.85 | 154 | 0 | 0 | OpenAI | 0.2267688 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r030 | 30 | completed |  | 30/30 | 100.85 | 154 | 0 | 0 | OpenAI | 0.2244752 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r031 | 31 | completed |  | 30/30 | 92.05 | 154 | 0 | 0 | OpenAI | 0.2238412 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_floor_dd1feb_r032 | 32 | completed |  | 30/30 | 101.2 | 154 | 0 | 0 | OpenAI | 0.2262828 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
