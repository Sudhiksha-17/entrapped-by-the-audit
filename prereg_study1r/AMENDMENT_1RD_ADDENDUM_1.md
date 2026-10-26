# Study 1R-D amendment, addendum 1: Cell B on DeepInfra stopped; provider speed test and selection rule (human message 88)

Written after the freeze as a separate file, so the frozen amendment (`AMENDMENT_1RD.md`, hashed in `FROZEN_1RD.json`) stays
byte-identical. Recorded before any speed-test or new confirmatory Cell B episode. A Cell B re-freeze hashes this
addendum together with the amendment.

- Cell B on DeepInfra was stopped on 2026-10-25 at 18:32 after DeepInfra rate limits (HTTP 429): 10 episodes completed
  and 18 failed, which met the stop condition "failure rate above 10%" (I-066). These 28 episodes are excluded and not
  analysed. Cell B is not resumed on DeepInfra.
- **Provider speed test (exploratory; indices 2000+; never confirmatory; up to $3):** one Silent episode per OpenRouter
  provider serving `qwen/qwen3-235b-a22b-2507` with structured output that can be pinned with fallbacks disabled,
  DeepInfra excluded (Parasail, Venice, GMICloud, Google Vertex as listed 2026-10-25 19:14 local); same model,
  temperature, max_tokens and settings as the Cell B configs; only the pinned provider differs. Reported: minutes per
  episode, errors and rate-limit (429) responses.
- **Selection rule:** among providers whose speed-test episode completed with 0 errors (no errored call), the provider
  with the shortest episode time. If no provider completes its episode in under 8 minutes with 0 errors, Cell B is
  dropped for tonight.
- **If a provider qualifies:** a fresh Cell B (Silent, Silent-floor, Offer-floor; N = 33 each; indices 0-32) on that
  provider replaces the stopped one, as a run-mechanics change made because of rate limits and decided before any Cell
  B outcome was analysed; re-freeze; block 0 gate; then as many parallel invocations as the provider allows without
  errors. **Hard cutoff 02:00 local:** if Cell B has not finished by then it stops, and Cell B is reported as
  incomplete and not analysed.
- **Cell A** continues (indices 25-59). The block-cost stop at block 22 (I-067) is read as the artifact of a failed
  episode's partial cost with its replacement excluded (D-135).



## Speed test result and selection (2026-10-25, 19:16 to 19:28 local; `runs/study1r_addon_D_speedtest/`)

| Provider | Episode | Minutes | Calls | Errored calls | 429 responses | Parse failures | Routed | Cost | G2 |
|---|---|---|---|---|---|---|---|---|---|
| Parasail | completed | 4.9 | 154 | 0 | 0 | 0 | Parasail | $0.0996 | passed |
| Venice | completed | 12.0 | 154 | 0 | 0 | 0 | Venice | $0.1137 | passed |
| GMICloud | failed (api_failure) | 0.3 | 25 | 25 (HTTP 503) | 0 | 0 | none | $0.0000 | n/a |
| Google Vertex | failed (non-transient) | 0.1 | 5 | 5 (HTTP 404) | 0 | 0 | none | $0.0000 | n/a |

**Selected by the rule: Parasail** (0 errors, shortest episode, under 8 minutes). Fresh Cell B: arms Silent,
Silent-floor and Offer-floor on `qwen/qwen3-235b-a22b-2507` pinned to Parasail (fp8), all other settings as the first
Cell B; N = 33 each, indices 0-32; configs `configs/study1r_addon_D_b2/` (`scripts/make_study1rd_b2_configs.py`), runner
`python -m sting.study1rd_b2`, lock `prereg_study1r/FROZEN_1RD_B2.json`. Cost: $0.0996 x 1.10 = $0.1096 per episode;
99 episodes planned $10.85; cap $12.48 (budget group `study1r_addon_D_b2`). Parallel invocations over disjoint index
ranges (all three arms of an index together), starting with 3 after the block 0 gate and reduced on errors. Hard
cutoff 02:00 local.
