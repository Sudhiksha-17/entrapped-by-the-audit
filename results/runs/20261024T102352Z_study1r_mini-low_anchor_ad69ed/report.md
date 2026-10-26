# Run report: 20261024T102352Z_study1r_mini-low_anchor_ad69ed

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 49-56 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 49,50,51,52,53,54,55,56 --approve-cost --purpose Study 1R confirmatory blocks 49-56 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,860,734; tokens out 423,157
- Cost: estimated $1.9848; actual $1.8052168 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T102352Z_study1r_mini-low_anchor_ad69ed/manifest.json` (committed copy of `runs/study1r/20261024T102352Z_study1r_mini-low_anchor_ad69ed/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0511940, probe $0.0364304, seller $0.7175924

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r049 | 49 | completed |  | 30/30 | 112.48 | 154 | 0 | 0 | OpenAI | 0.2274728 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r050 | 50 | completed |  | 30/30 | 113.36 | 154 | 0 | 0 | OpenAI | 0.2194676 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r051 | 51 | completed |  | 30/30 | 100.95 | 154 | 0 | 0 | OpenAI | 0.2279280 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r052 | 52 | completed |  | 30/30 | 129.68 | 154 | 0 | 0 | OpenAI | 0.2211964 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r053 | 53 | completed |  | 30/30 | 95.9 | 154 | 0 | 0 | OpenAI | 0.2245376 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r054 | 54 | completed |  | 30/30 | 120.12 | 154 | 0 | 0 | OpenAI | 0.2281760 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r055 | 55 | completed |  | 30/30 | 121.65 | 154 | 0 | 0 | OpenAI | 0.2254624 |
| 20261024T102352Z_study1r_mini-low_anchor_ad69ed_r056 | 56 | completed |  | 30/30 | 118.87 | 154 | 0 | 0 | OpenAI | 0.2309760 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
