from compression_tool.tree import Node

def build_min_heap(heap: list[Node]) -> list:
    for i in range((len(heap)//2) -1, -1, -1): # start from last non-leaf node, stop at idx 0, step -1 meaning negative steps.
        sift_down(heap, i)
    return heap

def sift_down(heap: list[Node], i: int):
    n = len(heap) 
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
    #triggers after push insert, pushes towards the root, compares weights and uses symbol integer as tiebreaker, return final index and raise error if out of range.
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
    if a.weight != b.weight: 
        return a.weight < b.weight
    if hasattr(a, "symbol") and hasattr(b, "symbol"):
        return a.symbol < b.symbol
    return False
    

def pop_min(heap: list[Node]):
    if len(heap) == 0:
        raise IndexError("pop_min from an empty heap")
    if len(heap) == 1:
        return heap.pop()
    heap[-1],heap[0] = heap[0], heap[-1]
    root = heap.pop()
    sift_down(heap, 0)
    return root
    


def heap_push(heap: list[Node], node: Node) -> int:
    heap.append(node)
    return sift_up(heap, len(heap) -1)

def check_min_heap_valid(heap: list[Node]) -> bool:
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