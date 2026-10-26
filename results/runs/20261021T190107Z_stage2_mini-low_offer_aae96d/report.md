# Run report: 20261021T190107Z_stage2_mini-low_offer_aae96d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,791,949; tokens out 422,817
- Cost: estimated $1.9072; actual $1.7932868 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190107Z_stage2_mini-low_offer_aae96d/manifest.json` (committed copy of `runs/stage2/20261021T190107Z_stage2_mini-low_offer_aae96d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0705512, seller $0.7227356

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r017 | 17 | completed |  | 30/30 | 111.91 | 150 | 0 | 0 | OpenAI | 0.2253360 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r018 | 18 | completed |  | 30/30 | 135.66 | 150 | 0 | 0 | OpenAI | 0.2242612 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r019 | 19 | completed |  | 30/30 | 119.47 | 150 | 0 | 0 | OpenAI | 0.2212068 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r020 | 20 | completed |  | 30/30 | 123.25 | 150 | 0 | 0 | OpenAI | 0.2297152 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r021 | 21 | completed |  | 30/30 | 102.94 | 150 | 0 | 0 | OpenAI | 0.2229964 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r022 | 22 | completed |  | 30/30 | 174.09 | 150 | 0 | 0 | OpenAI | 0.2215420 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r023 | 23 | completed |  | 30/30 | 132.82 | 150 | 0 | 0 | OpenAI | 0.2266276 |
| 20261021T190107Z_stage2_mini-low_offer_aae96d_r024 | 24 | completed |  | 30/30 | 104.85 | 150 | 0 | 0 | OpenAI | 0.2216016 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
