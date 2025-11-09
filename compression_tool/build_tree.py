from compression_tool.tree import Node, LeafNode, InternalNode
from compression_tool.utils.heapify import build_min_heap, heap_push, pop_min, comes_before
# Convert freq → list of LeafNodes → heapify → loop merge.

def build_tree(freq: dict[int, int]) -> Node | None:
    if not freq:
        return None
    
    for sym, wt in freq.items():
        if not isinstance(sym, int) or not isinstance(wt, int) or wt <= 0:
            raise ValueError(f"Invalid pair: {sym!r}: {wt!r}")
        
    if len(freq) == 1:
        (sym, wt), = freq.items()
        return LeafNode(symbol=sym,weight=wt)
        
    
    heap = []
    for sym, wt in freq.items():
        heap_push(heap, LeafNode(symbol=sym, weight=wt))

    build_min_heap(heap)

    while len(heap) > 1:
        first = pop_min(heap)
        second = pop_min(heap)

        left, right = (first, second) if comes_before(first, second) else (second, first)
        parent = InternalNode(left=left, right=right)

        heap_push(heap, parent)

    return heap[0]

    
