# Run report: 20261021T190108Z_stage2_4.1-high_silent_b6d7a0

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,188,553; tokens out 435,228
- Cost: estimated $8.4984; actual $7.8589300 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190108Z_stage2_4.1-high_silent_b6d7a0/manifest.json` (committed copy of `runs/stage2/20261021T190108Z_stage2_4.1-high_silent_b6d7a0/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5852400, seller $3.2736900

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r017 | 17 | completed |  | 30/30 | 193.51 | 150 | 0 | 0 | OpenAI | 0.9518860 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r018 | 18 | completed |  | 30/30 | 213.71 | 150 | 0 | 0 | OpenAI | 1.0460400 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r019 | 19 | completed |  | 30/30 | 191.85 | 150 | 0 | 0 | OpenAI | 0.9638120 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r020 | 20 | completed |  | 30/30 | 195.22 | 150 | 0 | 0 | OpenAI | 1.0067120 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r021 | 21 | completed |  | 30/30 | 166.23 | 150 | 0 | 0 | OpenAI | 0.9908460 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r022 | 22 | completed |  | 30/30 | 182.13 | 150 | 0 | 0 | OpenAI | 0.9661880 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r023 | 23 | completed |  | 30/30 | 125.11 | 150 | 0 | 0 | OpenAI | 0.9852860 |
| 20261021T190108Z_stage2_4.1-high_silent_b6d7a0_r024 | 24 | completed |  | 30/30 | 167.4 | 150 | 0 | 0 | OpenAI | 0.9481600 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
