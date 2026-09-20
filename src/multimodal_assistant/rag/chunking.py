"""Text chunking strategies for RAG.

See docs/modules/01_rag_system.md, task 3.
"""

from dataclasses import dataclass


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    metadata: dict


def chunk_text(
    doc_id: str,
    text: str,
    metadata: dict | None = None,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> list[Chunk]:
    """Split a document's text into overlapping chunks suitable for embedding.

    Args:
        doc_id: id of the source document, used to build chunk_id and to trace
            a retrieved chunk back to its source for citations.
        text: the full document text.
        metadata: optional metadata to carry onto every chunk.
        chunk_size: target chunk size (characters or tokens — your choice, but
            be consistent and document it in docs/ARCHITECTURE.md).
        chunk_overlap: overlap between consecutive chunks to avoid splitting
            relevant context across a boundary.

    Returns:
        A list of Chunk objects with unique chunk_id values.

    TODO:
        - Decide fixed-size vs. sentence/paragraph-aware splitting and justify
          it in docs/ARCHITECTURE.md
        - Ensure chunk_overlap actually overlaps content (not just indices)
        - Guard against chunk_size <= chunk_overlap
    """
    raise NotImplementedError("TODO: implement chunk_text (Module 1)")
