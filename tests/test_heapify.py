from compression_tool.heapify import build_min_heap, sift_down
import pytest

def test_heapify_simple():
    data = [
        (45, b'f'),
        (12, b'c'),
        (5, b'a'),
        (16, b'e'),
        (13, b'd'),
        (9, b'b'),
        ]
    
    heap = build_min_heap(data)

    assert heap[0][0] == min(freq for freq, _ in data)

def test_sift_down():
    data = [
        (3, b'a'),
        (1, b'b'),
        (4, b'c'),
        (2, b'd'),
        (5, b'e'),
        (6, b'f'),
    ]

    sift_down(data, 0)

    assert data[0][0] == 1

