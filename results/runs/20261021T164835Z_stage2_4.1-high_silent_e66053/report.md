# Run report: 20261021T164835Z_stage2_4.1-high_silent_e66053

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1205; tokens in 2,119,940; tokens out 436,629
- Cost: estimated $8.4984; actual $7.7313760 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164835Z_stage2_4.1-high_silent_e66053/manifest.json` (committed copy of `runs/stage2/20261021T164835Z_stage2_4.1-high_silent_e66053/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.4949920, seller $3.2363840

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r001 | 1 | completed |  | 30/30 | 147.66 | 150 | 0 | 0 | OpenAI | 0.9580420 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r002 | 2 | completed |  | 30/30 | 157.26 | 150 | 0 | 0 | OpenAI | 0.9760540 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r003 | 3 | completed |  | 30/30 | 170.92 | 150 | 0 | 0 | OpenAI | 0.9701200 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r004 | 4 | completed |  | 30/30 | 185.2 | 150 | 0 | 0 | OpenAI | 0.9522720 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r005 | 5 | completed |  | 30/30 | 176.8 | 155 | 0 | 0 | OpenAI | 0.9591800 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r006 | 6 | completed |  | 30/30 | 148.01 | 150 | 0 | 0 | OpenAI | 0.9538560 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r007 | 7 | completed |  | 30/30 | 152.1 | 150 | 0 | 0 | OpenAI | 1.0076000 |
| 20261021T164835Z_stage2_4.1-high_silent_e66053_r008 | 8 | completed |  | 30/30 | 139.64 | 150 | 0 | 0 | OpenAI | 0.9542520 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
