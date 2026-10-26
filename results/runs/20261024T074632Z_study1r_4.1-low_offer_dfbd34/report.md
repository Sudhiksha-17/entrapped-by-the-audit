# Run report: 20261024T074632Z_study1r_4.1-low_offer_dfbd34

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,638,541; tokens out 446,812
- Cost: estimated $9.9112; actual $8.7982020 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074632Z_study1r_4.1-low_offer_dfbd34/manifest.json` (committed copy of `runs/study1r/20261024T074632Z_study1r_4.1-low_offer_dfbd34/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.9577680, probe $0.2383340, seller $3.6021000

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r009 | 9 | completed |  | 30/30 | 97.79 | 154 | 0 | 0 | OpenAI | 1.0885120 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r010 | 10 | completed |  | 30/30 | 99.17 | 154 | 0 | 0 | OpenAI | 1.1173000 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r011 | 11 | completed |  | 30/30 | 107.29 | 154 | 0 | 0 | OpenAI | 1.0399860 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r012 | 12 | completed |  | 30/30 | 101.32 | 154 | 0 | 0 | OpenAI | 1.1172120 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r013 | 13 | completed |  | 30/30 | 236.69 | 154 | 0 | 0 | OpenAI | 1.0878100 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r014 | 14 | completed |  | 30/30 | 99.97 | 154 | 0 | 0 | OpenAI | 1.1085200 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r015 | 15 | completed |  | 30/30 | 137.95 | 154 | 0 | 0 | OpenAI | 1.1462520 |
| 20261024T074632Z_study1r_4.1-low_offer_dfbd34_r016 | 16 | completed |  | 30/30 | 107.22 | 154 | 0 | 0 | OpenAI | 1.0926100 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
