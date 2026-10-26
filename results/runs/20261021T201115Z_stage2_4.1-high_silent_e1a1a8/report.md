# Run report: 20261021T201115Z_stage2_4.1-high_silent_e1a1a8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 25,26,27,28,29,30,31,32 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1201; tokens in 2,151,208; tokens out 432,911
- Cost: estimated $8.4984; actual $7.7657040 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T201115Z_stage2_4.1-high_silent_e1a1a8/manifest.json` (committed copy of `runs/stage2/20261021T201115Z_stage2_4.1-high_silent_e1a1a8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5324840, seller $3.2332200

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r025 | 25 | completed |  | 30/30 | 162.26 | 150 | 0 | 0 | OpenAI | 1.0092400 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r026 | 26 | completed |  | 30/30 | 167.2 | 150 | 0 | 0 | OpenAI | 0.9477960 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r027 | 27 | completed |  | 30/30 | 170.15 | 150 | 0 | 0 | OpenAI | 0.9684280 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r028 | 28 | completed |  | 30/30 | 137.76 | 150 | 0 | 0 | OpenAI | 0.9944700 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r029 | 29 | completed |  | 30/30 | 122.91 | 150 | 0 | 0 | OpenAI | 0.9589640 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r030 | 30 | completed |  | 30/30 | 171.95 | 151 | 0 | 0 | OpenAI | 0.9620440 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r031 | 31 | completed |  | 30/30 | 176.66 | 150 | 0 | 0 | OpenAI | 0.9685780 |
| 20261021T201115Z_stage2_4.1-high_silent_e1a1a8_r032 | 32 | completed |  | 30/30 | 126.68 | 150 | 0 | 0 | OpenAI | 0.9561840 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
