# Run report: 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory blocks 25-32 (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-A confirmatory blocks 25-32 (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1234; tokens in 2,257,288; tokens out 439,876
- Cost: estimated $8.8688; actual $7.9815520 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 2
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5418920, probe $0.1985120, seller $3.2411480

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r025 | 25 | completed |  | 30/30 | 118.79 | 154 | 0 | 0 | OpenAI | 0.9996960 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r026 | 26 | completed |  | 30/30 | 127.04 | 155 | 1 | 0 | OpenAI | 0.9857620 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r027 | 27 | completed |  | 30/30 | 117.12 | 154 | 0 | 0 | OpenAI | 0.9841300 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r028 | 28 | completed |  | 30/30 | 106.99 | 155 | 1 | 0 | OpenAI | 1.0154340 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r029 | 29 | completed |  | 30/30 | 105.99 | 154 | 0 | 0 | OpenAI | 0.9968600 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r030 | 30 | completed |  | 30/30 | 109.71 | 154 | 0 | 0 | OpenAI | 0.9854300 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r031 | 31 | completed |  | 30/30 | 107.97 | 154 | 0 | 0 | OpenAI | 1.0308620 |
| 20261024T194540Z_study1r_addon_A_4.1-high_silent_c2ed7e_r032 | 32 | completed |  | 30/30 | 128.31 | 154 | 0 | 0 | OpenAI | 0.9833780 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
