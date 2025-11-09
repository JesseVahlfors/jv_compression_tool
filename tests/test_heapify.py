from compression_tool.utils.heapify import build_min_heap, sift_down, comes_before, check_min_heap_valid, sift_up, pop_min, heap_push
from compression_tool.tree import Node, LeafNode, InternalNode
import pytest

#Node constructor
def n(symbol: str, weight: int) -> LeafNode:
    return LeafNode(symbol=ord(symbol), weight=weight)

def test_heapify_simple():
    heap = [n('f', 45),
            n('c', 12),
            n('a', 5),
            n('e', 16),
            n('d', 13),
            n('b', 9),
    ]
    heap = build_min_heap(heap)

    assert heap[0].weight == min(node.weight for node in heap)


def test_sift_down():
    heap = [
        n('a', 3),
        n('b', 1),
        n('c', 4),
        n('d', 2),
        n('e', 5),
        n('f', 6),
    ]

    sift_down(heap, 0)

    assert heap[0].weight == 1
    assert check_min_heap_valid(heap)


def test_check_min_heap_valid():
    heap = [
        n('a', 2),
        n('b', 3),
        n('c', 4),
        n('d', 5),
        n('e', 6),
        n('f', 7),
    ]
    incorrect_heap = [
        n('a', 2),
        n('b', 30),
        n('c', 4),
        n('d', 5),
        n('e', 6),
        n('f', 7),
    ]
    equal = [ n('a', 2), n('b', 2), n('c', 2), ]

    right_bad = [ n('a', 2), n('b', 5), n('c', 1), ]

    shuffled_valid = [ n('a', 1), n('b', 3), n('c', 4), n('d', 7), ]   

    assert check_min_heap_valid([]) is True
    assert check_min_heap_valid([('b', 3)]) is True
    assert check_min_heap_valid(heap) is True
    assert check_min_heap_valid(incorrect_heap) is False
    assert check_min_heap_valid(equal) is True
    assert check_min_heap_valid(right_bad) is False
    assert check_min_heap_valid(shuffled_valid) is True


def test_sift_up_root_noop():
    heap = [ n('a', 2), n('b', 3), n('c', 4) ]
    final_idx = sift_up(heap, 0)
    assert final_idx == 0
    assert check_min_heap_valid(heap)

def test_sift_up_single_swap():
    single_swap = [ n('a', 2), n('b', 5), n('c', 6) ]
    single_swap.append(n('d', 3))
    final_idx = sift_up(single_swap, 3)
    assert final_idx == 1
    assert single_swap[1].weight == 3
    assert check_min_heap_valid(single_swap)

def test_sift_up_multi_level_bubble():
    multi_level_bubble = [
        n('a', 3),
        n('b', 5),
        n('c', 6),
        n('d', 7),
        n('e', 8),
    ]
    multi_level_bubble.append(n('f', 1))
    final_idx = sift_up(multi_level_bubble, 5)
    assert final_idx == 0
    assert check_min_heap_valid(multi_level_bubble)
    assert multi_level_bubble[0].symbol == ord('f') and multi_level_bubble[0].weight == 1

def test_sift_up_tie_break_symbol():
    tie_break = [ n('a', 2), n('c', 2), n('d', 3) ]
    tie_break.append(n('b',2))
    final_idx = sift_up(tie_break, 3)
    assert final_idx == 1
    assert tie_break[3].symbol == ord('c') and tie_break[1].symbol == ord('b')
    assert check_min_heap_valid(tie_break)

def test_sift_up_out_of_range_raises():
    out_of_range = [ n('a', 2), n('b', 3), n('c', 4) ]
    with pytest.raises(IndexError): sift_up(out_of_range, len(out_of_range))
    with pytest.raises(IndexError): sift_up(out_of_range, -1)

def test_sift_up_no_swap_when_equal():
    no_swap_when_equal = [ n('a', 2), n('b', 2), n('f', 3) ]
    no_swap_when_equal.append(n('c', 2))
    final_idx = sift_up(no_swap_when_equal, 3)
    assert final_idx == 3
    assert no_swap_when_equal[1].symbol == ord('b') and no_swap_when_equal[3].symbol == ord('c')
    assert check_min_heap_valid(no_swap_when_equal)

def test_comes_before_weight_then_symbol():
    a,b,c =  n('a', 2), n('b', 2), n('c', 3)
    assert comes_before(a, b)          # same weight, smaller symbol
    assert not comes_before(b, a)
    assert comes_before(a, c)          # smaller weight wins
    assert not comes_before(c, a)
    
def test_pop_min_empty_raises():
    heap = []
    with pytest.raises(IndexError):
        pop_min(heap)

def test_pop_min_single_element():
    heap = [n('a',1)]

    node = pop_min(heap)

    assert node.symbol == ord('a') and node.weight == 1
    assert heap == []

def test_pop_min_remove_root():
    heap = [n('a',2), n('d',5), n('b',6), n('c',7), n('e',8)]

    node = pop_min(heap)

    assert node.weight == 2 and node.symbol == ord('a')
    assert len(heap) == 4
    assert check_min_heap_valid(heap)

def test_pop_min_tie_break():
    heap = [ n('a', 2), n('b', 2), n('c', 3), n('d',8) ]
    
    first = pop_min(heap)
    second = pop_min(heap)

    assert first.symbol == ord('a')
    assert second.symbol == ord('b')
    assert check_min_heap_valid(heap)

def test_pop_min_pops_in_order():
    heap = [n('d',4), n('a',2), n('c',2), n('b',2), n('e',5), n('f',3)]
    build_min_heap(heap)

    popped = []
    while len(heap) > 0:
        popped.append(pop_min(heap))

    assert [(x.weight, x.symbol) for x in popped] == sorted([(z.weight, z.symbol) for z in popped])
    assert heap == []


def test_heap_push():
    heap = [n('a',2), n('b',5), n('c',6)]
    node = n('d', 3)

    final_idx = heap_push(heap, node)
    assert final_idx == 1
    assert (heap[0].symbol, heap[0].weight) == (ord('a'), 2)
    assert (heap[1].symbol, heap[1].weight) == (ord('d'), 3) 
    assert (heap[3].symbol, heap[3].weight) == (ord('b'), 5)
    assert check_min_heap_valid(heap)

def test_multi_level_bubble_push():
    heap = [n('a',3), n('b',5), n('c',6), n('d',7)]
    node = n('e', 1)
    
    final_idx = heap_push(heap, node)
    assert final_idx == 0
    assert (heap[0].symbol, heap[0].weight) == (ord('e'),1)
    assert check_min_heap_valid(heap)
