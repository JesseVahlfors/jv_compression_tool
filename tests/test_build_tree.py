from compression_tool.build_tree import build_tree
from compression_tool.tree import Node, LeafNode, InternalNode
import pytest

def test_empty_tree():
    assert build_tree({}) == None

def test_single_symbol():
    root = build_tree({97: 5})
    assert isinstance(root, LeafNode)
    assert root.symbol == 97 and root.weight == 5

def test_two_symbols():
    root = build_tree({97: 3, 98: 2})
    assert isinstance(root, InternalNode)
    assert root.weight == 5
    assert {root.left.weight, root.right.weight} == {3,2} 

def test_small_multi_set():
    root = build_tree({97: 5, 98: 2, 99: 1})
    assert root.weight == 8 

def test_three_equals_total_only():
    root = build_tree({97: 1, 98: 1, 99: 1})
    assert root.weight == 3