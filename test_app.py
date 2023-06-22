from app import main
import pytest


@pytest.mark.first
def test_main():
    result = main()
    assert result is None
