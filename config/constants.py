import os

from os import environ
from typing import Final

from dotenv import load_dotenv

load_dotenv()

PRODUCTION: Final[str] = 'production'
DEVELOPMENT: Final[str] = 'development'
TESTING: Final[str] = 'testing'
MODE: Final[str] = os.getenv('mode', DEVELOPMENT)

PINECONE_API_KEY: Final[str] = environ['PINECONE_API_KEY'].strip()
PINECONE_API_ENV: Final[str] = environ['PINECONE_API_ENV'].strip()
INDEX_NAME: Final[str] = os.getenv('INDEX_NAME', 'langchaintest').strip()

OPENAI_API_KEY: Final[str] = environ['OPENAI_API_KEY'].strip()
