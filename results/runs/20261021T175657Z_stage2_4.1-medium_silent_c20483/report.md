# Run report: 20261021T175657Z_stage2_4.1-medium_silent_c20483

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1200; tokens in 2,213,364; tokens out 431,327
- Cost: estimated $8.5640; actual $7.8773440 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175657Z_stage2_4.1-medium_silent_c20483/manifest.json` (committed copy of `runs/stage2/20261021T175657Z_stage2_4.1-medium_silent_c20483/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.6299420, seller $3.2474020

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r009 | 9 | completed |  | 30/30 | 161.62 | 150 | 0 | 0 | OpenAI | 0.9473720 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r010 | 10 | completed |  | 30/30 | 183.94 | 150 | 0 | 0 | OpenAI | 0.9480340 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r011 | 11 | completed |  | 30/30 | 149.99 | 150 | 0 | 0 | OpenAI | 0.9740660 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r012 | 12 | completed |  | 30/30 | 208.81 | 150 | 0 | 0 | OpenAI | 0.9504640 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r013 | 13 | completed |  | 30/30 | 147.77 | 150 | 0 | 0 | OpenAI | 0.9652920 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r014 | 14 | completed |  | 30/30 | 144.09 | 150 | 0 | 0 | OpenAI | 1.0499940 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r015 | 15 | completed |  | 30/30 | 151.53 | 150 | 0 | 0 | OpenAI | 1.0525820 |
| 20261021T175657Z_stage2_4.1-medium_silent_c20483_r016 | 16 | completed |  | 30/30 | 146.63 | 150 | 0 | 0 | OpenAI | 0.9895400 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
