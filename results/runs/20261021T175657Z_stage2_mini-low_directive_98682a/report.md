# Run report: 20261021T175657Z_stage2_mini-low_directive_98682a

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,719,112; tokens out 415,421
- Cost: estimated $1.9072; actual $1.7523184 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175657Z_stage2_mini-low_directive_98682a/manifest.json` (committed copy of `runs/stage2/20261021T175657Z_stage2_mini-low_directive_98682a/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition directive, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0418156, seller $0.7105028

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175657Z_stage2_mini-low_directive_98682a_r009 | 9 | completed |  | 30/30 | 127.26 | 150 | 0 | 0 | OpenAI | 0.2192136 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r010 | 10 | completed |  | 30/30 | 175.86 | 150 | 0 | 0 | OpenAI | 0.2133948 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r011 | 11 | completed |  | 30/30 | 151.51 | 150 | 0 | 0 | OpenAI | 0.2240916 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r012 | 12 | completed |  | 30/30 | 112.72 | 150 | 0 | 0 | OpenAI | 0.2131764 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r013 | 13 | completed |  | 30/30 | 123.5 | 150 | 0 | 0 | OpenAI | 0.2174004 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r014 | 14 | completed |  | 30/30 | 116.28 | 150 | 0 | 0 | OpenAI | 0.2203952 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r015 | 15 | completed |  | 30/30 | 110.28 | 150 | 0 | 0 | OpenAI | 0.2235776 |
| 20261021T175657Z_stage2_mini-low_directive_98682a_r016 | 16 | completed |  | 30/30 | 124.49 | 150 | 0 | 0 | OpenAI | 0.2210688 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
