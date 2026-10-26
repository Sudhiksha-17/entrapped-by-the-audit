# Run report: 20261021T164834Z_stage2_mini-low_offer_d8ca28

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1203; tokens in 2,718,255; tokens out 424,748
- Cost: estimated $1.9072; actual $1.7663996 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164834Z_stage2_mini-low_offer_d8ca28/manifest.json` (committed copy of `runs/stage2/20261021T164834Z_stage2_mini-low_offer_d8ca28/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 1
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0587032, seller $0.7076964

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r001 | 1 | completed |  | 30/30 | 164.27 | 152 | 0 | 0 | OpenAI | 0.2200612 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r002 | 2 | completed |  | 30/30 | 117.95 | 150 | 0 | 0 | OpenAI | 0.2154484 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r003 | 3 | completed |  | 30/30 | 115.95 | 150 | 0 | 0 | OpenAI | 0.2242864 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r004 | 4 | completed |  | 30/30 | 101.21 | 150 | 0 | 0 | OpenAI | 0.2212844 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r005 | 5 | completed |  | 30/30 | 121.71 | 150 | 0 | 0 | OpenAI | 0.2259840 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r006 | 6 | completed |  | 30/30 | 110.3 | 150 | 0 | 0 | OpenAI | 0.2174148 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r007 | 7 | completed |  | 30/30 | 172.62 | 151 | 1 | 0 | OpenAI | 0.2211712 |
| 20261021T164834Z_stage2_mini-low_offer_d8ca28_r008 | 8 | completed |  | 30/30 | 116.11 | 150 | 0 | 0 | OpenAI | 0.2207492 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
