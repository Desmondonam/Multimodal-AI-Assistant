"""Context-aware answer generation for the RAG pipeline.

See docs/modules/01_rag_system.md, task 7.
"""

from multimodal_assistant.config import settings

RAG_SYSTEM_PROMPT = """You are a helpful assistant that answers questions using \
ONLY the provided context. If the answer is not contained in the context, say \
you don't know rather than guessing."""


def build_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    """Assemble the retrieved chunks and question into a single LLM prompt.

    TODO:
        - Format each chunk with a source marker (e.g. [1], [2]) so the model
          can cite them
        - Keep total prompt length within a sane token budget
    """
    raise NotImplementedError("TODO: implement build_prompt (Module 1)")


def generate_answer(question: str, retrieved_chunks: list[dict]) -> dict:
    """Generate a grounded answer to `question` using `retrieved_chunks`.

    Returns:
        {"answer": str, "sources": list[dict]} — sources should be a subset of
        retrieved_chunks that were actually used/cited.

    TODO:
        - Build the prompt via build_prompt()
        - Call the configured LLM provider (settings.llm_provider /
          settings.llm_model_name) — start with OpenAI's chat completions API,
          or swap in an open-source client
        - Parse/return the answer alongside the sources used
    """
    raise NotImplementedError("TODO: implement generate_answer (Module 1)")
