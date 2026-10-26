# Run report: 20261024T074633Z_study1r_4.1-high_offer_d8a720

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,280,098; tokens out 445,371
- Cost: estimated $8.8688; actual $8.0937880 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074633Z_study1r_4.1-high_offer_d8a720/manifest.json` (committed copy of `runs/study1r/20261024T074633Z_study1r_4.1-high_offer_d8a720/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5329220, probe $0.2279740, seller $3.3328920

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r009 | 9 | completed |  | 30/30 | 101.66 | 154 | 0 | 0 | OpenAI | 0.9848600 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r010 | 10 | completed |  | 30/30 | 97.45 | 154 | 0 | 0 | OpenAI | 1.0308520 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r011 | 11 | completed |  | 30/30 | 95.47 | 154 | 0 | 0 | OpenAI | 1.0129780 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r012 | 12 | completed |  | 30/30 | 106.98 | 154 | 0 | 0 | OpenAI | 1.0298720 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r013 | 13 | completed |  | 30/30 | 137.12 | 154 | 0 | 0 | OpenAI | 0.9821840 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r014 | 14 | completed |  | 30/30 | 93.31 | 154 | 0 | 0 | OpenAI | 0.9757000 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r015 | 15 | completed |  | 30/30 | 133.35 | 154 | 0 | 0 | OpenAI | 1.0041440 |
| 20261024T074633Z_study1r_4.1-high_offer_d8a720_r016 | 16 | completed |  | 30/30 | 108.93 | 154 | 0 | 0 | OpenAI | 1.0731980 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
