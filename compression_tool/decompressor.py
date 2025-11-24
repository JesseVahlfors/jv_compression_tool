"""
High-level Huffman decompression pipeline.

This module ties together header decoding, Huffman tree reconstruction,
bit unpacking, and code lookup to turn a compressed byte stream back
into the original raw bytes.
"""
from compression_tool.header import decode_header_and_payload, decode_header
from compression_tool.build_tree import build_tree
from compression_tool.code_map import build_code_map
from compression_tool.lookup import build_lookup_table, lookup_symbol
from compression_tool.utils.bitutils import unpack_bits

def decompress(data: bytes) -> bytes:
    """
    Decompress a bytestream using Huffman coding.

    This function orchestrates the full compression pipeline:

      1. Split the compressed stream into header bytes and payload bytes.
      2. Decode the header to recover the padding length and frequency table.
      3. Rebuild the Huffman tree from the frequency table.
      4. Rebuild the code map (symbol -> bits) and construct a reverse lookup (bits -> symbol).
      5. Unpack the payload bytes into a bitstring and remove any padding.
      6. Walk the bitstring using the lookup table to reconstruct the original bytes.

    Args:
        data:
            Compressed data as a bytes object (for example, the contents
            of a .huff file produced by :func:`compress`).

    Returns:
        A bytes object containing the fully decompressed original payload.
    """
    header, body_bytes = decode_header_and_payload(data)
    if body_bytes == b"":
        return b""
    
    _, pad_len, freq = header
    root = build_tree(freq)
    code_map = build_code_map(root)
    lookup_table = build_lookup_table(code_map)
    bitstring = unpack_bits(body_bytes, pad_len)
    bytes_list =[]
    idx = 0
    while idx < (len(bitstring)):
        symbol, length = lookup_symbol(bitstring, idx , lookup_table)
        bytes_list.append(symbol)
        idx += length

    return bytes(bytes_list)