from src.compression_tool.compressor import compress
from src.compression_tool.decompressor import decompress
import os

def test_decompressor_empty_data():
    original = b""
    compressed = compress(original)
    decompressed = decompress(compressed)

    assert decompressed == original

def test_decompressor_single_symbol_once():
    original = b"A"
    compressed = compress(original)
    decompressed = decompress(compressed)

    assert decompressed == original

def test_decompressor_single_symbol_repeated():
    original = b"AAAAAA"
    compressed = compress(original)
    decompressed = decompress(compressed)

    assert decompressed == original

def test_decompressor_multiple_symbols_AAB():
    original = b"AAB"
    compressed = compress(original)
    decompressed = decompress(compressed)

    assert decompressed == original

def test_decompress_multiple_symbols_hello_world():
    original = b"hello world"
    compressed = compress(original)
    decompressed = decompress(compressed)
    
    assert decompressed == original

def test_decompressor_non_ascii_bytes():
    """
    Roundtrip all byte values 0-255 once.

    This checks that:
      - we don't assume text anywhere in the pipeline
      - Huffman coding works for the full byte range
      - tree/codes stay deterministic with many equal-frequency symbols
    """
    original = bytes(range(256))  # 0x00 .. 0xFF
    compressed = compress(original)
    decompressed = decompress(compressed)

    assert decompressed == original


def test_decompressor_random_bytes():
    """
    Roundtrip a block of random bytes.

    This gives a more "real world" stress test with arbitrary patterns.
    """
    original = os.urandom(256)  # size is arbitrary; 256 is a nice stress level
    compressed = compress(original)
    decompressed = decompress(compressed)

    assert decompressed == original