import streamlit as st

from config import open_ai, pinecone

from config.constants import INDEX_NAME, MODE, PRODUCTION

from icecream import ic
from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone
from utils.ai.open_ai import create_or_get_conversation_chain

from views.home import home


def main():
    open_ai.setup()
    pinecone.setup()

    embeddings = OpenAIEmbeddings()
    vectorstore = Pinecone.from_existing_index(
        index_name=INDEX_NAME, embedding=embeddings,
    )

    st.session_state.conversation = create_or_get_conversation_chain(
        vectorstore,
    )

    home()


# to run this application, you need to run "streamlit run app.py"
if __name__ == '__main__':
    if MODE == PRODUCTION:
        ic.disable()

    main()
