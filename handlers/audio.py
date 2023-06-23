from pathlib import Path

from typing import IO
import io

from utils.outputs.text_to_speech import text_to_speech, TextToSpeechConfig
import streamlit as st


def handle_text_2_speech(text: str | Path | IO):
    if not text:
        st.error(f"invalid input:{type(text)}")
        return

    config = TextToSpeechConfig(text=text, output=io.BytesIO())
    text_to_speech(config)
    st.audio(config.output, config.format)
