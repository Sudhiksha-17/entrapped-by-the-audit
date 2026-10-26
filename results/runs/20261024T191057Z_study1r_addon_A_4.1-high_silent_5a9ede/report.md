# Run report: 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory blocks 9-16 (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-A confirmatory blocks 9-16 (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1235; tokens in 2,263,751; tokens out 436,664
- Cost: estimated $8.8688; actual $7.9701260 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 3
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5296980, probe $0.2049960, seller $3.2354320

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r009 | 9 | completed |  | 30/30 | 161.27 | 157 | 3 | 0 | OpenAI | 0.9902360 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r010 | 10 | completed |  | 30/30 | 185.26 | 154 | 0 | 0 | OpenAI | 0.9939200 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r011 | 11 | completed |  | 30/30 | 120.91 | 154 | 0 | 0 | OpenAI | 0.9844000 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r012 | 12 | completed |  | 30/30 | 129.92 | 154 | 0 | 0 | OpenAI | 1.0368240 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r013 | 13 | completed |  | 30/30 | 112.48 | 154 | 0 | 0 | OpenAI | 1.0168140 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r014 | 14 | completed |  | 30/30 | 105.8 | 154 | 0 | 0 | OpenAI | 0.9824780 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r015 | 15 | completed |  | 30/30 | 127.98 | 154 | 0 | 0 | OpenAI | 0.9836740 |
| 20261024T191057Z_study1r_addon_A_4.1-high_silent_5a9ede_r016 | 16 | completed |  | 30/30 | 120.64 | 154 | 0 | 0 | OpenAI | 0.9817800 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
