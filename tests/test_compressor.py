import pytest
from compression_tool.compressor import compress
from compression_tool.utils.bitutils import pack_bits
from compression_tool.header import build_header, decode_header_and_payload

def test_compress_empty_data():
    data = compress(b"")
    
    assert data == build_header(0, {})

def test_compress_single_symbol():
    result = compress(b"A")
    header_str = build_header(7, {65:1})
    expected_header = header_str.encode("utf-8")
    expected_body = b"\x00"

    assert result == expected_header + expected_body

def test_compress_multiple_symbols():
    compressed = compress(b"AAB")
    header_info, body_bytes = decode_header_and_payload(compressed)
    _, pad_len, freq = header_info

    assert freq == {65: 2, 66: 1}
    assert 0 <= pad_len <= 7 
    assert len(body_bytes) >= 1 