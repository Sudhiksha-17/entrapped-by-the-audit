"""Write verbatim seller messages selected for the Stage 1a pilot report.

Selection made by reading keyword-filtered candidates (D-042: quote selection only, never an outcome
measure). Usage: python scripts/stage1a_pilot_quotes.py results/stage1a/pilot_quotes.md
"""
import json
import sys
from pathlib import Path

SELECTION = [  # (summary run_id, round, seller)
    ("20261018T021040Z_stage1a_a_gpt-4.1-mini_default_bf593c", 18, "Seller B"),
    ("20261018T021040Z_stage1a_a_gpt-4.1-mini_default_bf593c", 19, "Seller A"),
    ("20261018T021213Z_stage1a_b_gpt-4.1-mini_ceo_aec90d", 18, "Seller B"),
    ("20261018T021213Z_stage1a_b_gpt-4.1-mini_ceo_aec90d", 22, "Seller B"),
    ("20261018T021442Z_stage1a_c_claude-haiku-4.5_default_29437c", 10, "Seller B"),
    ("20261018T021442Z_stage1a_c_claude-haiku-4.5_default_29437c", 11, "Seller B"),
    ("20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8", 22, "Seller A"),
    ("20261018T021958Z_stage1a_c_llama-3.3-70b_default_8071c8", 23, "Seller B"),
]

lines = ["# Stage 1a pilots: selected seller messages (verbatim)", "",
         "Selected by reading keyword-filtered candidates; the filter is for quote selection only and is never "
         "an outcome measure (D-042).", ""]
for run_id, rnd, seller in SELECTION:
    ep = json.loads(Path(f"results/stage1a/{run_id}_summary.json").read_text(encoding="utf-8"))["episodes"][0]
    msg = next(m for m in ep["keyword_messages_NOT_AN_OUTCOME_MEASURE"] if m["round"] == rnd and m["seller"] == seller)
    lines.append(f"- `{ep['replicate_id']}`, round {rnd}, {seller}: \"{msg['text']}\"")
Path(sys.argv[1]).write_text("\n".join(lines) + "\n", encoding="utf-8")
