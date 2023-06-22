import streamlit as st
from icecream import ic

import public
from utils.ai.openai import get_text_chunk, upsert
from handlers.userinput import handle_userinput
from utils.inputs.pdf import extract


def home():
    st.set_page_config(page_title="Prompt Wiki", page_icon=":books:")
    st.write(public.css_index, unsafe_allow_html=True)

    # initial session_state in order to avoid refresh
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat based on PDF you provided :books:")
    user_question = st.text_input("Ask a question about your documents:")

    if user_question:
        handle_userinput(user_question)

    # Define the templates

    with st.sidebar:
        st.subheader("Your PDF documents")
        pdf_docs = st.file_uploader("Upload your pdfs here and click on 'Proces'", accept_multiple_files=True)
        # if the button is pressed
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                data = extract(pdf_docs)
                ic('pdfs have been reading into data')

                # Use loader and data splitter to make a documentlist
                doc = get_text_chunk(data)
                ic(f'text_chunks are generated and the total chucks are {len(doc)}')

                # Upsert data to the VectorStore
                upsert(doc)
