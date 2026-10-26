# Run report: 20261021T164833Z_stage2_mini-low_anchor_44e1b9

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1206; tokens in 2,775,594; tokens out 421,076
- Cost: estimated $1.9072; actual $1.7839592 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164833Z_stage2_mini-low_anchor_44e1b9/manifest.json` (committed copy of `runs/stage2/20261021T164833Z_stage2_mini-low_anchor_44e1b9/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0680356, seller $0.7159236

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r001 | 1 | completed |  | 30/30 | 159.74 | 151 | 0 | 0 | OpenAI | 0.2254916 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r002 | 2 | completed |  | 30/30 | 156.67 | 150 | 0 | 0 | OpenAI | 0.2184892 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r003 | 3 | completed |  | 30/30 | 110.69 | 150 | 0 | 0 | OpenAI | 0.2222712 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r004 | 4 | completed |  | 30/30 | 197.29 | 150 | 0 | 0 | OpenAI | 0.2239836 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r005 | 5 | completed |  | 30/30 | 146.75 | 155 | 0 | 0 | OpenAI | 0.2219640 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r006 | 6 | completed |  | 30/30 | 117.66 | 150 | 0 | 0 | OpenAI | 0.2205908 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r007 | 7 | completed |  | 30/30 | 110.31 | 150 | 0 | 0 | OpenAI | 0.2233408 |
| 20261021T164833Z_stage2_mini-low_anchor_44e1b9_r008 | 8 | completed |  | 30/30 | 122.31 | 150 | 0 | 0 | OpenAI | 0.2278280 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
