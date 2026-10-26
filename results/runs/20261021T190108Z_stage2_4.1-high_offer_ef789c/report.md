# Run report: 20261021T190108Z_stage2_4.1-high_offer_ef789c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,132,999; tokens out 436,921
- Cost: estimated $8.4984; actual $7.7613660 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190108Z_stage2_4.1-high_offer_ef789c/manifest.json` (committed copy of `runs/stage2/20261021T190108Z_stage2_4.1-high_offer_ef789c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5192040, seller $3.2421620

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r017 | 17 | completed |  | 30/30 | 177.44 | 150 | 0 | 0 | OpenAI | 0.9600100 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r018 | 18 | completed |  | 30/30 | 200.0 | 150 | 0 | 0 | OpenAI | 0.9812760 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r019 | 19 | completed |  | 30/30 | 194.71 | 150 | 0 | 0 | OpenAI | 0.9671420 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r020 | 20 | completed |  | 30/30 | 172.34 | 150 | 0 | 0 | OpenAI | 0.9932820 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r021 | 21 | completed |  | 30/30 | 176.51 | 150 | 0 | 0 | OpenAI | 0.9888680 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r022 | 22 | completed |  | 30/30 | 192.35 | 150 | 0 | 0 | OpenAI | 0.9447620 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r023 | 23 | completed |  | 30/30 | 143.13 | 150 | 0 | 0 | OpenAI | 0.9776520 |
| 20261021T190108Z_stage2_4.1-high_offer_ef789c_r024 | 24 | completed |  | 30/30 | 185.06 | 150 | 0 | 0 | OpenAI | 0.9483740 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
