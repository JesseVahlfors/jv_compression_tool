from src.compression_tool.build_tree import build_tree
from src.compression_tool.tree import Node, LeafNode, InternalNode
import pytest

def test_empty_tree():
    assert build_tree({}) == None

def test_single_symbol():
    root = build_tree({97: 5})
    assert isinstance(root, LeafNode)
    assert root.symbol == 97 and root.weight == 5

def test_small_multi_set():
    root = build_tree({97: 5, 98: 2, 99: 1})
    assert root.weight == 8 

def test_three_equals_total_only():
    root = build_tree({97: 1, 98: 1, 99: 1})
    assert root.weight == 3

def test_root_weight_equals_sum():
    freq = {97: 5, 98: 2, 99: 1, 100: 7}
    root = build_tree(freq)
    assert root.weight == sum(freq.values())

@pytest.mark.parametrize("bad", [
    {97: 0},
    {97: -1},
    {"a": 3},
    {97: 2.5},
])

def test_input_validation(bad):
    with pytest.raises(ValueError):
        build_tree(bad)