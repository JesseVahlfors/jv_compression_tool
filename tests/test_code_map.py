import pytest
from compression_tool.code_map import code_map
from compression_tool.build_tree import build_tree

def test_empty_tree():
    root = None
    assert code_map(root) == {}

def test_single_symbol():
    root = build_tree({97: 5})

    assert code_map(root) == {97: 0}

def test_two_symbols():
    root = build_tree({97: 3, 98: 2})

    assert 97 in root and 98 in root
    assert len(root[97]) == 1 and len(root[98]) == 1
    assert root[97] == 0 and root[98] == 1