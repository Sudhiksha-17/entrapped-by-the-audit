# Run report: 20261024T070258Z_study1r_4.1-low_offer_786ec3

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,669,592; tokens out 445,298
- Cost: estimated $9.9112; actual $8.8618240 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070258Z_study1r_4.1-low_offer_786ec3/manifest.json` (committed copy of `runs/study1r/20261024T070258Z_study1r_4.1-low_offer_786ec3/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.9771200, probe $0.2498960, seller $3.6348080

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r001 | 1 | completed |  | 30/30 | 126.69 | 154 | 0 | 0 | OpenAI | 1.1147960 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r002 | 2 | completed |  | 30/30 | 104.35 | 154 | 0 | 0 | OpenAI | 1.1281820 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r003 | 3 | completed |  | 30/30 | 126.06 | 154 | 0 | 0 | OpenAI | 1.1140520 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r004 | 4 | completed |  | 30/30 | 134.76 | 154 | 0 | 0 | OpenAI | 1.0952500 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r005 | 5 | completed |  | 30/30 | 112.68 | 154 | 0 | 0 | OpenAI | 1.1454580 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r006 | 6 | completed |  | 30/30 | 99.79 | 154 | 0 | 0 | OpenAI | 1.1161540 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r007 | 7 | completed |  | 30/30 | 114.14 | 154 | 0 | 0 | OpenAI | 1.0492680 |
| 20261024T070258Z_study1r_4.1-low_offer_786ec3_r008 | 8 | completed |  | 30/30 | 106.06 | 154 | 0 | 0 | OpenAI | 1.0986640 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
