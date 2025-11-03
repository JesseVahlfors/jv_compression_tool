from compression_tool.heapify import build_min_heap, sift_down, check_min_heap_valid
from compression_tool.tree import Node, LeafNode, InternalNode
import pytest

def test_heapify_simple():
    data = [
        LeafNode(symbol=b'f', weight=45),
        LeafNode(symbol=b'c', weight=12),
        LeafNode(symbol=b'a', weight=5),
        LeafNode(symbol=b'e', weight=16),
        LeafNode(symbol=b'd', weight=13),
        LeafNode(symbol=b'b', weight=9),
        ]
    
    heap = build_min_heap(data)

    assert heap[0].weight == min(freq for freq, _ in data)

def test_sift_down():
    data = [
        LeafNode(symbol=b'a', weight=3),
        LeafNode(symbol=b'b', weight=1),
        LeafNode(symbol=b'c', weight=4),
        LeafNode(symbol=b'd', weight=2),
        LeafNode(symbol=b'e', weight=5),
        LeafNode(symbol=b'f', weight=6),
    ]

    sift_down(data, 0)

    assert data[0].weight == 1

def test_check_min_heap_valid():
    data = [
        LeafNode(symbol=b'a', weight=2),
        LeafNode(symbol=b'b', weight=3),
        LeafNode(symbol=b'c', weight=4),
        LeafNode(symbol=b'd', weight=5),
        LeafNode(symbol=b'e', weight=6),
        LeafNode(symbol=b'f', weight=7),
    ]

    assert check_min_heap_valid(data) is True