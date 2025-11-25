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

    with pytest.raises(ValueError, match="code cannot have duplicates."):
        build_lookup_table(code_map)

@pytest.mark.parametrize("malformed_code", [
    "",
    "10x10",
    101,
])

def test_build_lookup_table_malformed_code(malformed_code):
    code_map = {97: malformed_code}
    with pytest.raises(ValueError):
        build_lookup_table(code_map)


def test_lookup_symbol_1_bit_code():
    bitstream = "011110"
    index = 0
    table = {"0": 97, "1": 98}

    assert lookup_symbol(bitstream, index, table) == (97, 1)

def test_lookup_symbol_multi_bit_code():
    bitstream = "110010"
    index = 0
    table = {"110": 97}

    assert lookup_symbol(bitstream, index, table) == (97, 3)

def test_lookup_symbol_index_offset():
    bitstream = "0011"
    index = 2
    table = {"0": 97, "11": 98}

    assert lookup_symbol(bitstream, index, table) == (98, 2)

def test_lookup_symbol_no_valid_prefix():
    bitstream = "1"
    index = 0
    table = {"10": 97}

    with pytest.raises(KeyError):
        lookup_symbol(bitstream, index, table)

    table = {"0": 97}
    bitstream = "111"
    index = 0

    with pytest.raises(KeyError):
        lookup_symbol(bitstream, index, table)

def test_lookup_symbol_index_out_of_range():
    bitstream = "0101"
    index = 4
    table = {"0": 97, "11": 98}

    with pytest.raises(IndexError):
        lookup_symbol(bitstream, index, table)