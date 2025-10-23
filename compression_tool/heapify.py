
def build_min_heap(heap):
    for i in range((len(heap)//2) -1, -1, -1): # start from last non-leaf node, stop at idx 0, step -1 meaning negative steps.
        sift_down(heap, i)
    return heap

def sift_down(heap, i):
    n = len(heap) 
    left_index = i*2 + 1 
    right_index = i*2 + 2 

    smallest = i 

    if left_index < n and heap[left_index][0] < heap[smallest][0]: 
        smallest = left_index
    if right_index < n and heap[right_index][0] < heap[smallest][0]:
        smallest = right_index

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        sift_down(heap, smallest)

def check_min_heap_valid(heap):
    pass