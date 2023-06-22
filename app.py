import threading

import streamlit as st
import openai
from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone

from config import open_ai, pinecone

from constants import OPENAI_API_KEY, INDEX_NAME
from utils.ai.openai import get_conversation_chain

from icecream import ic

from views.home import home


def main():
    threading.Thread(target=home, args=(), daemon=True).start()

    open_ai.setup()
    pinecone.setup()

    embeddings = OpenAIEmbeddings()
    vectorstore = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    # create conversation chain
    st.session_state.conversation = get_conversation_chain(vectorstore)
    ic('conversation chain created')


# to run this application, you need to run "streamlit run app.py"
if __name__ == '__main__':
    main()
