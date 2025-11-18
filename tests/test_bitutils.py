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

def test_pack_bits_multi_byte_string():
    string = "0100000101000010"
    bytes, pad_len = pack_bits(string)

    assert bytes == b"AB"
    assert pad_len == 0

@pytest.mark.parametrize("invalids", [
    "2",
    "0102",
    "abc",
    "01 01",
])

def test_pack_bits_invalids_input(invalids):
    with pytest.raises(ValueError):
        pack_bits(invalids)