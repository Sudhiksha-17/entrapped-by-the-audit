# Run report: 20261023T175651Z_judge_20261021T164834Z_stage2_mini-low_offer_d8ca28_1d4d5a

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: judge; stage: judge:stage2; run type: exploratory
- Purpose: Stage 2 judge, first arm-run check before the remaining 39 (human messages 31 and 33)
- Command: `python -m sting.judge <repo>\runs\stage2\20261021T164834Z_stage2_mini-low_offer_d8ca28 --approve-cost --purpose Stage 2 judge, first arm-run check before the remaining 39 (human messages 31 and 33)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 320; tokens in 321,457; tokens out 53,856
- Cost: estimated $0.2692; actual $0.2147524 (OpenRouter-reported where available)
- Manifest: `results/runs/20261023T175651Z_judge_20261021T164834Z_stage2_mini-low_offer_d8ca28_1d4d5a/manifest.json` (committed copy of `runs/judge:stage2/20261023T175651Z_judge_20261021T164834Z_stage2_mini-low_offer_d8ca28_1d4d5a/manifest.json`)

- Source run: `20261021T164834Z_stage2_mini-low_offer_d8ca28`; seller-rounds judged: 320; valid labels: 319; invalid: 1

| Label | Value counts (valid labels) |
|---|---|
| engaged_with_message | yes 319 |
| response | accept 35, counter 231, noncommittal 18, reject 35 |
| awareness | none 252, strategic_distrust 67 |
| legal_or_ethical_concern | no 319 |
| own_coordination_intent | none 14, overt 126, tacit 179 |
