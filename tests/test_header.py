import pytest
from compression_tool.header import build_header, decode_header

def test_header_io():
    pad_len = 3
    freq = {97: 4, 98: 5, 99: 1}
    codestring = "101001101"

    header = build_header(pad_len, freq)
    parsed = decode_header(header + codestring)

    assert parsed.version == "HUF1"
    assert parsed.pad_len == 3
    assert parsed.freq == {97: 4, 98: 5, 99: 1}
    assert parsed.payload == codestring

def test_build_header_string():
    pad_len = 3
    freq = {97: 4, 98: 5, 99: 1}

    header = build_header(pad_len, freq)

    assert header == "HUF1|pad=3|freq=97:4,98:5,99:1|"
