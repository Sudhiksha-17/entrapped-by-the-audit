# Run report: 20261024T065648Z_study1r_mini-low_offer_032fb8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory block 0 (replicate index 0, all 9 arms; human message 67, gate B)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R confirmatory block 0 (replicate index 0, all 9 arms; human message 67, gate B)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 154; tokens in 369,000; tokens out 53,002
- Cost: estimated $0.2481; actual $0.2302144 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T065648Z_study1r_mini-low_offer_032fb8/manifest.json` (committed copy of `runs/study1r/20261024T065648Z_study1r_mini-low_offer_032fb8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1324508, probe $0.0047112, seller $0.0930524

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T065648Z_study1r_mini-low_offer_032fb8_r000 | 0 | completed |  | 30/30 | 113.17 | 154 | 0 | 0 | OpenAI | 0.2302144 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
