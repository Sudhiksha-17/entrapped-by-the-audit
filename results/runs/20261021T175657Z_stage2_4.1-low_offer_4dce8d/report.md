# Run report: 20261021T175657Z_stage2_4.1-low_offer_4dce8d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1202; tokens in 2,598,195; tokens out 435,573
- Cost: estimated $8.5640; actual $8.6809740 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175657Z_stage2_4.1-low_offer_4dce8d/manifest.json` (committed copy of `runs/stage2/20261021T175657Z_stage2_4.1-low_offer_4dce8d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0855520, seller $3.5954220

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r009 | 9 | completed |  | 30/30 | 145.16 | 150 | 0 | 0 | OpenAI | 1.0539860 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r010 | 10 | completed |  | 30/30 | 186.61 | 151 | 0 | 0 | OpenAI | 1.0658000 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r011 | 11 | completed |  | 30/30 | 245.89 | 151 | 0 | 0 | OpenAI | 1.0671240 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r012 | 12 | completed |  | 30/30 | 176.55 | 150 | 0 | 0 | OpenAI | 1.1048360 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r013 | 13 | completed |  | 30/30 | 148.71 | 150 | 0 | 0 | OpenAI | 1.0674280 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r014 | 14 | completed |  | 30/30 | 135.07 | 150 | 0 | 0 | OpenAI | 1.0823280 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r015 | 15 | completed |  | 30/30 | 161.68 | 150 | 0 | 0 | OpenAI | 1.1064140 |
| 20261021T175657Z_stage2_4.1-low_offer_4dce8d_r016 | 16 | completed |  | 30/30 | 161.32 | 150 | 0 | 0 | OpenAI | 1.1330580 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
