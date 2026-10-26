# Run report: 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 1-8 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-C confirmatory blocks 1-8 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,876,543; tokens out 418,828
- Cost: estimated $1.9624; actual $1.8068028 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0499056, probe $0.0419080, seller $0.7149892

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r001 | 1 | completed |  | 30/30 | 92.66 | 154 | 0 | 0 | OpenAI | 0.2294976 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r002 | 2 | completed |  | 30/30 | 92.91 | 154 | 0 | 0 | OpenAI | 0.2262260 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r003 | 3 | completed |  | 30/30 | 93.68 | 154 | 0 | 0 | OpenAI | 0.2225284 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r004 | 4 | completed |  | 30/30 | 106.74 | 154 | 0 | 0 | OpenAI | 0.2271700 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r005 | 5 | completed |  | 30/30 | 100.89 | 154 | 0 | 0 | OpenAI | 0.2262036 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r006 | 6 | completed |  | 30/30 | 102.04 | 154 | 0 | 0 | OpenAI | 0.2220580 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r007 | 7 | completed |  | 30/30 | 101.49 | 154 | 0 | 0 | OpenAI | 0.2287896 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_floor_781ac4_r008 | 8 | completed |  | 30/30 | 96.5 | 154 | 0 | 0 | OpenAI | 0.2243296 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
