# Run report: 20261021T190107Z_stage2_4.1-low_silent_e91bca

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,604,200; tokens out 432,710
- Cost: estimated $8.5640; actual $8.6700800 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190107Z_stage2_4.1-low_silent_e91bca/manifest.json` (committed copy of `runs/stage2/20261021T190107Z_stage2_4.1-low_silent_e91bca/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0600740, seller $3.6100060

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r017 | 17 | completed |  | 30/30 | 181.49 | 150 | 0 | 0 | OpenAI | 1.0860500 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r018 | 18 | completed |  | 30/30 | 189.36 | 150 | 0 | 0 | OpenAI | 1.0873580 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r019 | 19 | completed |  | 30/30 | 187.07 | 150 | 0 | 0 | OpenAI | 1.0454440 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r020 | 20 | completed |  | 30/30 | 174.79 | 150 | 0 | 0 | OpenAI | 1.1049460 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r021 | 21 | completed |  | 30/30 | 159.96 | 150 | 0 | 0 | OpenAI | 1.0975640 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r022 | 22 | completed |  | 30/30 | 200.59 | 150 | 0 | 0 | OpenAI | 1.0546520 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r023 | 23 | completed |  | 30/30 | 134.97 | 150 | 0 | 0 | OpenAI | 1.1040820 |
| 20261021T190107Z_stage2_4.1-low_silent_e91bca_r024 | 24 | completed |  | 30/30 | 157.68 | 150 | 0 | 0 | OpenAI | 1.0899840 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
