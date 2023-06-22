from icecream import ic
import pinecone

from config.constants import PINECONE_API_KEY, PINECONE_API_ENV, INDEX_NAME
from database.pinecone_db import index_list, create_index


def setup() -> None:
    ic('Init pinecone database')
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV,
    )
    indexes = index_list()
    if INDEX_NAME not in indexes:
        ic(f"creating index:{INDEX_NAME}")
        create_index(INDEX_NAME)

    ic(f"pinecone-setup:{index_list()}")
