"""Ties embeddings + vector store together into a single retrieve() call.

See docs/modules/01_rag_system.md, task 6.
"""

from multimodal_assistant.rag.embeddings import EmbeddingModel
from multimodal_assistant.rag.vector_store import VectorStore


class Retriever:
    def __init__(self, embedding_model: EmbeddingModel, vector_store: VectorStore) -> None:
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, question: str, top_k: int = 5) -> list[dict]:
        """Embed `question` and return the top_k most relevant chunks.

        Returns:
            A list of dicts (chunk_id, doc_id, text, metadata, score), ranked
            by relevance descending.

        TODO:
            - Embed the question with self.embedding_model.embed_query
            - Call self.vector_store.similarity_search
            - (Bonus) add a reranking step for higher precision
        """
        raise NotImplementedError("TODO: implement Retriever.retrieve (Module 1)")
