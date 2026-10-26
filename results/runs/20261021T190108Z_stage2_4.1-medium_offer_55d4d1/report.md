# Run report: 20261021T190108Z_stage2_4.1-medium_offer_55d4d1

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,139,466; tokens out 436,340
- Cost: estimated $8.5640; actual $7.7696520 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190108Z_stage2_4.1-medium_offer_55d4d1/manifest.json` (committed copy of `runs/stage2/20261021T190108Z_stage2_4.1-medium_offer_55d4d1/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5886760, seller $3.1809760

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r017 | 17 | completed |  | 30/30 | 173.96 | 150 | 0 | 0 | OpenAI | 0.9618820 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r018 | 18 | completed |  | 30/30 | 206.86 | 150 | 0 | 0 | OpenAI | 0.9638160 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r019 | 19 | completed |  | 30/30 | 187.08 | 150 | 0 | 0 | OpenAI | 0.9592060 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r020 | 20 | completed |  | 30/30 | 202.73 | 150 | 0 | 0 | OpenAI | 0.9756720 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r021 | 21 | completed |  | 30/30 | 176.52 | 150 | 0 | 0 | OpenAI | 0.9628500 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r022 | 22 | completed |  | 30/30 | 158.91 | 150 | 0 | 0 | OpenAI | 1.0221080 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r023 | 23 | completed |  | 30/30 | 149.35 | 150 | 0 | 0 | OpenAI | 0.9561280 |
| 20261021T190108Z_stage2_4.1-medium_offer_55d4d1_r024 | 24 | completed |  | 30/30 | 162.5 | 150 | 0 | 0 | OpenAI | 0.9679900 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
