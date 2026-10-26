# Run report: 20261021T164835Z_stage2_4.1-medium_offer_17ccdb

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1205; tokens in 2,148,433; tokens out 438,052
- Cost: estimated $8.5640; actual $7.7995540 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164835Z_stage2_4.1-medium_offer_17ccdb/manifest.json` (committed copy of `runs/stage2/20261021T164835Z_stage2_4.1-medium_offer_17ccdb/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5874680, seller $3.2120860

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r001 | 1 | completed |  | 30/30 | 148.1 | 150 | 0 | 0 | OpenAI | 0.9617040 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r002 | 2 | completed |  | 30/30 | 175.98 | 150 | 0 | 0 | OpenAI | 0.9524500 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r003 | 3 | completed |  | 30/30 | 167.36 | 150 | 0 | 0 | OpenAI | 0.9868460 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r004 | 4 | completed |  | 30/30 | 191.73 | 150 | 0 | 0 | OpenAI | 0.9949480 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r005 | 5 | completed |  | 30/30 | 198.51 | 155 | 0 | 0 | OpenAI | 0.9887900 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r006 | 6 | completed |  | 30/30 | 174.54 | 150 | 0 | 0 | OpenAI | 0.9493660 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r007 | 7 | completed |  | 30/30 | 186.48 | 150 | 0 | 0 | OpenAI | 1.0021680 |
| 20261021T164835Z_stage2_4.1-medium_offer_17ccdb_r008 | 8 | completed |  | 30/30 | 139.35 | 150 | 0 | 0 | OpenAI | 0.9632820 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
