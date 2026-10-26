# Run report: 20261021T175657Z_stage2_mini-low_offer_5f508d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,726,882; tokens out 419,114
- Cost: estimated $1.9072; actual $1.7613352 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175657Z_stage2_mini-low_offer_5f508d/manifest.json` (committed copy of `runs/stage2/20261021T175657Z_stage2_mini-low_offer_5f508d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0541576, seller $0.7071776

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r009 | 9 | completed |  | 30/30 | 156.74 | 150 | 0 | 0 | OpenAI | 0.2123556 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r010 | 10 | completed |  | 30/30 | 188.19 | 150 | 0 | 0 | OpenAI | 0.2275340 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r011 | 11 | completed |  | 30/30 | 116.4 | 150 | 0 | 0 | OpenAI | 0.2229092 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r012 | 12 | completed |  | 30/30 | 135.5 | 150 | 0 | 0 | OpenAI | 0.2197364 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r013 | 13 | completed |  | 30/30 | 101.14 | 150 | 0 | 0 | OpenAI | 0.2200348 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r014 | 14 | completed |  | 30/30 | 116.38 | 150 | 0 | 0 | OpenAI | 0.2237516 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r015 | 15 | completed |  | 30/30 | 119.81 | 150 | 0 | 0 | OpenAI | 0.2193120 |
| 20261021T175657Z_stage2_mini-low_offer_5f508d_r016 | 16 | completed |  | 30/30 | 170.36 | 150 | 0 | 0 | OpenAI | 0.2157016 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
