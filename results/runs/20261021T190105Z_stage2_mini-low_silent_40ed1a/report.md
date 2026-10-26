# Run report: 20261021T190105Z_stage2_mini-low_silent_40ed1a

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 17,18,19,20,21,22,23,24 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 17-24 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1201; tokens in 2,745,229; tokens out 398,483
- Cost: estimated $1.9072; actual $1.7356644 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T190105Z_stage2_mini-low_silent_40ed1a/manifest.json` (committed copy of `runs/stage2/20261021T190105Z_stage2_mini-low_silent_40ed1a/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 1
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0322960, seller $0.7033684

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r017 | 17 | completed |  | 30/30 | 119.43 | 150 | 0 | 0 | OpenAI | 0.2173044 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r018 | 18 | completed |  | 30/30 | 126.2 | 150 | 0 | 0 | OpenAI | 0.2156016 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r019 | 19 | completed |  | 30/30 | 144.63 | 150 | 0 | 0 | OpenAI | 0.2192976 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r020 | 20 | completed |  | 30/30 | 134.1 | 150 | 0 | 0 | OpenAI | 0.2155244 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r021 | 21 | completed |  | 30/30 | 127.96 | 151 | 1 | 0 | OpenAI | 0.2160468 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r022 | 22 | completed |  | 30/30 | 284.23 | 150 | 0 | 0 | OpenAI | 0.2168356 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r023 | 23 | completed |  | 30/30 | 136.63 | 150 | 0 | 0 | OpenAI | 0.2167424 |
| 20261021T190105Z_stage2_mini-low_silent_40ed1a_r024 | 24 | completed |  | 30/30 | 115.31 | 150 | 0 | 0 | OpenAI | 0.2183116 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
