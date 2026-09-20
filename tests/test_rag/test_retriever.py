"""Tests for Module 1 retriever. Remove @pytest.mark.skip as you implement
Retriever.retrieve in src/multimodal_assistant/rag/retriever.py.

Uses fakes for the embedding model and vector store so this test exercises
only the glue logic in Retriever, not real ML models.
"""

import numpy as np
import pytest

from multimodal_assistant.rag.retriever import Retriever


class FakeEmbeddingModel:
    def embed_query(self, query: str) -> np.ndarray:
        return np.array([1.0, 0.0, 0.0], dtype="float32")


class FakeVectorStore:
    def similarity_search(self, query_embedding: np.ndarray, top_k: int = 5) -> list[dict]:
        return [
            {"chunk_id": "c1", "doc_id": "d1", "text": "relevant text", "metadata": {}, "score": 0.95}
        ][:top_k]


@pytest.mark.skip(reason="TODO: implement Retriever.retrieve (Module 1)")
def test_retrieve_returns_ranked_chunks():
    retriever = Retriever(embedding_model=FakeEmbeddingModel(), vector_store=FakeVectorStore())
    results = retriever.retrieve("any question", top_k=1)
    assert len(results) == 1
    assert results[0]["chunk_id"] == "c1"
    assert "score" in results[0]


@pytest.mark.skip(reason="TODO: implement Retriever.retrieve (Module 1)")
def test_retrieve_respects_top_k():
    class MultiResultStore(FakeVectorStore):
        def similarity_search(self, query_embedding, top_k=5):
            return [{"chunk_id": f"c{i}", "doc_id": "d1", "text": "t", "metadata": {}, "score": 1.0 - i * 0.1} for i in range(10)][:top_k]

    retriever = Retriever(embedding_model=FakeEmbeddingModel(), vector_store=MultiResultStore())
    results = retriever.retrieve("any question", top_k=3)
    assert len(results) == 3
