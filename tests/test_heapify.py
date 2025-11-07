from compression_tool.utils.heapify import build_min_heap, sift_down, check_min_heap_valid, sift_up, pop_min, push
from compression_tool.tree import Node, LeafNode, InternalNode
import pytest

def test_heapify_simple():
    heap = [
        LeafNode(symbol=ord('f'), weight=45),
        LeafNode(symbol=ord('c'), weight=12),
        LeafNode(symbol=ord('a'), weight=5),
        LeafNode(symbol=ord('e'), weight=16),
        LeafNode(symbol=ord('d'), weight=13),
        LeafNode(symbol=ord('b'), weight=9),
    ]
    
    heap = build_min_heap(heap)

    assert heap[0].weight == min(node.weight for node in heap)


def test_sift_down():
    heap = [
        LeafNode(symbol=ord('a'), weight=3),
        LeafNode(symbol=ord('b'), weight=1),
        LeafNode(symbol=ord('c'), weight=4),
        LeafNode(symbol=ord('d'), weight=2),
        LeafNode(symbol=ord('e'), weight=5),
        LeafNode(symbol=ord('f'), weight=6),
    ]

    sift_down(heap, 0)

    assert heap[0].weight == 1


def test_check_min_heap_valid():
    heap = [
        LeafNode(symbol=ord('a'), weight=2),
        LeafNode(symbol=ord('b'), weight=3),
        LeafNode(symbol=ord('c'), weight=4),
        LeafNode(symbol=ord('d'), weight=5),
        LeafNode(symbol=ord('e'), weight=6),
        LeafNode(symbol=ord('f'), weight=7),
    ]
    incorrect_heap = [
        LeafNode(symbol=ord('a'), weight=2),
        LeafNode(symbol=ord('b'), weight=30),
        LeafNode(symbol=ord('c'), weight=4),
        LeafNode(symbol=ord('d'), weight=5),
        LeafNode(symbol=ord('e'), weight=6),
        LeafNode(symbol=ord('f'), weight=7),
    ]
    equal = [
        LeafNode(symbol=ord('a'), weight=2),
        LeafNode(symbol=ord('b'), weight=2),
        LeafNode(symbol=ord('c'), weight=2),
    ]
    right_bad = [
        LeafNode(symbol=ord('a'), weight=2),
        LeafNode(symbol=ord('b'), weight=5),
        LeafNode(symbol=ord('c'), weight=1),
    ]
    shuffled_valid = [
        LeafNode(symbol=ord('a'), weight=1),
        LeafNode(symbol=ord('b'), weight=3),
        LeafNode(symbol=ord('c'), weight=4),
        LeafNode(symbol=ord('d'), weight=7),
    ]

    assert check_min_heap_valid([]) is True
    assert check_min_heap_valid([LeafNode(symbol=ord('b'), weight=3)]) is True
    assert check_min_heap_valid(heap) is True
    assert check_min_heap_valid(incorrect_heap) is False
    assert check_min_heap_valid(equal) is True
    assert check_min_heap_valid(right_bad) is False
    assert check_min_heap_valid(shuffled_valid) is True


def test_sift_up():
    heap = [
        LeafNode(ord('a'), 2),
        LeafNode(ord('b'), 3),
        LeafNode(ord('c'), 4)
    ]
    final_idx = sift_up(heap, 0)
    assert final_idx == 0
    assert check_min_heap_valid(heap)

    single_swap = [
        LeafNode(ord('a'), 2),
        LeafNode(ord('b'), 5),
        LeafNode(ord('c'), 6)
    ]
    single_swap.append(LeafNode(ord('d'), 3))
    final_idx = sift_up(single_swap, 3)
    assert final_idx == 1
    assert single_swap[1].weight == 3
    assert check_min_heap_valid(single_swap)

    multi_level_bubble = [
        LeafNode(symbol=ord('a'), weight=3),
        LeafNode(symbol=ord('b'), weight=5),
        LeafNode(symbol=ord('c'), weight=6),
        LeafNode(symbol=ord('d'), weight=7),
        LeafNode(symbol=ord('e'), weight=8),
    ]
    multi_level_bubble.append(LeafNode(ord('f'), 1))
    final_idx = sift_up(multi_level_bubble, 5)
    assert final_idx == 0
    assert check_min_heap_valid(multi_level_bubble)
    assert multi_level_bubble[0].symbol == ord('f') and multi_level_bubble[0].weight == 1
    



def test_pop_min():
    heap = [
        LeafNode(ord('a'), 1),
        LeafNode(ord('b'), 3),
        LeafNode(ord('c'), 6),
        LeafNode(ord('d'), 8),
        LeafNode(ord('e'), 10),
        LeafNode(ord('f'), 12),
        LeafNode(ord('g'), 15),
    ]

    smallest = pop_min(heap)
    assert smallest.weight == 1
    assert len(heap) == 6
    assert check_min_heap_valid(heap)


def test_push():
    heap = [
        LeafNode(ord('a'), 2),
        LeafNode(ord('b'), 3),
        LeafNode(ord('c'), 6),
        LeafNode(ord('d'), 8),
        LeafNode(ord('e'), 10),
        LeafNode(ord('f'), 12),
        LeafNode(ord('g'), 15),
    ]
    new_node = LeafNode(ord('h'), 1)
    push(heap, new_node)

    assert heap[0] == new_node
    assert check_min_heap_valid(heap)

