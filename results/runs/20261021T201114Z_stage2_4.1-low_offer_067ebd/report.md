# Run report: 20261021T201114Z_stage2_4.1-low_offer_067ebd

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 25,26,27,28,29,30,31,32 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,522,517; tokens out 439,911
- Cost: estimated $8.5640; actual $8.5643220 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T201114Z_stage2_4.1-low_offer_067ebd/manifest.json` (committed copy of `runs/stage2/20261021T201114Z_stage2_4.1-low_offer_067ebd/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.9994500, seller $3.5648720

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r025 | 25 | completed |  | 30/30 | 189.1 | 150 | 0 | 0 | OpenAI | 1.0351620 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r026 | 26 | completed |  | 30/30 | 161.54 | 150 | 0 | 0 | OpenAI | 1.0928680 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r027 | 27 | completed |  | 30/30 | 144.04 | 150 | 0 | 0 | OpenAI | 1.1063480 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r028 | 28 | completed |  | 30/30 | 157.84 | 150 | 0 | 0 | OpenAI | 1.0643660 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r029 | 29 | completed |  | 30/30 | 146.15 | 150 | 0 | 0 | OpenAI | 1.0834000 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r030 | 30 | completed |  | 30/30 | 168.65 | 150 | 0 | 0 | OpenAI | 1.1244560 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r031 | 31 | completed |  | 30/30 | 127.71 | 150 | 0 | 0 | OpenAI | 1.0538860 |
| 20261021T201114Z_stage2_4.1-low_offer_067ebd_r032 | 32 | completed |  | 30/30 | 122.67 | 150 | 0 | 0 | OpenAI | 1.0038360 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
