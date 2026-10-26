# Run report: 20261021T201113Z_stage2_mini-low_directive_509ef7

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 25,26,27,28,29,30,31,32 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,729,956; tokens out 418,769
- Cost: estimated $1.9072; actual $1.7620128 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T201113Z_stage2_mini-low_directive_509ef7/manifest.json` (committed copy of `runs/stage2/20261021T201113Z_stage2_mini-low_directive_509ef7/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition directive, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0633220, seller $0.6986908

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r025 | 25 | completed |  | 30/30 | 107.57 | 150 | 0 | 0 | OpenAI | 0.2139260 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r026 | 26 | completed |  | 30/30 | 108.03 | 150 | 0 | 0 | OpenAI | 0.2247960 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r027 | 27 | completed |  | 30/30 | 117.54 | 150 | 0 | 0 | OpenAI | 0.2200364 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r028 | 28 | completed |  | 30/30 | 130.72 | 150 | 0 | 0 | OpenAI | 0.2215020 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r029 | 29 | completed |  | 30/30 | 111.8 | 150 | 0 | 0 | OpenAI | 0.2150520 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r030 | 30 | completed |  | 30/30 | 156.73 | 150 | 0 | 0 | OpenAI | 0.2231928 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r031 | 31 | completed |  | 30/30 | 119.34 | 150 | 0 | 0 | OpenAI | 0.2220900 |
| 20261021T201113Z_stage2_mini-low_directive_509ef7_r032 | 32 | completed |  | 30/30 | 99.36 | 150 | 0 | 0 | OpenAI | 0.2214176 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
