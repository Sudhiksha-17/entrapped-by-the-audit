# Run report: 20261021T201114Z_stage2_4.1-medium_silent_7f3280

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 25,26,27,28,29,30,31,32 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1201; tokens in 2,264,442; tokens out 431,395
- Cost: estimated $8.5640; actual $7.9800440 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T201114Z_stage2_4.1-medium_silent_7f3280/manifest.json` (committed copy of `runs/stage2/20261021T201114Z_stage2_4.1-medium_silent_7f3280/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.6946420, seller $3.2854020

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r025 | 25 | completed |  | 30/30 | 164.21 | 150 | 0 | 0 | OpenAI | 1.0188820 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r026 | 26 | completed |  | 30/30 | 171.25 | 150 | 0 | 0 | OpenAI | 0.9756660 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r027 | 27 | completed |  | 30/30 | 132.64 | 150 | 0 | 0 | OpenAI | 0.9921320 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r028 | 28 | completed |  | 30/30 | 142.16 | 150 | 0 | 0 | OpenAI | 0.9511840 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r029 | 29 | completed |  | 30/30 | 132.08 | 151 | 0 | 0 | OpenAI | 1.0600120 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r030 | 30 | completed |  | 30/30 | 157.46 | 150 | 0 | 0 | OpenAI | 0.9854040 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r031 | 31 | completed |  | 30/30 | 155.06 | 150 | 0 | 0 | OpenAI | 0.9991840 |
| 20261021T201114Z_stage2_4.1-medium_silent_7f3280_r032 | 32 | completed |  | 30/30 | 117.11 | 150 | 0 | 0 | OpenAI | 0.9975800 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
