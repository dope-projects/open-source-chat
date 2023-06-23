import streamlit as st
from icecream import ic

from utils.ai.openai import get_text_chunk, upsert
from utils.inputs.pdf import extract


def sidebar_spinner(pdf_docs):
    with st.spinner('Processing'):
        # get pdf text
        data = extract(pdf_docs)
        ic('pdfs have been reading into data')

        # Use loader and data splitter to make a document list
        doc = get_text_chunk(data)
        ic(f'text_chunks are generated and the total chucks are {len(doc)}')

        # Upsert data to the VectorStore
        upsert(doc)


def sidebar():
    with st.sidebar:
        st.subheader('Your PDF documents')
        pdf_docs = st.file_uploader(
            "Upload your pdfs here and click on 'Proces'",
            accept_multiple_files=True,
        )
        # if the button is pressed
        if st.button('Process'):
            sidebar_spinner(pdf_docs)
