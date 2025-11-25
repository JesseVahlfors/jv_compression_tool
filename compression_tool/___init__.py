from .compressor import compress as compress_bytes
from .decompressor import decompress as decompress_bytes
from .file_compressor import compress_file, CompressionResult
from .file_decompressor import decompress_file, DecompressionResult

__all__ = [
    "compress_bytes",
    "decompress_bytes",
    "compress_file",
    "decompress_file",
    "CompressionResult",
    "DecompressionResult",
]