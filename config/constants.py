import os
from typing import Final

from os import environ

from dotenv import load_dotenv

load_dotenv()

PRODUCTION: Final[str] = "production"
DEVELOPMENT: Final[str] = "development"
TESTING: Final[str] = "testing"

PINECONE_API_KEY: Final[str] = environ["PINECONE_API_KEY"]
PINECONE_API_ENV: Final[str] = environ["PINECONE_API_ENV"]
OPENAI_API_KEY: Final[str] = environ["OPENAI_API_KEY"]
INDEX_NAME: Final[str] = os.getenv("INDEX_NAME", "chatgpt")
MODE: Final[str] = os.getenv("mode", DEVELOPMENT)
