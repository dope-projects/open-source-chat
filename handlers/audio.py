from pathlib import Path

from typing import IO
import io

from utils.outputs.text_to_speech import text_to_speech, TextToSpeechConfig
import streamlit as st


def handle_text_2_speech(text: str | Path | IO):
    if not text:
        st.error("invalid input")
        return

    config = TextToSpeechConfig(text=text, output=io.BytesIO())
    output_file = text_to_speech(config)
    st.audio(output_file, format='audio/mp3')
