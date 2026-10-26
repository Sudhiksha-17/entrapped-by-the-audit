# Run report: 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory blocks 9-16 (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-A confirmatory blocks 9-16 (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1233; tokens in 2,231,236; tokens out 446,534
- Cost: estimated $8.8688; actual $7.9832880 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 1
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5334580, probe $0.1921800, seller $3.2576500

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r009 | 9 | completed |  | 30/30 | 162.04 | 155 | 1 | 0 | OpenAI | 0.9931020 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r010 | 10 | completed |  | 30/30 | 184.99 | 154 | 0 | 0 | OpenAI | 0.9958460 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r011 | 11 | completed |  | 30/30 | 114.04 | 154 | 0 | 0 | OpenAI | 0.9857040 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r012 | 12 | completed |  | 30/30 | 138.83 | 154 | 0 | 0 | OpenAI | 1.0429540 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r013 | 13 | completed |  | 30/30 | 120.99 | 154 | 0 | 0 | OpenAI | 1.0021620 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r014 | 14 | completed |  | 30/30 | 113.21 | 154 | 0 | 0 | OpenAI | 1.0027000 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r015 | 15 | completed |  | 30/30 | 124.08 | 154 | 0 | 0 | OpenAI | 0.9900620 |
| 20261024T191057Z_study1r_addon_A_4.1-high_competitive_05b9f8_r016 | 16 | completed |  | 30/30 | 136.88 | 154 | 0 | 0 | OpenAI | 0.9707580 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
