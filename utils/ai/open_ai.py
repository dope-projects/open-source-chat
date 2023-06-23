from config.constants import INDEX_NAME
from database import pinecone_db
from icecream import ic
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.conversational_retrieval.base import (
    BaseConversationalRetrievalChain,
)
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone


def get_text_chunk(text):
    # use text_splitter to split it into documents list
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
    )
    chunks = text_splitter.split_text(text)

    # (variable) docs: List[Document]
    docs = [Document(page_content=text) for text in chunks]
    return docs


def upsert(data) -> Pinecone:
    # default model is:text-embedding-ada-002
    embeddings = OpenAIEmbeddings()

    #   will not to use vector in memory today.
    #    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    pinecone_db.create_index(INDEX_NAME)
    # to get more information, you can look at this page
    # https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/pinecone

    vectorstore = pinecone_db.upsert(
        data,
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
    return vectorstore


def create_or_get_conversation_chain(vectorstore) -> BaseConversationalRetrievalChain:
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    ic(f'conversation_chain is {conversation_chain}')
    return conversation_chain
