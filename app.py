import streamlit as st
import openai
from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone

from constants import OPENAI_API_KEY
from utils.ai.openai import get_conversation_chain

from icecream import ic

from views.home import home


def main():
    openai.api_key = OPENAI_API_KEY

    # Set up pinecone database

    # set up basic page
    home()

    embeddings = OpenAIEmbeddings()
    INDEX_NAME = 'langchaintest'
    print(f'{INDEX_NAME}')
    vectorstore = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    # create conversation chain
    st.session_state.conversation = get_conversation_chain(vectorstore)
    ic('conversation chain created')


# to run this application, you need to run "streamlit run app.py"
if __name__ == '__main__':
    main()
