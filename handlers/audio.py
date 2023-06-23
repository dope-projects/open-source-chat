from pathlib import Path

from typing import IO

from utils.outputs.text_to_speech import text_to_speech
import streamlit as st


def handle_text_2_speech(input_text: str | Path | IO):
    if input_text:
        output_file = text_to_speech(input_text)
        st.audio(output_file, format='audio/mp3')
