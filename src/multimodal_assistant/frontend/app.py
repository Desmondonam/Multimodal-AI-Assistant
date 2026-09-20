"""Streamlit frontend entrypoint.

See docs/modules/04_fullstack.md, frontend tasks 1-4.

Run with: `make frontend` (streamlit run src/multimodal_assistant/frontend/app.py)

Swap for Gradio if you prefer — keep the same three sections and error handling
requirements either way.
"""

import streamlit as st

from multimodal_assistant.config import settings

st.set_page_config(page_title="Multi-Modal AI Assistant", layout="wide")
st.title("Multi-Modal AI Assistant")

tab_qa, tab_write, tab_image = st.tabs(["Ask a Question", "Write Something", "Generate an Image"])

with tab_qa:
    st.subheader("Ask a Question (RAG)")
    # TODO:
    #   - text_input for the question
    #   - on submit: POST to f"{settings.frontend_api_base_url}/qa"
    #   - show a spinner while waiting; render the answer + cited sources
    #   - on error (4xx/5xx), show st.error with a clean message, not the raw traceback
    st.info("TODO: implement the QA tab (Module 4)")

with tab_write:
    st.subheader("Creative Writing")
    # TODO:
    #   - inputs: prompt, style, temperature, num_variations
    #   - POST to f"{settings.frontend_api_base_url}/write"
    #   - render each variation in its own expandable card
    st.info("TODO: implement the Writing tab (Module 4)")

with tab_image:
    st.subheader("Image Generation")
    # TODO:
    #   - inputs: prompt, negative prompt, width/height, steps
    #   - POST to f"{settings.frontend_api_base_url}/image" to enqueue
    #   - poll GET f"{settings.frontend_api_base_url}/image/{{job_id}}" until done
    #   - show a progress indicator while queued/processing; render the image when done
    st.info("TODO: implement the Image Generation tab (Module 4)")
