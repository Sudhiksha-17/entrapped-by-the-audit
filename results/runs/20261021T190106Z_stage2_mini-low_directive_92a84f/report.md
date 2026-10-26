# Run report: 20261021T190106Z_stage2_mini-low_directive_92a84f

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,718,768; tokens out 417,800
- Cost: estimated $1.9072; actual $1.7559872 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190106Z_stage2_mini-low_directive_92a84f/manifest.json` (committed copy of `runs/stage2/20261021T190106Z_stage2_mini-low_directive_92a84f/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition directive, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0511536, seller $0.7048336

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r017 | 17 | completed |  | 30/30 | 103.18 | 150 | 0 | 0 | OpenAI | 0.2242456 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r018 | 18 | completed |  | 30/30 | 131.28 | 150 | 0 | 0 | OpenAI | 0.2138760 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r019 | 19 | completed |  | 30/30 | 144.16 | 150 | 0 | 0 | OpenAI | 0.2239048 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r020 | 20 | completed |  | 30/30 | 123.91 | 150 | 0 | 0 | OpenAI | 0.2231836 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r021 | 21 | completed |  | 30/30 | 129.15 | 150 | 0 | 0 | OpenAI | 0.2150852 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r022 | 22 | completed |  | 30/30 | 118.31 | 150 | 0 | 0 | OpenAI | 0.2175120 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r023 | 23 | completed |  | 30/30 | 123.28 | 150 | 0 | 0 | OpenAI | 0.2216644 |
| 20261021T190106Z_stage2_mini-low_directive_92a84f_r024 | 24 | completed |  | 30/30 | 113.35 | 150 | 0 | 0 | OpenAI | 0.2165156 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
