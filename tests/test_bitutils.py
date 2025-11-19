import pytest
from compression_tool.utils.bitutils import pack_bits, unpack_bits

def test_pack_bits_empty_string():
    bits, pad_len = pack_bits("")

    assert bits == b""
    assert pad_len == 0

def test_pack_bits_length_multiple_of_8():
    string = "01000001"
    bits, pad_len = pack_bits(string)

    assert bits == b"A"
    assert pad_len == 0

def test_pack_bits_length_not_multiple_of_8():
    string = "010"
    bits, pad_len = pack_bits(string)

    assert bits == b"@"
    assert pad_len == 5

def test_pack_bits_multi_byte_string():
    string = "0100000101000010"
    bits, pad_len = pack_bits(string)

    assert bits == b"AB"
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

def test_unpack_bits_empty_byte():
    data =  b""
    pad_len = 0
    bits = unpack_bits(data, pad_len)

    assert bits == ""

def test_unpack_bits_one_byte():
    data = b"A"
    pad_len = 0
    bits = unpack_bits(data, pad_len)

    assert bits == "01000001"

def test_unpack_bits_byte_not_multiple_of_8():
    data = b"@"
    pad_len = 5
    bits = unpack_bits(data, pad_len)

    assert bits == "010"

def test_unpack_bits_multi_byte_string():
    data = b"AB"
    pad_len = 0
    bits = unpack_bits(data, pad_len)

    assert bits == "0100000101000010"