# Run report: 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 25-32 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-C confirmatory blocks 25-32 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,229,674; tokens out 440,997
- Cost: estimated $8.7608; actual $7.9335640 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5372760, probe $0.1969920, seller $3.1992960

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r025 | 25 | completed |  | 30/30 | 98.54 | 154 | 0 | 0 | OpenAI | 0.9967820 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r026 | 26 | completed |  | 30/30 | 97.64 | 154 | 0 | 0 | OpenAI | 1.0290340 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r027 | 27 | completed |  | 30/30 | 97.23 | 154 | 0 | 0 | OpenAI | 0.9951500 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r028 | 28 | completed |  | 30/30 | 89.2 | 154 | 0 | 0 | OpenAI | 0.9769300 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r029 | 29 | completed |  | 30/30 | 97.68 | 154 | 0 | 0 | OpenAI | 1.0003840 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r030 | 30 | completed |  | 30/30 | 112.78 | 154 | 0 | 0 | OpenAI | 0.9737820 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r031 | 31 | completed |  | 30/30 | 93.59 | 154 | 0 | 0 | OpenAI | 0.9794040 |
| 20261025T050356Z_study1r_addon_C_4.1-high_silent_floor_7c0dc4_r032 | 32 | completed |  | 30/30 | 95.38 | 154 | 0 | 0 | OpenAI | 0.9820980 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
