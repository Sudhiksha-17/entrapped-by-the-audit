# Run report: 20261024T074632Z_study1r_4.1-low_silent_1b2d37

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,794,968; tokens out 434,454
- Cost: estimated $9.9112; actual $9.0279360 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074632Z_study1r_4.1-low_silent_1b2d37/manifest.json` (committed copy of `runs/study1r/20261024T074632Z_study1r_4.1-low_silent_1b2d37/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.1305980, probe $0.2557400, seller $3.6415980

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r009 | 9 | completed |  | 30/30 | 96.56 | 154 | 0 | 0 | OpenAI | 1.1160880 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r010 | 10 | completed |  | 30/30 | 88.97 | 154 | 0 | 0 | OpenAI | 1.1379580 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r011 | 11 | completed |  | 30/30 | 101.72 | 154 | 0 | 0 | OpenAI | 1.1329400 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r012 | 12 | completed |  | 30/30 | 101.59 | 154 | 0 | 0 | OpenAI | 1.1338540 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r013 | 13 | completed |  | 30/30 | 224.92 | 154 | 0 | 0 | OpenAI | 1.1189380 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r014 | 14 | completed |  | 30/30 | 100.11 | 154 | 0 | 0 | OpenAI | 1.1142140 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r015 | 15 | completed |  | 30/30 | 138.11 | 154 | 0 | 0 | OpenAI | 1.1476500 |
| 20261024T074632Z_study1r_4.1-low_silent_1b2d37_r016 | 16 | completed |  | 30/30 | 106.13 | 154 | 0 | 0 | OpenAI | 1.1262940 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
