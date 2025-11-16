feat(lookup): implement enough functionality to pass """ Reverse lookup table operations """
from compression_tool.code_map import build_code_map

def build_lookup_table(code_map: dict[int, str]) -> dict[str, int]:
    """
    Build a reverse lookup table from a Huffman code map.

    Args:
        code_map: Dict mapping symbols to bitstrings.

    Returns:
        Dict mapping bitstrings to symbols.

    Raises:
        ValueError: If duplicate codes exist or codes are malformed. 
    """
    lookup = {code: symbol for symbol, code in code_map.items()}
    return lookup
    

def lookup_symbol(bitstream: str, index: int, table: dict[str, int]) -> tuple[int, int]:
    """
    Lookup the next symbol in a Huffman-coded bitstream.

    Args:
        bitstream: The full bitstring.
        index: The starting index for decoding.
        table: Reverse lookup mapping bitstrings to symbols.

    Returns:
        (symbol, length): The decoded symbol and number of bits consumed.

    Raises:
        KeyError: If no valid prefix exists at the given position.  
    """