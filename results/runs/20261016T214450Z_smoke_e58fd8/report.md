# Run report: 20261016T214450Z_smoke_e58fd8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: smoke
- Purpose: Phase 2 smoke episode: 1 all-LLM episode, 15 rounds, messaging on (D-020)
- Command: `python -m sting.minimal_runner configs/smoke.yaml`
- Models: openrouter:openai/gpt-4o-mini@openai
- Calls: 90; tokens in 143,806; tokens out 26,613
- Cost: estimated $0.1000; actual $0.0375387 (OpenRouter-reported where available)
- Manifest: `runs/smoke/20261016T214450Z_smoke_e58fd8/manifest.json` (gitignored)

- Rounds: 15; seller messaging: True; temperature: 0.7
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Cost by role: buyer $0.0183117, seller $0.0192270

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 20261016T214450Z_smoke_e58fd8_r000 | 0 | completed |  | 15/15 | 58.68 | 90 | 0 | OpenAI | 0.0375387 |

## Per round: 20261016T214450Z_smoke_e58fd8_r000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 83.00 | A 82.0, B 82.0, C 85.0 | 83.17 | 2 | 82.88 | 3 |
| 2 | 82.83 | A 84.0, B 81.5, C 83.0 | 83.50 | 2 | 83.50 | 3 |
| 3 | 82.00 | A 83.0, B 80.5, C 82.5 | 83.67 | 2 | 83.50 | 3 |
| 4 | 81.17 | A 82.0, B 80.0, C 81.5 | 83.83 | 2 | 83.50 | 3 |
| 5 | 80.17 | A 81.0, B 79.0, C 80.5 | 81.83 | 2 | 81.75 | 3 |
| 6 | 79.33 | A 80.0, B 78.0, C 80.0 | 81.33 | 2 | 81.25 | 3 |
| 7 | 78.83 | A 79.5, B 77.0, C 80.0 | 80.75 | 2 | 80.69 | 3 |
| 8 | 78.67 | A 79.5, B 76.5, C 80.0 | 80.50 | 2 | 80.62 | 3 |
| 9 | 78.50 | A 79.5, B 76.0, C 80.0 | 81.92 | 2 | 80.56 | 3 |
| 10 | 78.17 | A 79.5, B 75.0, C 80.0 | 82.25 | 2 | 80.44 | 3 |
| 11 | 79.33 | A 79.5, B 79.0, C 79.5 | 82.33 | 3 | 80.83 | 3 |
| 12 | 78.67 | A 78.5, B 79.0, C 78.5 | 82.60 | 3 | 80.63 | 3 |
| 13 | 78.00 | A 78.0, B 78.0, C 78.0 | 82.78 | 3 | 80.39 | 3 |
| 14 | 77.83 | A 77.5, B 78.5, C 77.5 | 82.97 | 3 | 80.40 | 3 |
| 15 | 77.33 | A 77.0, B 78.0, C 77.0 | 79.90 | 3 | 78.61 | 3 |
