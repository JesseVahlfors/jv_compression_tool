from unittest.mock import patch
import pytest
from compression_tool.file_compressor import compress_file
import tempfile
import os

def test_file_compressor_reads_and_writes(tmp_path):
    input_file = tmp_path / "input.txt"

    input_file.write_bytes(b"compress me")

    # Mock the compress function to test I/O without actual compression logic
    with patch("compression_tool.file_compressor.compress", return_value=b"COMPRESSED") as mock_compress:
        compress_file(input_file)
        # Ensure the compress function was called with correct data
        mock_compress.assert_called_once_with(b"compress me")

    result = (input_file.with_suffix('.huff')).read_bytes()
    assert result == b"COMPRESSED"
    assert os.path.exists(input_file.with_suffix('.huff'))
