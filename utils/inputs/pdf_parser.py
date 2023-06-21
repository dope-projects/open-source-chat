from pathlib import Path

from PyPDF2 import PdfReader
from typing import IO


def parse_pdf(pdf: str | IO | Path):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
