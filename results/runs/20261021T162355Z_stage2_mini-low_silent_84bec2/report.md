# Run report: 20261021T162355Z_stage2_mini-low_silent_84bec2

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: stage2; run type: confirmatory
- Purpose: Stage 2 confirmatory, block 0 only (replicate index 0, all 12 arms), against frozen prereg 40d93a9 / lock 1c2410c4 (human message 24)
- Command: `python -m sting.stage2_runner configs/stage2/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Stage 2 confirmatory, block 0 only (replicate index 0, all 12 arms), against frozen prereg 40d93a9 / lock 1c2410c4 (human message 24)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 150; tokens in 344,622; tokens out 49,711
- Cost: estimated $0.2384; actual $0.2173864 (OpenRouter-reported where available)
- Manifest: `results/runs/20261021T162355Z_stage2_mini-low_silent_84bec2/manifest.json` (committed copy of `runs/stage2/20261021T162355Z_stage2_mini-low_silent_84bec2/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1297820, seller $0.0876044

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021T162355Z_stage2_mini-low_silent_84bec2_r000 | 0 | completed |  | 30/30 | 108.03 | 150 | 0 | 0 | OpenAI | 0.2173864 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
