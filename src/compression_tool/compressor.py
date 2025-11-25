"""
High-level Huffman compression pipeline.

This module ties together the frequency table, tree builder, code map,
bit packing, and header encoding to turn raw bytes into a single
compressed byte stream.
"""
from compression_tool.header import build_header
from compression_tool.frequency import build_frequency_table
from compression_tool.build_tree import build_tree
from compression_tool.code_map import build_code_map
from compression_tool.utils.bitutils import pack_bits


def compress(data: bytes) -> bytes:
    """
    Compress a bytestream using Huffman coding.

    This function orchestrates the full compression pipeline:

      1. Build a frequency table from the input bytes.
      2. Build a Huffman tree and corresponding code map.
      3. Encode the input data as a bitstring using the code map.
      4. Pack the bitstring into bytes (recording the padding length).
      5. Build a textual header containing version, pad_len and frequency table.
      6. Encode the header to bytes and prepend it to the packed payload.

    Special case:
        If ``data`` is empty, returns only the header bytes for an empty file
        (no payload bytes).

    Args:
        data: Raw input payload as a bytes object (e.g. file contents).

    Returns:
        A bytes object containing the full compressed stream:

            header_bytes + packed_payload_bytes

        where ``header_bytes`` is the UTF-8 encoded header string produced by
        :func:`build_header`, and ``packed_payload_bytes`` is the Huffman-coded
        body returned by :func:`pack_bits`.
    """
    if data == b"":
        header = build_header(0, {})
        return header.encode("utf-8")
    
    freq_table = build_frequency_table(data)
    root = build_tree(freq_table)
    code_map = build_code_map(root)
    codestring = ""
    for symbol in data:
        codestring += code_map[symbol]
    packed_bytes, pad_len = pack_bits(codestring)
    header = build_header(pad_len, freq_table)
    header_bytes = header.encode("utf-8")

    return header_bytes + packed_bytes
