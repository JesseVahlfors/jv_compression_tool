from pathlib import Path
from .compressor import compress
from dataclasses import dataclass

@dataclass
class CompressionResult:
    input_path: Path
    output_path: Path
    original_size: int
    compressed_size: int

    @property
    def compression_ration(self) -> float:
        return self.compressed_size / self.original_size if self.original_size else 1.0


def compress_file(
        input_path: str | Path,
        output_path: str | Path | None = None,
    ) -> CompressionResult:
    """
    Read a file from disk, compress it using Huffman coding,
    and write the compressed bytes to output_path.

    If output_path is None, uses input_path with '.huff' appended.
    """
    in_path = Path(input_path)
    if output_path == None:
        out_path = in_path.with_suffix(input_path.suffix + ".huff")
    else:
        out_path = Path(output_path)
    
    data = in_path.read_bytes()
    compressed = compress(data)
    print(compressed)
    out_path.write_bytes(compressed)

    return CompressionResult(
        input_path=in_path,
        output_path=out_path,
        original_size=len(data),
        compressed_size=len(compressed),
    )

