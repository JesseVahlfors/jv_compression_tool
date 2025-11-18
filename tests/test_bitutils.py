import pytest
from compression_tool.utils.bitutils import pack_bits

def test_pack_bits_empty_string():
    bytes, pad_len = pack_bits("")

    assert bytes == b""
    assert pad_len == 0

def test_pack_bits_length_multiple_of_8():
    string = "01000001"
    bytes, pad_len = pack_bits(string)

    assert bytes == b"A"
    assert pad_len == 0

def test_pack_bits_length_not_multiple_of_8():
    string = "010"
    bytes, pad_len = pack_bits(string)

    assert bytes == b"@"
    assert pad_len == 5