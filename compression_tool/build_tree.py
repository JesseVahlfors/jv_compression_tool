from compression_tool.tree import Node, LeafNode, InternalNode
from compression_tool.utils.heapify import build_min_heap
# Convert freq → list of LeafNodes → heapify → loop merge.

def build_tree(freq: dict[int, int]) -> Node | None:

    if freq == {}:
        return None
    
    heap = [LeafNode(symbol, weight) for symbol, weight in freq.items()]

    heap = build_min_heap(heap)

    pass

    
