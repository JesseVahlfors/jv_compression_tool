from compression_tool.utils.heapify import build_min_heap, sift_down, check_min_heap_valid, sift_up, pop_min, push
from compression_tool.tree import Node, LeafNode, InternalNode
import pytest

def test_heapify_simple():
    heap = [
        LeafNode(symbol=b'f', weight=45),
        LeafNode(symbol=b'c', weight=12),
        LeafNode(symbol=b'a', weight=5),
        LeafNode(symbol=b'e', weight=16),
        LeafNode(symbol=b'd', weight=13),
        LeafNode(symbol=b'b', weight=9),
        ]
    
    heap = build_min_heap(heap)

    assert heap[0].weight == min(freq for freq, _ in heap)

def test_sift_down():
    heap = [
        LeafNode(symbol=b'a', weight=3),
        LeafNode(symbol=b'b', weight=1),
        LeafNode(symbol=b'c', weight=4),
        LeafNode(symbol=b'd', weight=2),
        LeafNode(symbol=b'e', weight=5),
        LeafNode(symbol=b'f', weight=6),
    ]

    sift_down(heap, 0)

    assert heap[0].weight == 1

def test_check_min_heap_valid():
    heap = [
        LeafNode(symbol=b'a', weight=2),
        LeafNode(symbol=b'b', weight=3),
        LeafNode(symbol=b'c', weight=4),
        LeafNode(symbol=b'd', weight=5),
        LeafNode(symbol=b'e', weight=6),
        LeafNode(symbol=b'f', weight=7),
    ]
    incorrect_heap = [
        LeafNode(symbol=b'a', weight=2),
        LeafNode(symbol=b'b', weight=30),
        LeafNode(symbol=b'c', weight=4),
        LeafNode(symbol=b'd', weight=5),
        LeafNode(symbol=b'e', weight=6),
        LeafNode(symbol=b'f', weight=7),
    ]
    equal = [
        LeafNode(symbol=b'a', weight=2),
        LeafNode(symbol=b'b', weight=2),
        LeafNode(symbol=b'c', weight=2),
    ]
    right_bad = [
        LeafNode(symbol=b'a', weight=2),
        LeafNode(symbol=b'b', weight=5),
        LeafNode(symbol=b'c', weight=1),   
    ]
    shuffled_valid = [
        LeafNode(symbol=b'a', weight=1),
        LeafNode(symbol=b'b', weight=3),
        LeafNode(symbol=b'c', weight=4),
        LeafNode(symbol=b'd', weight=7),
    ]

    assert check_min_heap_valid([]) is True
    assert check_min_heap_valid([LeafNode(symbol=b'b', weight=3)])
    assert check_min_heap_valid(heap) is True
    assert check_min_heap_valid(incorrect_heap) is False
    assert check_min_heap_valid(equal) is True
    assert check_min_heap_valid(right_bad) is False
    assert check_min_heap_valid(shuffled_valid) is True

def test_sift_up():
    heap = [
        LeafNode(b'a', 1),
        LeafNode(b'b', 3),
        LeafNode(b'c', 6),
        LeafNode(b'd', 8),
        LeafNode(b'e', 10),
        LeafNode(b'f', 12),
        LeafNode(b'g', 15),
    ]
    new_node = LeafNode(b'h', 2)
    heap.append(new_node)
    sift_up(heap, len(heap) - 1)
    
    assert heap[0].weight == 1
    assert heap[1].weight == 2
    assert check_min_heap_valid(heap)

def test_pop_min():
    heap = [
        LeafNode(b'a', 1),
        LeafNode(b'b', 3),
        LeafNode(b'c', 6),
        LeafNode(b'd', 8),
        LeafNode(b'e', 10),
        LeafNode(b'f', 12),
        LeafNode(b'g', 15),
    ]

    smallest = pop_min(heap)
    assert smallest.weight == 1
    assert len(heap) == 6
    assert check_min_heap_valid(heap)

def test_push():
    heap = [
        LeafNode(b'a', 2),
        LeafNode(b'b', 3),
        LeafNode(b'c', 6),
        LeafNode(b'd', 8),
        LeafNode(b'e', 10),
        LeafNode(b'f', 12),
        LeafNode(b'g', 15),
    ]
    new_node = LeafNode(b'h', 1)
    push(heap, new_node)

    assert heap[0] == new_node
    assert check_min_heap_valid(heap)

