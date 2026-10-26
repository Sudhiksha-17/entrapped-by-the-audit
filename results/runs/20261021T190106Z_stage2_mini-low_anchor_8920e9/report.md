# Run report: 20261021T190106Z_stage2_mini-low_anchor_8920e9

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,733,753; tokens out 422,918
- Cost: estimated $1.9072; actual $1.7701700 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190106Z_stage2_mini-low_anchor_8920e9/manifest.json` (committed copy of `runs/stage2/20261021T190106Z_stage2_mini-low_anchor_8920e9/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0590332, seller $0.7111368

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r017 | 17 | completed |  | 30/30 | 105.75 | 150 | 0 | 0 | OpenAI | 0.2244444 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r018 | 18 | completed |  | 30/30 | 124.54 | 150 | 0 | 0 | OpenAI | 0.2252536 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r019 | 19 | completed |  | 30/30 | 113.67 | 150 | 0 | 0 | OpenAI | 0.2185332 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r020 | 20 | completed |  | 30/30 | 176.8 | 150 | 0 | 0 | OpenAI | 0.2188236 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r021 | 21 | completed |  | 30/30 | 136.49 | 150 | 0 | 0 | OpenAI | 0.2243216 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r022 | 22 | completed |  | 30/30 | 136.87 | 150 | 0 | 0 | OpenAI | 0.2255088 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r023 | 23 | completed |  | 30/30 | 115.19 | 150 | 0 | 0 | OpenAI | 0.2220388 |
| 20261021T190106Z_stage2_mini-low_anchor_8920e9_r024 | 24 | completed |  | 30/30 | 110.34 | 150 | 0 | 0 | OpenAI | 0.2112460 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
