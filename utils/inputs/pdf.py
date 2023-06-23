from functools import cache
from pathlib import Path

from pypdf import PdfReader
from typing import IO


@cache
def extract(*pdf_docs: str | IO | Path) -> str:
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
