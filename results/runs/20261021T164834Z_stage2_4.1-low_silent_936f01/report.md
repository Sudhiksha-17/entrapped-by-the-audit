# Run report: 20261021T164834Z_stage2_4.1-low_silent_936f01

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1201; tokens in 2,586,313; tokens out 433,111
- Cost: estimated $8.5640; actual $8.6375140 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164834Z_stage2_4.1-low_silent_936f01/manifest.json` (committed copy of `runs/stage2/20261021T164834Z_stage2_4.1-low_silent_936f01/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0629860, seller $3.5745280

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r001 | 1 | completed |  | 30/30 | 187.74 | 150 | 0 | 0 | OpenAI | 1.0531140 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r002 | 2 | completed |  | 30/30 | 210.75 | 151 | 0 | 0 | OpenAI | 1.0969980 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r003 | 3 | completed |  | 30/30 | 148.28 | 150 | 0 | 0 | OpenAI | 1.0975660 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r004 | 4 | completed |  | 30/30 | 198.06 | 150 | 0 | 0 | OpenAI | 1.0610880 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r005 | 5 | completed |  | 30/30 | 198.22 | 150 | 0 | 0 | OpenAI | 1.1323520 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r006 | 6 | completed |  | 30/30 | 167.09 | 150 | 0 | 0 | OpenAI | 1.1051000 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r007 | 7 | completed |  | 30/30 | 157.23 | 150 | 0 | 0 | OpenAI | 0.9842460 |
| 20261021T164834Z_stage2_4.1-low_silent_936f01_r008 | 8 | completed |  | 30/30 | 153.35 | 150 | 0 | 0 | OpenAI | 1.1070500 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
