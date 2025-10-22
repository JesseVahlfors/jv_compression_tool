
def build_min_heap(data):
    return data

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
