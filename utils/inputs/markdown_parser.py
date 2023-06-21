import markdown
from pathlib import Path
from typing import IO

def parse_markdown(markdown_docs: str | IO | Path):
    # Determine the input type
    if isinstance(markdown_docs, str):
        # Input is already a string
        input_string = markdown_docs
    elif isinstance(markdown_docs, Path):
        # Input is a file path
        with open(markdown_docs, 'r') as file:
            input_string = file.read()
    else:
        # Input is an IO object
        input_string = markdown_docs.read()

    # Convert Markdown to HTML
    html = markdown.markdown(input_string)

    # Remove any HTML tags and return as a single string
    return ''.join(html.strip().splitlines())
