# conftest.py
import pytest
import os

@pytest.fixture
def mpy_file_path():
    return os.path.join(os.path.dirname(__file__), "../data/somefile.mpy")
