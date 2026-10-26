# Run report: 20261024T091015Z_study1r_mini-low_offer_2129d6

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,887,331; tokens out 428,658
- Cost: estimated $1.9848; actual $1.8275756 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091015Z_study1r_mini-low_offer_2129d6/manifest.json` (committed copy of `runs/study1r/20261024T091015Z_study1r_mini-low_offer_2129d6/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0596328, probe $0.0401276, seller $0.7278152

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r025 | 25 | completed |  | 30/30 | 95.23 | 154 | 0 | 0 | OpenAI | 0.2224724 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r026 | 26 | completed |  | 30/30 | 102.3 | 154 | 0 | 0 | OpenAI | 0.2288640 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r027 | 27 | completed |  | 30/30 | 105.42 | 154 | 0 | 0 | OpenAI | 0.2331548 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r028 | 28 | completed |  | 30/30 | 119.57 | 154 | 0 | 0 | OpenAI | 0.2282504 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r029 | 29 | completed |  | 30/30 | 104.09 | 154 | 0 | 0 | OpenAI | 0.2310112 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r030 | 30 | completed |  | 30/30 | 133.28 | 154 | 0 | 0 | OpenAI | 0.2364904 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r031 | 31 | completed |  | 30/30 | 109.27 | 154 | 0 | 0 | OpenAI | 0.2327080 |
| 20261024T091015Z_study1r_mini-low_offer_2129d6_r032 | 32 | completed |  | 30/30 | 98.28 | 154 | 0 | 0 | OpenAI | 0.2146244 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
