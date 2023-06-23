import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone

from config import open_ai, pinecone

from config.constants import INDEX_NAME, PRODUCTION, MODE
from utils.ai.openai import create_or_get_conversation_chain

from icecream import ic

from views.home import home


def main():
    open_ai.setup()
    pinecone.setup()

    embeddings = OpenAIEmbeddings()
    vectorstore = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    # create conversation chain
    st.session_state.conversation = create_or_get_conversation_chain(vectorstore)
    ic('conversation chain created')

    home()


# to run this application, you need to run "streamlit run app.py"
if __name__ == '__main__':
    if MODE == PRODUCTION:
        ic.disable()

    main()
