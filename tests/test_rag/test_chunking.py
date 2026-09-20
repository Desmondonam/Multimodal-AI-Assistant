"""Tests for Module 1 chunking. Remove @pytest.mark.skip as you implement
chunk_text in src/multimodal_assistant/rag/chunking.py.
"""

import pytest

from multimodal_assistant.rag.chunking import chunk_text


@pytest.mark.skip(reason="TODO: implement chunk_text (Module 1)")
def test_chunk_text_respects_size():
    text = "word " * 1000
    chunks = chunk_text(doc_id="doc1", text=text, chunk_size=100, chunk_overlap=10)
    assert len(chunks) > 1
    for chunk in chunks:
        assert len(chunk.text) <= 120  # allow small slack for word boundaries


@pytest.mark.skip(reason="TODO: implement chunk_text (Module 1)")
def test_chunk_text_has_overlap():
    text = "abcdefghij " * 50
    chunks = chunk_text(doc_id="doc1", text=text, chunk_size=50, chunk_overlap=10)
    assert chunks[0].text[-5:] in chunks[1].text


@pytest.mark.skip(reason="TODO: implement chunk_text (Module 1)")
def test_chunk_ids_are_unique():
    text = "sentence. " * 200
    chunks = chunk_text(doc_id="doc1", text=text, chunk_size=100, chunk_overlap=0)
    ids = [c.chunk_id for c in chunks]
    assert len(ids) == len(set(ids))


@pytest.mark.skip(reason="TODO: implement chunk_text (Module 1)")
def test_chunk_text_rejects_bad_overlap():
    with pytest.raises(ValueError):
        chunk_text(doc_id="doc1", text="short text", chunk_size=10, chunk_overlap=10)
