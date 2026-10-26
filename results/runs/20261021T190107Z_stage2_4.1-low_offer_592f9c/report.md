# Run report: 20261021T190107Z_stage2_4.1-low_offer_592f9c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1201; tokens in 2,565,510; tokens out 437,493
- Cost: estimated $8.5640; actual $8.6265480 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190107Z_stage2_4.1-low_offer_592f9c/manifest.json` (committed copy of `runs/stage2/20261021T190107Z_stage2_4.1-low_offer_592f9c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 1
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0444260, seller $3.5821220

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r017 | 17 | completed |  | 30/30 | 195.1 | 150 | 0 | 0 | OpenAI | 1.1221620 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r018 | 18 | completed |  | 30/30 | 208.07 | 150 | 0 | 0 | OpenAI | 1.0990940 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r019 | 19 | completed |  | 30/30 | 250.3 | 150 | 0 | 0 | OpenAI | 1.1067020 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r020 | 20 | completed |  | 30/30 | 180.18 | 150 | 0 | 0 | OpenAI | 1.0763940 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r021 | 21 | completed |  | 30/30 | 171.02 | 151 | 1 | 0 | OpenAI | 1.0848200 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r022 | 22 | completed |  | 30/30 | 154.34 | 150 | 0 | 0 | OpenAI | 1.1242800 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r023 | 23 | completed |  | 30/30 | 142.81 | 150 | 0 | 0 | OpenAI | 1.0415020 |
| 20261021T190107Z_stage2_4.1-low_offer_592f9c_r024 | 24 | completed |  | 30/30 | 191.01 | 150 | 0 | 0 | OpenAI | 0.9715940 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
