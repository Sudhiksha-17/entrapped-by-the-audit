# Run report: 20261016T215200Z_throughput_59a75f

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: throughput
- Purpose: Phase 2 throughput test: 2 parallel episodes of 5 rounds (credit rule 5)
- Command: `python -m sting.minimal_runner configs/throughput.yaml`
- Models: openrouter:openai/gpt-4o-mini@openai
- Calls: 60; tokens in 63,975; tokens out 17,927
- Cost: estimated $0.0300; actual $0.0203525 (OpenRouter-reported where available)
- Manifest: `runs/throughput/20261016T215200Z_throughput_59a75f/manifest.json` (gitignored)

- Rounds: 5; seller messaging: True; temperature: 0.7
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 2; completed 2; failed 0; failures by reason: {}; parse failures: 0
- Cost by role: buyer $0.0099945, seller $0.0103579

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 20261016T215200Z_throughput_59a75f_r000 | 0 | completed |  | 5/5 | 24.15 | 30 | 0 | OpenAI | 0.0103012 |
| 20261016T215200Z_throughput_59a75f_r001 | 1 | completed |  | 5/5 | 21.03 | 30 | 0 | OpenAI | 0.0100512 |

## Per round: 20261016T215200Z_throughput_59a75f_r000

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 82.83 | A 84.0, B 82.0, C 82.5 | 84.17 | 2 | 83.38 | 3 |
| 2 | 83.50 | A 83.75, B 83.0, C 83.75 | 84.67 | 3 | 84.08 | 3 |
| 3 | 83.67 | A 83.5, B 84.0, C 83.5 | 85.08 | 3 | 84.37 | 3 |
| 4 | 84.00 | A 83.5, B 85.0, C 83.5 | 85.83 | 2 | 85.00 | 3 |
| 5 | 84.33 | A 83.25, B 85.0, C 84.75 | 86.17 | 2 | 85.44 | 3 |

## Per round: 20261016T215200Z_throughput_59a75f_r001

| Round | Mean seller ask | Seller asks | Mean buyer bid | Trades | Mean trade price | Seller messages |
|---|---|---|---|---|---|---|
| 1 | 87.19 | A 82.01, B 83.0, C 96.56 | 91.50 | 2 | 89.12 | 3 |
| 2 | 83.33 | A 83.5, B 83.0, C 83.5 | 92.55 | 3 | 87.94 | 3 |
| 3 | 84.03 | A 84.0, B 83.1, C 85.0 | 92.77 | 3 | 88.40 | 3 |
| 4 | 84.83 | A 85.0, B 83.5, C 86.0 | 93.29 | 3 | 89.06 | 3 |
| 5 | 85.67 | A 86.0, B 84.0, C 87.0 | 93.73 | 3 | 89.70 | 3 |
