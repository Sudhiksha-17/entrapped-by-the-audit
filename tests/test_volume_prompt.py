"""Volume prompt (prereg/stage2_spec.md section 3) via the prompt mirror; fake client only."""
import json
import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from sting.minimal_runner import run_batch, seller_prompt
from sting.paths import REPO_ROOT
from sting.prompt_mirror import CEO_TEXT, TEMPLATE_SUBDIR, UPSTREAM_TEMPLATES, VOLUME_TEMPLATE, ensure_mirror

import pytest

SPEC = (REPO_ROOT / "prereg" / "stage2_spec.md").read_text(encoding="utf-8")


def spec_quote(label):
    return re.search(rf"\*\*{label}[^\n]*\n> (.+)\n", SPEC).group(1).strip()


def test_volume_and_ceo_texts_match_the_spec():
    assert (REPO_ROOT / "sting" / "prompts" / "volume_message.txt").read_text(encoding="utf-8") == spec_quote("Volume prompt")
    assert CEO_TEXT == spec_quote("Upstream CEO prompt")
    assert CEO_TEXT in (UPSTREAM_TEMPLATES / "seller_prompt_base.jinja2").read_text(encoding="utf-8")
    assert len(spec_quote("Volume prompt").split()) == 45 and len(CEO_TEXT.split()) == 46


def test_mirror_copies_upstream_templates_byte_for_byte(tmp_path):
    root, digest = ensure_mirror(tmp_path)
    for p in UPSTREAM_TEMPLATES.glob("*.jinja2"):
        assert (root / TEMPLATE_SUBDIR / p.name).read_bytes() == p.read_bytes()
    assert ensure_mirror(tmp_path) == (root, digest)  # deterministic


def render(root, template, **kw):
    env = Environment(loader=FileSystemLoader(str(root / TEMPLATE_SUBDIR)))
    base = dict(seller_id="Seller A", company="Acme", valuation=80.0, round_number=11, num_rounds=30,
                hide_num_rounds=False, memory="m", seller_comms_enabled=True, seller_messages={}, bid_queue=[],
                ask_queue=[], past_bids_and_asks="", past_trades="", agent_successful_trades="", scratch_pad="",
                demonym=None, is_gagged=False, initial_condition=True, oversight_enabled=False,
                max_message_length=500)
    base.update(kw)
    return env.get_template(template).render(base)


def test_volume_prompt_differs_from_ceo_prompt_only_in_the_message(tmp_path):
    root, _ = ensure_mirror(tmp_path)
    ceo = render(root, "seller_prompt_base.jinja2", boss_pressure=True)
    vol = render(root, VOLUME_TEMPLATE, boss_pressure=False)
    volume_text = (REPO_ROOT / "sting" / "prompts" / "volume_message.txt").read_text(encoding="utf-8")
    assert "# Message from the CEO of Acme" in vol and vol.endswith(volume_text)
    assert ceo.replace(CEO_TEXT, volume_text) == vol
    default = render(root, "seller_prompt_base.jinja2", boss_pressure=False)
    assert "Message from the CEO" not in default


def test_seller_prompt_config_key():
    assert seller_prompt({}) == "default" and seller_prompt({"boss_pressure": True}) == "ceo"
    assert seller_prompt({"seller_prompt": "volume"}) == "volume"
    with pytest.raises(ValueError):
        seller_prompt({"seller_prompt": "volume", "boss_pressure": False})
    with pytest.raises(ValueError):
        seller_prompt({"seller_prompt": "urgent"})


@pytest.mark.parametrize("prompt,marker", [("volume", "tracks the number of your closed trades"),
                                           ("ceo", "tracks the average price point of your closed trades"),
                                           ("default", None)])
def test_episode_prompts_carry_the_cell_message(tmp_path, prompt, marker):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake_sting.yaml").read_text(encoding="utf-8"))
    cfg.update(rounds=1, seller_prompt=prompt)
    summary = run_batch(cfg, runs_dir=tmp_path, purpose="volume test")
    rep = next(p for p in Path(summary["run_dir"]).iterdir() if p.is_dir())
    seller_md = (rep / "upstream_logs" / "Seller A.md").read_text(encoding="utf-8")
    buyer_md = (rep / "upstream_logs" / "Buyer A.md").read_text(encoding="utf-8")
    if marker:
        assert marker in seller_md and "# Message from the CEO of" in seller_md
    else:
        assert "Message from the CEO" not in seller_md
    assert "Message from the CEO" not in buyer_md  # seller prompt only
    setup = json.loads((rep / "market_setup.json").read_text())
    assert setup["seller_prompt"] == prompt and setup["boss_pressure"] == (prompt == "ceo")
    run_cfg = json.loads((Path(summary["run_dir"]) / "run_config.json").read_text())
    assert len(run_cfg["prompt_mirror_sha256"]) == 64
