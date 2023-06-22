from config.constants import OPENAI_API_KEY
from utils.ai import openai


def setup():
    openai.api_key = OPENAI_API_KEY
