"""Automatic quality evaluation for generated text.

See docs/modules/02_creative_writing.md, task 5.
"""


def distinct_n(texts: list[str], n: int = 2) -> float:
    """Fraction of distinct n-grams across `texts` (diversity metric, 0..1).

    TODO: tokenize each text, count n-grams, return
    len(unique_ngrams) / len(total_ngrams).
    """
    raise NotImplementedError("TODO: implement distinct_n (Module 2)")


def repetition_score(text: str) -> float:
    """Heuristic degeneration check: fraction of repeated n-grams within one text.

    Higher = more repetitive/degenerate. TODO: implement using n-gram counts.
    """
    raise NotImplementedError("TODO: implement repetition_score (Module 2)")


def evaluate_generations(texts: list[str]) -> dict:
    """Produce a summary report for a batch of generated texts.

    Returns a dict with at least: distinct_1, distinct_2, avg_length,
    avg_repetition_score. This report should be referenced in your technical
    documentation as evidence of generation quality.
    """
    raise NotImplementedError("TODO: implement evaluate_generations (Module 2)")
