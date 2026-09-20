"""End-to-end ingestion CLI: raw docs -> chunks -> embeddings -> vector store.

See docs/modules/01_rag_system.md, task 8. Run via `make ingest`.
"""

from pathlib import Path

from multimodal_assistant.config import settings
from multimodal_assistant.rag.chunking import chunk_text
from multimodal_assistant.rag.embeddings import EmbeddingModel
from multimodal_assistant.rag.ingestion import ingest_documents
from multimodal_assistant.rag.vector_store import VectorStore

RAW_DATA_PATH = Path("data/raw/squad_train.json")


def main() -> None:
    """Run the full ingestion pipeline.

    TODO:
        1. documents = ingest_documents(RAW_DATA_PATH)
        2. chunks = [] ; for each document, extend with chunk_text(...)
        3. embedding_model = EmbeddingModel()
        4. embeddings = embedding_model.embed_texts([c.text for c in chunks])
        5. store = VectorStore(); store.create_table(dim=embeddings.shape[1], overwrite=True)
        6. store.upsert(chunks, embeddings)
        7. Print a short summary (num documents, num chunks, table location)
    """
    raise NotImplementedError("TODO: implement run_ingestion main (Module 1)")


if __name__ == "__main__":
    main()
