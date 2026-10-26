# Run report: 20261021T175656Z_stage2_mini-low_rapport_691757

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,747,792; tokens out 398,557
- Cost: estimated $1.9072; actual $1.7368080 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175656Z_stage2_mini-low_rapport_691757/manifest.json` (committed copy of `runs/stage2/20261021T175656Z_stage2_mini-low_rapport_691757/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition rapport, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0399556, seller $0.6968524

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175656Z_stage2_mini-low_rapport_691757_r009 | 9 | completed |  | 30/30 | 110.81 | 150 | 0 | 0 | OpenAI | 0.2204148 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r010 | 10 | completed |  | 30/30 | 135.65 | 150 | 0 | 0 | OpenAI | 0.2241148 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r011 | 11 | completed |  | 30/30 | 95.93 | 150 | 0 | 0 | OpenAI | 0.2146024 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r012 | 12 | completed |  | 30/30 | 128.86 | 150 | 0 | 0 | OpenAI | 0.2172272 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r013 | 13 | completed |  | 30/30 | 102.64 | 150 | 0 | 0 | OpenAI | 0.2154168 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r014 | 14 | completed |  | 30/30 | 170.01 | 150 | 0 | 0 | OpenAI | 0.2147304 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r015 | 15 | completed |  | 30/30 | 117.43 | 150 | 0 | 0 | OpenAI | 0.2188292 |
| 20261021T175656Z_stage2_mini-low_rapport_691757_r016 | 16 | completed |  | 30/30 | 166.41 | 150 | 0 | 0 | OpenAI | 0.2114724 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
