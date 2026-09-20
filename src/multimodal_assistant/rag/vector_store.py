"""LanceDB-backed vector store wrapper.

See docs/modules/01_rag_system.md, task 5.

Swap the implementation for Pinecone/Weaviate if you prefer (keep the same
public interface so retriever.py doesn't need to change).
"""

import numpy as np

from multimodal_assistant.config import settings
from multimodal_assistant.rag.chunking import Chunk


class VectorStore:
    """CRUD + similarity search over a table of chunk embeddings.

    TODO:
        - Connect to LanceDB at settings.lancedb_uri in __init__
        - Define a schema: chunk_id, doc_id, text, metadata (json), vector
    """

    def __init__(self, table_name: str = "chunks", uri: str | None = None) -> None:
        self.uri = uri or settings.lancedb_uri
        self.table_name = table_name
        raise NotImplementedError("TODO: implement VectorStore.__init__ (Module 1)")

    def create_table(self, dim: int, overwrite: bool = False) -> None:
        """Create (or recreate) the underlying table with the given vector dim."""
        raise NotImplementedError("TODO: implement create_table (Module 1)")

    def upsert(self, chunks: list[Chunk], embeddings: np.ndarray) -> None:
        """Insert or update rows for the given chunks and their embeddings.

        len(chunks) must equal embeddings.shape[0].
        """
        raise NotImplementedError("TODO: implement upsert (Module 1)")

    def similarity_search(self, query_embedding: np.ndarray, top_k: int = 5) -> list[dict]:
        """Return the top_k most similar chunks as dicts with at least:
        chunk_id, doc_id, text, metadata, score.
        """
        raise NotImplementedError("TODO: implement similarity_search (Module 1)")
