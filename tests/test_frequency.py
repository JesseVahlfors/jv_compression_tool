from compression_tool.frequency import count_frequencies
from pathlib import Path
import pytest

@pytest.fixture
def test_data():
    path = Path(__file__).parent / "data" / "test.txt"
    with open(path, "rb") as file:
        return file.read()

def test_frequency_with_static():
    data = b"aaabbc"
    freq = count_frequencies(data)
    assert freq == {97: 3, 98: 2, 99: 1}  # ASCII values for 'a', 'b', 'c'

def test_frequency_with_file(test_data):
    freq = count_frequencies(test_data)
    
    expected = {
        ord('X'): 333,  # Replace 'X' with actual byte values from test.txt
        ord('t'): 223000, # Replace 't' with actual byte values from test.txt
    }

    for char_code, count in expected.items():
        assert freq[char_code] == count, f"Unexpected count for {chr(char_code)}"