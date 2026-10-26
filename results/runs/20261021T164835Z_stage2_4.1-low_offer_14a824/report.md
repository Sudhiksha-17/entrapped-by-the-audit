# Run report: 20261021T164835Z_stage2_4.1-low_offer_14a824

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1201; tokens in 2,632,602; tokens out 435,485
- Cost: estimated $8.5640; actual $8.7490840 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164835Z_stage2_4.1-low_offer_14a824/manifest.json` (committed copy of `runs/stage2/20261021T164835Z_stage2_4.1-low_offer_14a824/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.1006820, seller $3.6484020

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r001 | 1 | completed |  | 30/30 | 196.54 | 151 | 0 | 0 | OpenAI | 1.1309860 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r002 | 2 | completed |  | 30/30 | 173.12 | 150 | 0 | 0 | OpenAI | 1.1195500 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r003 | 3 | completed |  | 30/30 | 169.87 | 150 | 0 | 0 | OpenAI | 1.0438660 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r004 | 4 | completed |  | 30/30 | 164.62 | 150 | 0 | 0 | OpenAI | 1.0787360 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r005 | 5 | completed |  | 30/30 | 163.98 | 150 | 0 | 0 | OpenAI | 1.1055240 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r006 | 6 | completed |  | 30/30 | 166.71 | 150 | 0 | 0 | OpenAI | 1.0744420 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r007 | 7 | completed |  | 30/30 | 145.75 | 150 | 0 | 0 | OpenAI | 1.1216180 |
| 20261021T164835Z_stage2_4.1-low_offer_14a824_r008 | 8 | completed |  | 30/30 | 134.07 | 150 | 0 | 0 | OpenAI | 1.0743620 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
