import pytest
from compression_tool.code_map import build_code_map
from compression_tool.build_tree import build_tree

# Left=0, right=1; node ordering is defined by comes_before (weight, then symbol). 
# Ties → lower symbol goes left (=‘0’).

def test_empty_tree():
    root = None
    assert build_code_map(root) == {}

def test_single_symbol():
    root = build_tree({97: 5})

    assert build_code_map(root) == {97: 0}

def test_two_symbols():
    root = build_tree({97: 3, 98: 2})
    map = build_code_map(root)

    print(f"root={root} left={root.left} right={root.right}")
    print(map)
    assert 97 in map and 98 in map
    assert len(map[97]) == 1 and len(map[98]) == 1
    assert map[97] == "1" and map[98] == "0"
    

def test_tie_break():
    root = build_tree({97: 2, 98: 2})
    map = build_code_map(root)

    assert len(map[97]) == 1 and len(map[98]) == 1
    assert map[97] == "0" and map[98] == "1"