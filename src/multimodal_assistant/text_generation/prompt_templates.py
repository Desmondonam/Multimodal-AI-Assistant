"""Parameterized prompt templates for creative writing.

See docs/modules/02_creative_writing.md, task 3.

Implement at least the three templates below (feel free to add more).
"""

TEMPLATES: dict[str, str] = {
    # TODO: fill in real templates, e.g.
    # "story_opening": "Write the opening paragraph of a {style} story about {topic}.",
    # "product_blurb": "Write a {style} product description for: {product}.",
    # "social_post": "Write a {style} social media post about {topic}.",
}


def render_template(name: str, **kwargs: str) -> str:
    """Render a named template with the given keyword variables.

    Raises:
        KeyError: if `name` is not a known template.
        ValueError: if a required variable is missing.

    TODO:
        - Populate TEMPLATES with at least 3 distinct templates
        - Implement variable substitution (str.format is fine) with a clear
          error if a required placeholder is missing
    """
    raise NotImplementedError("TODO: implement render_template (Module 2)")
