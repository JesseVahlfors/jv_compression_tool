RUN_SLOW_TESTS = False

import pytest
from src.compression_tool.file_compressor import compress_file
from src.compression_tool.file_decompressor import decompress_file
from pathlib import Path

def test_file_compressor_reads_and_writes(tmp_path):
    input_file = tmp_path / "example.txt"
    original_data = b"hello world"
    input_file.write_bytes(original_data)

    comp_result = compress_file(input_file)
    assert comp_result.input_path == input_file
    assert comp_result.output_path.exists()

    decomp_result = decompress_file(comp_result.output_path)
    assert decomp_result.output_path.exists()
    assert decomp_result.output_path.read_bytes() == original_data

def test_large_repetitive_file_compresses(tmp_path):
    input_file = tmp_path / "big.txt"
    original_data = (b"hello world " * 1000)
    input_file.write_bytes(original_data)

    comp_result = compress_file(input_file)

    assert comp_result.compressed_size < comp_result.original_size

LES_MIS = Path("tests/data/test.txt")

@pytest.mark.slow
@pytest.mark.skipif(
    not RUN_SLOW_TESTS,
    reason="Slow test disabled",
)
def test_les_mis_roundtrip(tmp_path):
    src = tmp_path / "test.txt"
    src.write_bytes(LES_MIS.read_bytes())

    comp = compress_file(src)

    decomp = decompress_file(comp.output_path)

    original_bytes = src.read_bytes()
    roundtrip_bytes = decomp.output_path.read_bytes()

    assert roundtrip_bytes == original_bytes
    assert comp.compressed_size < comp.original_size

    print(
        f"Les Mis original: {len(original_bytes)} bytes,"
        f"compressed: {comp.compressed_size} bytes",
        f"ratio: {comp.compressed_size / len(original_bytes):.3f}"
    )