""" Reverse lookup table operations """
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
    lookup = {}

    for symbol, code in code_map.items():
        if not isinstance(code, str) \
        or not code \
        or not set(code) <= {"0", "1"}:
            raise ValueError(f"invalid code. code={code!r}")
        if code in lookup:
           raise ValueError(f"code cannot have duplicates. code={code!r}")
       
        lookup[code] = symbol 

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
        IndexError: If index < 0 or >= bitstream length  
    """
    if index < 0 or index >= len(bitstream):
        raise IndexError(f"Index out of range index={index!r}")
    prefix = ""
    for i in range (index, len(bitstream)):
        prefix += bitstream[i]
        if prefix in table:
            symbol = table[prefix]
            bits_consumed = len(prefix)
            return symbol, bits_consumed
    
    raise KeyError("no valid prefix exists")
   

