# Run report: 20261024T095252Z_study1r_4.1-low_offer_c6d56d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 33-40 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 33,34,35,36,37,38,39,40 --approve-cost --purpose Study 1R confirmatory blocks 33-40 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 0; tokens in 0; tokens out 0
- Cost: estimated $0.0000; actual $0.0000000 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T095252Z_study1r_4.1-low_offer_c6d56d/manifest.json` (committed copy of `runs/study1r/20261024T095252Z_study1r_4.1-low_offer_c6d56d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 0; completed 0; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: 

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
