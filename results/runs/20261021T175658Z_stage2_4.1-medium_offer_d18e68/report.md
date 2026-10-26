# Run report: 20261021T175658Z_stage2_4.1-medium_offer_d18e68

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,240,062; tokens out 435,539
- Cost: estimated $8.5640; actual $7.9644360 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175658Z_stage2_4.1-medium_offer_d18e68/manifest.json` (committed copy of `runs/stage2/20261021T175658Z_stage2_4.1-medium_offer_d18e68/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.7227460, seller $3.2416900

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r009 | 9 | completed |  | 30/30 | 148.5 | 150 | 0 | 0 | OpenAI | 0.9617400 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r010 | 10 | completed |  | 30/30 | 189.23 | 150 | 0 | 0 | OpenAI | 0.9788760 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r011 | 11 | completed |  | 30/30 | 176.16 | 150 | 0 | 0 | OpenAI | 1.0088080 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r012 | 12 | completed |  | 30/30 | 198.45 | 150 | 0 | 0 | OpenAI | 1.0884540 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r013 | 13 | completed |  | 30/30 | 184.63 | 150 | 0 | 0 | OpenAI | 0.9677540 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r014 | 14 | completed |  | 30/30 | 157.31 | 150 | 0 | 0 | OpenAI | 0.9520480 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r015 | 15 | completed |  | 30/30 | 168.4 | 150 | 0 | 0 | OpenAI | 1.0258000 |
| 20261021T175658Z_stage2_4.1-medium_offer_d18e68_r016 | 16 | completed |  | 30/30 | 169.6 | 150 | 0 | 0 | OpenAI | 0.9809560 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
