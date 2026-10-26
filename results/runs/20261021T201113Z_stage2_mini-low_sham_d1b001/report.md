# Run report: 20261021T201113Z_stage2_mini-low_sham_d1b001

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 25,26,27,28,29,30,31,32 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, blocks 25-32 of 1-32, all 12 arms interleaved, replacement deferred (human message 25)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1202; tokens in 2,745,427; tokens out 398,066
- Cost: estimated $1.9072; actual $1.7350764 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T201113Z_stage2_mini-low_sham_d1b001/manifest.json` (committed copy of `runs/stage2/20261021T201113Z_stage2_mini-low_sham_d1b001/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition sham, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0432796, seller $0.6917968

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r025 | 25 | completed |  | 30/30 | 102.19 | 150 | 0 | 0 | OpenAI | 0.2155060 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r026 | 26 | completed |  | 30/30 | 125.44 | 150 | 0 | 0 | OpenAI | 0.2164096 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r027 | 27 | completed |  | 30/30 | 117.05 | 152 | 0 | 0 | OpenAI | 0.2212400 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r028 | 28 | completed |  | 30/30 | 107.07 | 150 | 0 | 0 | OpenAI | 0.2187404 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r029 | 29 | completed |  | 30/30 | 96.75 | 150 | 0 | 0 | OpenAI | 0.2198104 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r030 | 30 | completed |  | 30/30 | 113.4 | 150 | 0 | 0 | OpenAI | 0.2163848 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r031 | 31 | completed |  | 30/30 | 104.98 | 150 | 0 | 0 | OpenAI | 0.2165632 |
| 20261021T201113Z_stage2_mini-low_sham_d1b001_r032 | 32 | completed |  | 30/30 | 103.09 | 150 | 0 | 0 | OpenAI | 0.2104220 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
