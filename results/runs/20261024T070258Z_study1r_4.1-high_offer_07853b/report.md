# Run report: 20261024T070258Z_study1r_4.1-high_offer_07853b

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,256,813; tokens out 446,380
- Cost: estimated $8.8688; actual $8.0499140 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070258Z_study1r_4.1-high_offer_07853b/manifest.json` (committed copy of `runs/study1r/20261024T070258Z_study1r_4.1-high_offer_07853b/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5380360, probe $0.2124220, seller $3.2994560

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r001 | 1 | completed |  | 30/30 | 146.89 | 154 | 0 | 0 | OpenAI | 0.9913080 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r002 | 2 | completed |  | 30/30 | 107.21 | 154 | 0 | 0 | OpenAI | 0.9846860 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r003 | 3 | completed |  | 30/30 | 119.41 | 154 | 0 | 0 | OpenAI | 1.0115120 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r004 | 4 | completed |  | 30/30 | 137.07 | 154 | 0 | 0 | OpenAI | 1.0187280 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r005 | 5 | completed |  | 30/30 | 114.78 | 154 | 0 | 0 | OpenAI | 1.0218100 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r006 | 6 | completed |  | 30/30 | 103.7 | 154 | 0 | 0 | OpenAI | 1.0038300 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r007 | 7 | completed |  | 30/30 | 111.01 | 154 | 0 | 0 | OpenAI | 1.0452400 |
| 20261024T070258Z_study1r_4.1-high_offer_07853b_r008 | 8 | completed |  | 30/30 | 108.34 | 154 | 0 | 0 | OpenAI | 0.9728000 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
