# Run report: 20261021T164835Z_stage2_4.1-high_offer_aefd5d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1202; tokens in 2,134,856; tokens out 440,801
- Cost: estimated $8.4984; actual $7.7943920 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164835Z_stage2_4.1-high_offer_aefd5d/manifest.json` (committed copy of `runs/stage2/20261021T164835Z_stage2_4.1-high_offer_aefd5d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5512860, seller $3.2431060

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r001 | 1 | completed |  | 30/30 | 249.7 | 151 | 0 | 0 | OpenAI | 0.9865480 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r002 | 2 | completed |  | 30/30 | 180.38 | 150 | 0 | 0 | OpenAI | 0.9884820 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r003 | 3 | completed |  | 30/30 | 194.08 | 151 | 0 | 0 | OpenAI | 0.9565040 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r004 | 4 | completed |  | 30/30 | 203.86 | 150 | 0 | 0 | OpenAI | 0.9563420 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r005 | 5 | completed |  | 30/30 | 189.74 | 150 | 0 | 0 | OpenAI | 0.9863340 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r006 | 6 | completed |  | 30/30 | 152.88 | 150 | 0 | 0 | OpenAI | 0.9533740 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r007 | 7 | completed |  | 30/30 | 151.03 | 150 | 0 | 0 | OpenAI | 0.9603160 |
| 20261021T164835Z_stage2_4.1-high_offer_aefd5d_r008 | 8 | completed |  | 30/30 | 221.31 | 150 | 0 | 0 | OpenAI | 1.0064920 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
