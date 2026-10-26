# Run report: 20261016T214105Z_model_check_1ef862

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: model_check; stage: model_check
- Purpose: Phase 2 model check rerun 3; same key, 403
- Command: `python -m sting.model_check configs/model_check.yaml`
- Models: openrouter:openai/gpt-4o-mini
- Calls: 1; tokens in 0; tokens out 0
- Cost: estimated $0.0000; actual $0.0000000 (OpenRouter-reported where available)
- Manifest: `runs/model_check/20261016T214105Z_model_check_1ef862/manifest.json` (gitignored)

| Provider | Requested model | Status | Returned model | Routed provider | Tokens in/out | Cost $ | Note |
|---|---|---|---|---|---|---|---|
| openai | gpt-4o-mini | skipped |  |  | 0/0 |  | OPENAI_API_KEY not present |
| openai | gpt-4o | skipped |  |  | 0/0 |  | OPENAI_API_KEY not present |
| openai | gpt-4.1 | skipped |  |  | 0/0 |  | OPENAI_API_KEY not present |
| openai | gpt-4.1-mini | skipped |  |  | 0/0 |  | OPENAI_API_KEY not present |
| anthropic | claude-3-5-haiku-latest | skipped |  |  | 0/0 |  | ANTHROPIC_API_KEY not present |
| anthropic | claude-3-5-sonnet-latest | skipped |  |  | 0/0 |  | ANTHROPIC_API_KEY not present |
| anthropic | claude-3-7-sonnet-latest | skipped |  |  | 0/0 |  | ANTHROPIC_API_KEY not present |
| openrouter | openai/gpt-4o-mini | error |  |  | 0/0 |  | ModelCallFailed: model_check: non-transient error from openrouter/openai/gpt-4o- |
