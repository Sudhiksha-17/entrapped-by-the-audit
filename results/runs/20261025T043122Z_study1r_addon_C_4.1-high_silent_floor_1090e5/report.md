# Run report: 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 9-16 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-C confirmatory blocks 9-16 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1233; tokens in 2,279,432; tokens out 443,821
- Cost: estimated $8.7608; actual $8.0535600 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5930120, probe $0.1960360, seller $3.2645120

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r009 | 9 | completed |  | 30/30 | 111.32 | 154 | 0 | 0 | OpenAI | 0.9903780 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r010 | 10 | completed |  | 30/30 | 99.11 | 154 | 0 | 0 | OpenAI | 0.9845760 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r011 | 11 | completed |  | 30/30 | 105.46 | 154 | 0 | 0 | OpenAI | 0.9896040 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r012 | 12 | completed |  | 30/30 | 118.88 | 154 | 0 | 0 | OpenAI | 0.9958080 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r013 | 13 | completed |  | 30/30 | 121.4 | 154 | 0 | 0 | OpenAI | 0.9929880 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r014 | 14 | completed |  | 30/30 | 144.89 | 154 | 0 | 0 | OpenAI | 0.9961420 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r015 | 15 | completed |  | 30/30 | 135.01 | 155 | 0 | 0 | OpenAI | 1.1049780 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_floor_1090e5_r016 | 16 | completed |  | 30/30 | 101.32 | 154 | 0 | 0 | OpenAI | 0.9990860 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
