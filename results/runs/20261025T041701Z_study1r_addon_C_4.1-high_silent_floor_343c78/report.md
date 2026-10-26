# Run report: 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 1-8 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-C confirmatory blocks 1-8 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,245,956; tokens out 446,424
- Cost: estimated $8.7608; actual $8.0206800 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5622200, probe $0.2103680, seller $3.2480920

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r001 | 1 | completed |  | 30/30 | 99.76 | 154 | 0 | 0 | OpenAI | 0.9934140 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r002 | 2 | completed |  | 30/30 | 96.41 | 154 | 0 | 0 | OpenAI | 0.9938520 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r003 | 3 | completed |  | 30/30 | 103.82 | 154 | 0 | 0 | OpenAI | 1.0137820 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r004 | 4 | completed |  | 30/30 | 97.89 | 154 | 0 | 0 | OpenAI | 1.0030180 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r005 | 5 | completed |  | 30/30 | 105.51 | 154 | 0 | 0 | OpenAI | 0.9971800 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r006 | 6 | completed |  | 30/30 | 99.94 | 154 | 0 | 0 | OpenAI | 0.9782000 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r007 | 7 | completed |  | 30/30 | 108.6 | 154 | 0 | 0 | OpenAI | 1.0236680 |
| 20261025T041701Z_study1r_addon_C_4.1-high_silent_floor_343c78_r008 | 8 | completed |  | 30/30 | 115.21 | 154 | 0 | 0 | OpenAI | 1.0175660 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
