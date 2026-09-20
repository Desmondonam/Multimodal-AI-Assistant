"""Document ingestion for the RAG pipeline.

See docs/modules/01_rag_system.md, task 2.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class RawDocument:
    doc_id: str
    text: str
    metadata: dict


def ingest_documents(raw_data_path: Path) -> list[RawDocument]:
    """Load raw knowledge-base data (e.g. SQuAD 2.0 JSON) and normalize it.

    Args:
        raw_data_path: path to the raw dataset file/directory downloaded by
            scripts/download_data.py.

    Returns:
        A list of RawDocument, one per distinct source passage/article.

    TODO:
        - Parse the raw JSON (SQuAD format: data -> paragraphs -> context)
        - Deduplicate identical passages
        - Attach useful metadata (e.g. title, source) for citation later
    """
    raise NotImplementedError("TODO: implement ingest_documents (Module 1)")
