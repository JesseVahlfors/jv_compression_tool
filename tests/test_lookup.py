import pytest
from compression_tool.lookup import build_lookup_table, lookup_symbol

def test_build_lookup_table_empty_dict():
    code_map = {}

    assert build_lookup_table(code_map) == {}

def test_build_lookup_table_one_symbol():
    code_map = {97: "101"}

    assert build_lookup_table(code_map) == {"101": 97}

def test_build_lookup_table_duplicate_code():
    code_map = {97: "101", 99: "101"}

    with pytest.raises(ValueError, match="duplicate code"):
        build_lookup_table(code_map)

pytest.mark.parametrize("malformed_code", [
    "",
    "10x10",
    101,
])

def test_build_lookup_table_malformed_code(malformed_code):
    with pytest.raises(ValueError):
        build_lookup_table(malformed_code)


def test_lookup_symbol():
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
    raise ValueError
    #lookup_symbol(bitstream: str, index: int, table: dict[str, int])