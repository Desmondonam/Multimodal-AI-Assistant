"""Tests for Module 2. Remove @pytest.mark.skip as you implement each piece.

test_generate_* are marked `slow` since they load a real model — run with
`pytest -m slow` once implemented, or unmark if fast enough on your machine.
"""

import pytest

from multimodal_assistant.text_generation.prompt_templates import render_template


@pytest.mark.skip(reason="TODO: implement render_template / TEMPLATES (Module 2)")
def test_render_template_substitutes_variables():
    result = render_template("product_blurb", style="playful", product="a smart mug")
    assert "smart mug" in result


@pytest.mark.skip(reason="TODO: implement render_template / TEMPLATES (Module 2)")
def test_render_template_missing_variable_raises():
    with pytest.raises(ValueError):
        render_template("product_blurb", style="playful")  # missing `product`


@pytest.mark.skip(reason="TODO: implement render_template (Module 2)")
def test_render_template_unknown_name_raises():
    with pytest.raises(KeyError):
        render_template("not_a_real_template")


@pytest.mark.slow
@pytest.mark.skip(reason="TODO: implement Generator (Module 2) + fine-tuning")
def test_generator_returns_distinct_variations():
    from multimodal_assistant.text_generation.generator import Generator

    generator = Generator()
    variations = generator.generate("Write about a rainy city.", num_variations=3)
    assert len(variations) == 3
    assert len(set(variations)) == 3  # not near-duplicates
