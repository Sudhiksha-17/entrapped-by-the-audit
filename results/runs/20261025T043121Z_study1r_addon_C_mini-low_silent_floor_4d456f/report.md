# Run report: 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 9-16 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-C confirmatory blocks 9-16 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1233; tokens in 2,800,513; tokens out 427,023
- Cost: estimated $1.9624; actual $1.7896948 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0514376, probe $0.0370772, seller $0.7011800

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r009 | 9 | completed |  | 30/30 | 123.96 | 154 | 0 | 0 | OpenAI | 0.2242032 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r010 | 10 | completed |  | 30/30 | 102.03 | 154 | 0 | 0 | OpenAI | 0.2112480 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r011 | 11 | completed |  | 30/30 | 99.08 | 154 | 0 | 0 | OpenAI | 0.2309032 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r012 | 12 | completed |  | 30/30 | 112.98 | 154 | 0 | 0 | OpenAI | 0.2252268 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r013 | 13 | completed |  | 30/30 | 124.5 | 154 | 0 | 0 | OpenAI | 0.2266492 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r014 | 14 | completed |  | 30/30 | 158.78 | 155 | 0 | 0 | OpenAI | 0.2251520 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r015 | 15 | completed |  | 30/30 | 136.67 | 154 | 0 | 0 | OpenAI | 0.2295932 |
| 20261025T043121Z_study1r_addon_C_mini-low_silent_floor_4d456f_r016 | 16 | completed |  | 30/30 | 92.61 | 154 | 0 | 0 | OpenAI | 0.2167192 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
