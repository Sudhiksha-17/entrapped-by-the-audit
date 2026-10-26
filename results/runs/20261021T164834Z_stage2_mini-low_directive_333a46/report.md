# Run report: 20261021T164834Z_stage2_mini-low_directive_333a46

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 1,2,3,4,5,6,7,8 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 1-8 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,771,885; tokens out 422,113
- Cost: estimated $1.9072; actual $1.7841348 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T164834Z_stage2_mini-low_directive_333a46/manifest.json` (committed copy of `runs/stage2/20261021T164834Z_stage2_mini-low_directive_333a46/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition directive, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0645372, seller $0.7195976

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T164834Z_stage2_mini-low_directive_333a46_r001 | 1 | completed |  | 30/30 | 125.53 | 150 | 0 | 0 | OpenAI | 0.2248536 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r002 | 2 | completed |  | 30/30 | 131.35 | 150 | 0 | 0 | OpenAI | 0.2274284 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r003 | 3 | completed |  | 30/30 | 115.87 | 150 | 0 | 0 | OpenAI | 0.2233932 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r004 | 4 | completed |  | 30/30 | 138.41 | 150 | 0 | 0 | OpenAI | 0.2163776 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r005 | 5 | completed |  | 30/30 | 122.46 | 150 | 0 | 0 | OpenAI | 0.2216240 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r006 | 6 | completed |  | 30/30 | 106.4 | 150 | 0 | 0 | OpenAI | 0.2194216 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r007 | 7 | completed |  | 30/30 | 130.94 | 150 | 0 | 0 | OpenAI | 0.2253236 |
| 20261021T164834Z_stage2_mini-low_directive_333a46_r008 | 8 | completed |  | 30/30 | 122.16 | 150 | 0 | 0 | OpenAI | 0.2257128 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
