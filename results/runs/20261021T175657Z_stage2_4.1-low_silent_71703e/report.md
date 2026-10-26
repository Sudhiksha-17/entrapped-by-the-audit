# Run report: 20261021T175657Z_stage2_4.1-low_silent_71703e

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1201; tokens in 2,642,984; tokens out 430,540
- Cost: estimated $8.5640; actual $8.7302880 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175657Z_stage2_4.1-low_silent_71703e/manifest.json` (committed copy of `runs/stage2/20261021T175657Z_stage2_4.1-low_silent_71703e/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0851900, seller $3.6450980

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r009 | 9 | completed |  | 30/30 | 135.81 | 150 | 0 | 0 | OpenAI | 1.1058820 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r010 | 10 | completed |  | 30/30 | 182.11 | 150 | 0 | 0 | OpenAI | 1.1152920 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r011 | 11 | completed |  | 30/30 | 138.15 | 150 | 0 | 0 | OpenAI | 1.0993180 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r012 | 12 | completed |  | 30/30 | 157.1 | 150 | 0 | 0 | OpenAI | 1.0717500 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r013 | 13 | completed |  | 30/30 | 169.56 | 150 | 0 | 0 | OpenAI | 1.0520240 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r014 | 14 | completed |  | 30/30 | 141.62 | 150 | 0 | 0 | OpenAI | 1.1202220 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r015 | 15 | completed |  | 30/30 | 177.09 | 151 | 0 | 0 | OpenAI | 1.1349400 |
| 20261021T175657Z_stage2_4.1-low_silent_71703e_r016 | 16 | completed |  | 30/30 | 216.65 | 150 | 0 | 0 | OpenAI | 1.0308600 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
