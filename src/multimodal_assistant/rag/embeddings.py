"""Embedding generation using Sentence Transformers.

See docs/modules/01_rag_system.md, task 4.
"""

import numpy as np

from multimodal_assistant.config import settings


class EmbeddingModel:
    """Thin wrapper around a sentence-transformers model.

    TODO:
        - Load `settings.embedding_model_name` once in __init__ (cache it —
          don't reload per call)
        - Implement embed_texts for batches of chunks and embed_query for a
          single query string
    """

    def __init__(self, model_name: str | None = None) -> None:
        self.model_name = model_name or settings.embedding_model_name
        # TODO: load the SentenceTransformer model here
        raise NotImplementedError("TODO: implement EmbeddingModel.__init__ (Module 1)")

    def embed_texts(self, texts: list[str]) -> np.ndarray:
        """Embed a batch of texts, returning an (N, dim) float32 array."""
        raise NotImplementedError("TODO: implement embed_texts (Module 1)")

    def embed_query(self, query: str) -> np.ndarray:
        """Embed a single query string, returning a (dim,) float32 array."""
        raise NotImplementedError("TODO: implement embed_query (Module 1)")
