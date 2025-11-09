import pytest
from compression_tool.code_map import code_map
from compression_tool.build_tree import build_tree

def test_empty_tree():
    root = None
    assert code_map(root) == {}

def test_single_symbol():
    root = build_tree({97: 5})

    assert code_map(root) == {97: 0}

