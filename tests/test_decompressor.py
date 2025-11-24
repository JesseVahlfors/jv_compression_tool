from compression_tool.compressor import compress
from compression_tool.decompressor import decompress

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
