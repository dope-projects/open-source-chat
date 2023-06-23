import streamlit as st
from icecream import ic

from utils.ai.open_ai import get_text_chunk, upsert
from utils.inputs.pdf import extract


def sidebar_spinner():
    with st.spinner('Processing'):
        
        # Use loader and data splitter to make a document list
        doc = get_text_chunk()
        ic(f'text_chunks are generated and the total chucks are {len(doc)}')

        # Upsert data to the VectorStore
        upsert(doc)


def sidebar():
    with st.sidebar:
        st.subheader('Process the docs from github')

        # if the button is pressed
        if st.button('Process'):
            sidebar_spinner()
