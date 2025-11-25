from pathlib import Path
from dataclasses import dataclass
from .decompressor import decompress

@dataclass
class DecompressionResult:
    input_path: Path
    output_path: Path
    compressed_size: int
    decompressed_size: int

def _default_output_path_for(input_path: Path) -> Path:
    # If file ends with ".huff" strip it. Otherwise append ".out".
    if input_path.suffix == ".huff":
        return input_path.with_suffix("")
    return input_path.with_suffix(input_path.suffix + ".out")

def decompress_file(
        input_path: str | Path,
        output_path: str | Path | None = None,
) -> DecompressionResult:
    """
    Read a compressed file from disk, decompress it using Huffman coding,
    and write the decompressed bytes to output_path.

    If output_path is None:
      - If input ends with '.huff', strip '.huff'
      - Otherwise, append '.out' to the existing suffix
    """
    in_path = Path(input_path)
    if output_path is None:
        out_path = _default_output_path_for(in_path)
    else:
        out_path =  Path(output_path)

    compressed = in_path.read_bytes()
    decompressed = decompress(compressed)
    out_path.write_bytes(decompressed)

    return DecompressionResult(
        input_path= in_path,
        output_path= out_path,
        compressed_size=len(compressed),
        decompressed_size=len(decompressed),
    )