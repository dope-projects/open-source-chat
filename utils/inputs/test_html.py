import io
from pathlib import Path
import tempfile
import pytest
from html import extract


def test_extract_string_input():
    html_string = '<html><head><title>Test Title</title></head><body><p>Test paragraph.</p></body></html>'
    result = extract(html_string)
    assert result == html_string


def test_extract_path_input():
    html_string = '<html><head><title>Test Title</title></head><body><p>Test paragraph.</p></body></html>'
    with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
        temp_file.write(html_string)
        temp_file_path = Path(temp_file.name)
    result = extract(temp_file_path)
    temp_file_path.unlink()
    assert result == html_string


def test_extract_io_input():
    html_string = '<html><head><title>Test Title</title></head><body><p>Test paragraph.</p></body></html>'
    with io.StringIO(html_string) as html_io:
        result = extract(html_io)
    assert result == html_string


def test_extract_invalid_input():
    invalid_input = 12345
    with pytest.raises(ValueError, match="Invalid input type. Expected str, IO, or Path."):
        extract(invalid_input)
