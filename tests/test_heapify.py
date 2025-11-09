from compression_tool.utils.heapify import build_min_heap, sift_down, comes_before, check_min_heap_valid, sift_up, pop_min, push
from compression_tool.tree import Node, LeafNode, InternalNode
import pytest

#Node constructor
def n(symbol: int, weight: int) -> LeafNode:
    return LeafNode(symbol=symbol, weight=weight)

def test_heapify_simple():
    heap = [n(ord('f'), 45),
            n(ord('c'), 12),
            n(ord('a'), 5),
            n(ord('e'), 16),
            n(ord('d'), 13),
            n(ord('b'), 9),
    ]
    heap = build_min_heap(heap)

    assert heap[0].weight == min(node.weight for node in heap)


def test_sift_down():
    heap = [
        n(ord('a'), 3),
        n(ord('b'), 1),
        n(ord('c'), 4),
        n(ord('d'), 2),
        n(ord('e'), 5),
        n(ord('f'), 6),
    ]

    sift_down(heap, 0)

    assert heap[0].weight == 1


def test_check_min_heap_valid():
    heap = [
        n(ord('a'), 2),
        n(ord('b'), 3),
        n(ord('c'), 4),
        n(ord('d'), 5),
        n(ord('e'), 6),
        n(ord('f'), 7),
    ]
    incorrect_heap = [
        n(ord('a'), 2),
        n(ord('b'), 30),
        n(ord('c'), 4),
        n(ord('d'), 5),
        n(ord('e'), 6),
        n(ord('f'), 7),
    ]
    equal = [ n(ord('a'), 2), n(ord('b'), 2), n(ord('c'), 2), ]

    right_bad = [ n(ord('a'), 2), n(ord('b'), 5), n(ord('c'), 1), ]

    shuffled_valid = [ n(ord('a'), 1), n(ord('b'), 3), n(ord('c'), 4), n(ord('d'), 7), ]   

    assert check_min_heap_valid([]) is True
    assert check_min_heap_valid([(ord('b'), 3)]) is True
    assert check_min_heap_valid(heap) is True
    assert check_min_heap_valid(incorrect_heap) is False
    assert check_min_heap_valid(equal) is True
    assert check_min_heap_valid(right_bad) is False
    assert check_min_heap_valid(shuffled_valid) is True


def test_sift_up_root_noop():
    heap = [ n(ord('a'), 2), n(ord('b'), 3), n(ord('c'), 4) ]
    final_idx = sift_up(heap, 0)
    assert final_idx == 0
    assert check_min_heap_valid(heap)

def test_sift_up_single_swap():
    single_swap = [ n(ord('a'), 2), n(ord('b'), 5), n(ord('c'), 6) ]
    single_swap.append(n(ord('d'), 3))
    final_idx = sift_up(single_swap, 3)
    assert final_idx == 1
    assert single_swap[1].weight == 3
    assert check_min_heap_valid(single_swap)

def test_sift_up_multi_level_bubble():
    multi_level_bubble = [
        n(ord('a'), 3),
        n(ord('b'), 5),
        n(ord('c'), 6),
        n(ord('d'), 7),
        n(ord('e'), 8),
    ]
    multi_level_bubble.append(n(ord('f'), 1))
    final_idx = sift_up(multi_level_bubble, 5)
    assert final_idx == 0
    assert check_min_heap_valid(multi_level_bubble)
    assert multi_level_bubble[0].symbol == ord('f') and multi_level_bubble[0].weight == 1

def test_sift_up_tie_break_symbol():
    tie_break = [ n(ord('a'), 2), n(ord('c'), 2), n(ord('d'), 3) ]
    tie_break.append(n(ord('b'),2))
    final_idx = sift_up(tie_break, 3)
    assert final_idx == 1
    assert tie_break[3].symbol == ord('c') and tie_break[1].symbol == ord('b')
    assert check_min_heap_valid(tie_break)

def test_sift_up_out_of_range_raises():
    out_of_range = [ n(ord('a'), 2), n(ord('b'), 3), n(ord('c'), 4) ]
    with pytest.raises(IndexError): sift_up(out_of_range, len(out_of_range))
    with pytest.raises(IndexError): sift_up(out_of_range, -1)

def test_sift_up_no_swap_when_equal():
    no_swap_when_equal = [ n(ord('a'), 2), n(ord('b'), 2), n(ord('f'), 3) ]
    no_swap_when_equal.append(n(ord('c'), 2))
    final_idx = sift_up(no_swap_when_equal, 3)
    assert final_idx == 3
    assert no_swap_when_equal[1].symbol == ord('b') and no_swap_when_equal[3].symbol == ord('c')
    assert check_min_heap_valid(no_swap_when_equal)

def test_comes_before_weight_then_symbol():
    a,b,c =  n(ord('a'), 2), n(ord('b'), 2), n(ord('c'), 3)
    assert comes_before(a, b)          # same weight, smaller symbol
    assert not comes_before(b, a)
    assert comes_before(a, c)          # smaller weight wins
    assert not comes_before(c, a)
    


def test_pop_min():
    heap = [
        n(ord('a'), 1),
        n(ord('b'), 3),
        n(ord('c'), 6),
        n(ord('d'), 8),
        n(ord('e'), 10),
        n(ord('f'), 12),
        n(ord('g'), 15),
    ]

    smallest = pop_min(heap)
    assert smallest.weight == 1
    assert len(heap) == 6
    assert check_min_heap_valid(heap)


def test_push():
    heap = [
        n(ord('a'), 2),
        n(ord('b'), 3),
        n(ord('c'), 6),
        n(ord('d'), 8),
        n(ord('e'), 10),
        n(ord('f'), 12),
        n(ord('g'), 15),
    ]
    new_node = n(ord('h'), 1)
    push(heap, new_node)

    assert heap[0] == new_node
    assert check_min_heap_valid(heap)

