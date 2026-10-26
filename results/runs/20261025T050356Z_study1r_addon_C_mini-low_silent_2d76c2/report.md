# Run report: 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 25-32 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-C confirmatory blocks 25-32 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,863,580; tokens out 406,189
- Cost: estimated $1.9624; actual $1.7797824 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0433736, probe $0.0355760, seller $0.7008328

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r025 | 25 | completed |  | 30/30 | 100.73 | 154 | 0 | 0 | OpenAI | 0.2183612 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r026 | 26 | completed |  | 30/30 | 92.95 | 154 | 0 | 0 | OpenAI | 0.2223668 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r027 | 27 | completed |  | 30/30 | 101.65 | 154 | 0 | 0 | OpenAI | 0.2225604 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r028 | 28 | completed |  | 30/30 | 92.04 | 154 | 0 | 0 | OpenAI | 0.2199968 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r029 | 29 | completed |  | 30/30 | 91.86 | 154 | 0 | 0 | OpenAI | 0.2227680 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r030 | 30 | completed |  | 30/30 | 98.36 | 154 | 0 | 0 | OpenAI | 0.2249044 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r031 | 31 | completed |  | 30/30 | 90.2 | 154 | 0 | 0 | OpenAI | 0.2265460 |
| 20261025T050356Z_study1r_addon_C_mini-low_silent_2d76c2_r032 | 32 | completed |  | 30/30 | 98.59 | 154 | 0 | 0 | OpenAI | 0.2222788 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
