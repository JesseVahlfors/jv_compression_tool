from tree import Node, LeafNode, InternalNode
from heapify import build_min_heap
# Convert freq → list of LeafNodes → heapify → loop merge.

def pop_min(heap) -> LeafNode:
    pass



def build_tree(freq: dict[int, int]) -> Node | None:

    if freq == {}:
        return None
    
    heap = [LeafNode(symbol, weight) for symbol, weight in freq.items()]

    heap = build_min_heap(heap)

    while len(heap) > 1:
        pass

    
