# Run report: 20261021T201112Z_stage2_mini-low_silent_ffdb34

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 25,26,27,28,29,30,31,32 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1200; tokens in 2,741,320; tokens out 399,984
- Cost: estimated $1.9072; actual $1.7365024 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T201112Z_stage2_mini-low_silent_ffdb34/manifest.json` (committed copy of `runs/stage2/20261021T201112Z_stage2_mini-low_silent_ffdb34/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0394384, seller $0.6970640

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r025 | 25 | completed |  | 30/30 | 98.25 | 150 | 0 | 0 | OpenAI | 0.2125192 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r026 | 26 | completed |  | 30/30 | 100.38 | 150 | 0 | 0 | OpenAI | 0.2200980 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r027 | 27 | completed |  | 30/30 | 107.04 | 150 | 0 | 0 | OpenAI | 0.2147672 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r028 | 28 | completed |  | 30/30 | 113.41 | 150 | 0 | 0 | OpenAI | 0.2202772 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r029 | 29 | completed |  | 30/30 | 109.45 | 150 | 0 | 0 | OpenAI | 0.2160068 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r030 | 30 | completed |  | 30/30 | 102.44 | 150 | 0 | 0 | OpenAI | 0.2148700 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r031 | 31 | completed |  | 30/30 | 119.17 | 150 | 0 | 0 | OpenAI | 0.2189696 |
| 20261021T201112Z_stage2_mini-low_silent_ffdb34_r032 | 32 | completed |  | 30/30 | 95.17 | 150 | 0 | 0 | OpenAI | 0.2189944 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
