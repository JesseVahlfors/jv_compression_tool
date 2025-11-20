import pytest
from compression_tool.compressor import compress
from compression_tool.utils.bitutils import pack_bits
from compression_tool.header import build_header

def test_compress_empty_data():
    data = compress(b"")
    print(data)
    assert data == build_header(0, {})

def test_compress_single_symbol():
    result = compress(b"A")
    header_str = build_header(7, {65:1})
    expected_header = header_str.encode("utf-8")
    expected_body = b"\x00"
    assert result == expected_header + expected_body
