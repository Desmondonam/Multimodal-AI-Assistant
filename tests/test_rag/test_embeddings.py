"""Tests for Module 1 embeddings. Remove @pytest.mark.skip as you implement
EmbeddingModel in src/multimodal_assistant/rag/embeddings.py.
"""

import numpy as np
import pytest

from multimodal_assistant.rag.embeddings import EmbeddingModel


@pytest.mark.skip(reason="TODO: implement EmbeddingModel (Module 1)")
def test_embed_texts_shape():
    model = EmbeddingModel()
    embeddings = model.embed_texts(["hello world", "another sentence"])
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == 2
    assert embeddings.ndim == 2


@pytest.mark.skip(reason="TODO: implement EmbeddingModel (Module 1)")
def test_embed_query_shape_matches_texts():
    model = EmbeddingModel()
    query_vec = model.embed_query("what is the capital of France?")
    text_vecs = model.embed_texts(["Paris is the capital of France."])
    assert query_vec.shape[-1] == text_vecs.shape[-1]


@pytest.mark.skip(reason="TODO: implement EmbeddingModel (Module 1)")
def test_similar_sentences_are_closer_than_unrelated():
    model = EmbeddingModel()
    a = model.embed_query("The cat sat on the mat.")
    b = model.embed_query("A feline rested on the rug.")
    c = model.embed_query("Stock markets fell sharply today.")

    def cos_sim(x, y):
        return float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y)))

    assert cos_sim(a, b) > cos_sim(a, c)
