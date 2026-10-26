# Run report: 20261021T175655Z_stage2_mini-low_silent_ad78c9

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 9,10,11,12,13,14,15,16 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 9-16 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1201; tokens in 2,740,998; tokens out 405,108
- Cost: estimated $1.9072; actual $1.7445720 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T175655Z_stage2_mini-low_silent_ad78c9/manifest.json` (committed copy of `runs/stage2/20261021T175655Z_stage2_mini-low_silent_ad78c9/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0369980, seller $0.7075740

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r009 | 9 | completed |  | 30/30 | 125.59 | 151 | 0 | 0 | OpenAI | 0.2101216 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r010 | 10 | completed |  | 30/30 | 108.36 | 150 | 0 | 0 | OpenAI | 0.2196032 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r011 | 11 | completed |  | 30/30 | 112.87 | 150 | 0 | 0 | OpenAI | 0.2194304 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r012 | 12 | completed |  | 30/30 | 99.46 | 150 | 0 | 0 | OpenAI | 0.2173240 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r013 | 13 | completed |  | 30/30 | 111.11 | 150 | 0 | 0 | OpenAI | 0.2244480 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r014 | 14 | completed |  | 30/30 | 124.62 | 150 | 0 | 0 | OpenAI | 0.2189932 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r015 | 15 | completed |  | 30/30 | 123.63 | 150 | 0 | 0 | OpenAI | 0.2183520 |
| 20261021T175655Z_stage2_mini-low_silent_ad78c9_r016 | 16 | completed |  | 30/30 | 115.12 | 150 | 0 | 0 | OpenAI | 0.2162996 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
