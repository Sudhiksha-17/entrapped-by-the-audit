# Run report: 20261021T190106Z_stage2_mini-low_sham_2a46fb

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,727,672; tokens out 399,104
- Cost: estimated $1.9072; actual $1.7296352 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190106Z_stage2_mini-low_sham_2a46fb/manifest.json` (committed copy of `runs/stage2/20261021T190106Z_stage2_mini-low_sham_2a46fb/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition sham, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0333280, seller $0.6963072

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r017 | 17 | completed |  | 30/30 | 100.36 | 150 | 0 | 0 | OpenAI | 0.2143576 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r018 | 18 | completed |  | 30/30 | 145.63 | 150 | 0 | 0 | OpenAI | 0.2160240 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r019 | 19 | completed |  | 30/30 | 118.65 | 150 | 0 | 0 | OpenAI | 0.2140728 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r020 | 20 | completed |  | 30/30 | 112.98 | 150 | 0 | 0 | OpenAI | 0.2134868 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r021 | 21 | completed |  | 30/30 | 136.41 | 150 | 0 | 0 | OpenAI | 0.2191596 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r022 | 22 | completed |  | 30/30 | 103.98 | 150 | 0 | 0 | OpenAI | 0.2177480 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r023 | 23 | completed |  | 30/30 | 119.06 | 150 | 0 | 0 | OpenAI | 0.2155780 |
| 20261021T190106Z_stage2_mini-low_sham_2a46fb_r024 | 24 | completed |  | 30/30 | 101.53 | 150 | 0 | 0 | OpenAI | 0.2192084 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
