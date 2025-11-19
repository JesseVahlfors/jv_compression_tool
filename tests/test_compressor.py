import pytest
from compression_tool.compressor import compress
from compression_tool.utils.bitutils import pack_bits
from compression_tool.header import build_header

def test_compress_empty_data():
    freq = {}
    bitstring = ""
    packed_bits, pad_len = pack_bits("")
    header = build_header(0, {})