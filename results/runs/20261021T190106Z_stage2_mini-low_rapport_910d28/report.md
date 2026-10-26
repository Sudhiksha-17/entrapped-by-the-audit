# Run report: 20261021T190106Z_stage2_mini-low_rapport_910d28

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1201; tokens in 2,754,203; tokens out 402,785
- Cost: estimated $1.9072; actual $1.7461372 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190106Z_stage2_mini-low_rapport_910d28/manifest.json` (committed copy of `runs/stage2/20261021T190106Z_stage2_mini-low_rapport_910d28/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition rapport, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0429940, seller $0.7031432

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r017 | 17 | completed |  | 30/30 | 103.27 | 150 | 0 | 0 | OpenAI | 0.2213228 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r018 | 18 | completed |  | 30/30 | 122.93 | 150 | 0 | 0 | OpenAI | 0.2193756 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r019 | 19 | completed |  | 30/30 | 128.08 | 151 | 0 | 0 | OpenAI | 0.2128708 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r020 | 20 | completed |  | 30/30 | 122.49 | 150 | 0 | 0 | OpenAI | 0.2219404 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r021 | 21 | completed |  | 30/30 | 106.89 | 150 | 0 | 0 | OpenAI | 0.2209948 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r022 | 22 | completed |  | 30/30 | 107.98 | 150 | 0 | 0 | OpenAI | 0.2162516 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r023 | 23 | completed |  | 30/30 | 121.87 | 150 | 0 | 0 | OpenAI | 0.2154120 |
| 20261021T190106Z_stage2_mini-low_rapport_910d28_r024 | 24 | completed |  | 30/30 | 102.44 | 150 | 0 | 0 | OpenAI | 0.2179692 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
