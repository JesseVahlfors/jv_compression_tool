"""Min-heap helper operations used to build the Huffman tree."""

from compression_tool.tree import Node

def build_min_heap(heap: list[Node]) -> list:
    """
    Build a binary min-heap from a list of nodes.

    Args:
        heap: list of node objects with .weight attribute

    Returns:
        The same list object, reordered in-place into a valid min-heap.
    """
    
    for i in range((len(heap)//2) -1, -1, -1): # start from last non-leaf node, stop at idx 0, step -1 meaning negative steps.
        sift_down(heap, i)
    return heap

def sift_down(heap: list[Node], i: int):
    """
    Restore the min-heap property by sifting a node down the tree.

    Args:
        heap: list of node objects with .weight attribute
        i: Index from which to start sifting down.

    Raises:
        IndexError: If i is outside the bounds of the heap.
    """

    n = len(heap)
    if i < 0 or i >= n:
        raise IndexError(f"The index is out of range ({i})")
    if i == n//2:
        return
    
    left_index = i*2 + 1 
    right_index = i*2 + 2 
    smallest = i 

    if left_index < n and comes_before(heap[left_index], heap[smallest]): 
        smallest = left_index

    if right_index < n and comes_before(heap[right_index], heap[smallest]):
        smallest = right_index

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        sift_down(heap, smallest)

def sift_up(heap: list[Node], idx: int) -> int:
    """
    Restore the min-heap property by sifting a node up toward the root.

    Args:
        heap: list of node objects with .weight attribute
        idx: Index from which to start sifting up.

    Returns:
        The final index of the node after sifting.

    Raises:
        IndexError: If idx is outside the bounds of the heap. 
    """

    if idx < 0 or idx >= len(heap):
        raise IndexError(f"The index is out of range ({idx})")
    
    if idx == 0:
        return 0
    
    while idx > 0:
        parent = (idx - 1) // 2
        if comes_before(heap[idx], heap[parent]):
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break

    return idx

def comes_before(a: Node, b:Node) -> bool:
    """
     Compare two nodes according to heap ordering.

    Nodes are ordered first by weight; for equal weights, leaf nodes
    are ordered by their symbol value if both nodes have a .symbol attribute.
    
    Args:
        a: First node to compare.
        b: Second node to compare.

    Returns:
        True if a should come before b in the min-heap, False otherwise.
    """

    if a.weight != b.weight: 
        return a.weight < b.weight
    if hasattr(a, "symbol") and hasattr(b, "symbol"):
        return a.symbol < b.symbol
    return False
    

def pop_min(heap: list[Node]):
    """
    Removes smallest weight value node from the heap and returns it.

    Args:
        heap: list of node objects with .weight attribute

    Returns:
        The node at the root of the heap (the minimum element).
    
    Raises:
        IndexError: If called on an empty heap.

    """
    
    if len(heap) == 0:
        raise IndexError("pop_min from an empty heap")
    if len(heap) == 1:
        return heap.pop()
    heap[-1],heap[0] = heap[0], heap[-1]
    root = heap.pop()
    sift_down(heap, 0)
    return root
    


def heap_push(heap: list[Node], node: Node) -> int:
    """
    Push a new node into the heap and restore the min-heap property.

    Args:
        heap: list of node objects with .weight attribute
        node: Node to insert into the heap.

    Returns:
        The index of the inserted node after sifting up.
    
    """

    heap.append(node)
    return sift_up(heap, len(heap) -1)

def check_min_heap_valid(heap: list[Node]) -> bool:
    """ 
    Check whether a list of nodes satisfies the min-heap property.

    Args:
        heap: List of node objects with a .weight attribute.

    Returns:
        True if the list represents a valid min-heap, False otherwise.
    """

    n = len(heap)
    if n <= 1:
        return True
    
    for i in range(n//2):
        left, right = 2 * i + 1, 2 * i + 2

        if left < n and heap[left].weight < heap[i].weight: 
            #as long as the length of the list is higher than the left index do the comparison
            return False
        if right < n and heap[right].weight < heap[i].weight:
            return False
    
    return True