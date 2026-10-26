# Run report: 20261024T065649Z_study1r_4.1-high_offer_f031ce

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory block 0 (replicate index 0, all 9 arms; human message 67, gate B)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R confirmatory block 0 (replicate index 0, all 9 arms; human message 67, gate B)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 154; tokens in 274,984; tokens out 56,963
- Cost: estimated $1.1086; actual $0.9968400 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T065649Z_study1r_4.1-high_offer_f031ce/manifest.json` (committed copy of `runs/study1r/20261024T065649Z_study1r_4.1-high_offer_f031ce/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.5599300, probe $0.0211840, seller $0.4157260

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T065649Z_study1r_4.1-high_offer_f031ce_r000 | 0 | completed |  | 30/30 | 134.05 | 154 | 0 | 0 | OpenAI | 0.9968400 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
