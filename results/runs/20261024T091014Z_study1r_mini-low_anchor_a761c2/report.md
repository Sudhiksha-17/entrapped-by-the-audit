# Run report: 20261024T091014Z_study1r_mini-low_anchor_a761c2

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1262; tokens in 2,929,597; tokens out 438,544
- Cost: estimated $1.9848; actual $1.8594164 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091014Z_study1r_mini-low_anchor_a761c2/manifest.json` (committed copy of `runs/study1r/20261024T091014Z_study1r_mini-low_anchor_a761c2/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 9; completed 8; failed 1; failures by reason: {'other': 1}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0771664, probe $0.0388276, seller $0.7434224

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r025 | 25 | completed |  | 30/30 | 100.2 | 154 | 0 | 0 | OpenAI | 0.2257252 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r026 | 26 | completed |  | 30/30 | 100.44 | 154 | 0 | 0 | OpenAI | 0.2285908 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r027 | 27 | completed |  | 30/30 | 116.06 | 154 | 0 | 0 | OpenAI | 0.2279632 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r028 | 28 | failed | other | 5/30 | 25.33 | 30 | 0 | 0 | OpenAI | 0.0301180 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r028_repl1 | 28 | completed |  | 30/30 | 120.94 | 154 | 0 | 0 | OpenAI | 0.2320436 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r029 | 29 | completed |  | 30/30 | 100.8 | 154 | 0 | 0 | OpenAI | 0.2302288 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r030 | 30 | completed |  | 30/30 | 110.02 | 154 | 0 | 0 | OpenAI | 0.2251056 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r031 | 31 | completed |  | 30/30 | 109.16 | 154 | 0 | 0 | OpenAI | 0.2300296 |
| 20261024T091014Z_study1r_mini-low_anchor_a761c2_r032 | 32 | completed |  | 30/30 | 99.79 | 154 | 0 | 0 | OpenAI | 0.2296116 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
