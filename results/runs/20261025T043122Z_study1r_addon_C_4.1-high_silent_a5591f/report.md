# Run report: 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 9-16 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-C confirmatory blocks 9-16 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1233; tokens in 2,280,698; tokens out 436,913
- Cost: estimated $8.7608; actual $8.0040920 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5574720, probe $0.2007680, seller $3.2458520

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r009 | 9 | completed |  | 30/30 | 100.97 | 154 | 0 | 0 | OpenAI | 1.0130380 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r010 | 10 | completed |  | 30/30 | 94.54 | 154 | 0 | 0 | OpenAI | 0.9696860 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r011 | 11 | completed |  | 30/30 | 102.46 | 154 | 0 | 0 | OpenAI | 0.9944980 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r012 | 12 | completed |  | 30/30 | 125.39 | 154 | 0 | 0 | OpenAI | 0.9824700 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r013 | 13 | completed |  | 30/30 | 138.54 | 154 | 0 | 0 | OpenAI | 0.9898280 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r014 | 14 | completed |  | 30/30 | 145.47 | 154 | 0 | 0 | OpenAI | 1.0048800 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r015 | 15 | completed |  | 30/30 | 132.34 | 155 | 0 | 0 | OpenAI | 1.0626540 |
| 20261025T043122Z_study1r_addon_C_4.1-high_silent_a5591f_r016 | 16 | completed |  | 30/30 | 98.71 | 154 | 0 | 0 | OpenAI | 0.9870380 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
