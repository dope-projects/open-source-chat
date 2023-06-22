from icecream import ic
from langchain.vectorstores import pinecone

from constants import PINECONE_API_KEY, PINECONE_API_ENV
from database.pinecone_db import index_list


def setup() -> None:
    ic('Init pinecone database')
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV,
    )

    ic(f"pinecone-setup:{index_list()}")
