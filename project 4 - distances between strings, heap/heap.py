def parent(i):
    if i == 0:
        return None
    else:
        return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, i):
    lef = left(i)
    rig = right(i)
    largest = i
    if lef < len(A) and A[lef] > A[largest]:
        largest = lef
    if rig < len(A) and A[rig] > A[largest]:
        largest = rig
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def min_heapify(A, i):
    lef = left(i)
    rig = right(i)
    smallest = i
    if lef < len(A) and A[lef] < A[smallest]:
        smallest = lef
    if rig < len(A) and A[rig] < A[smallest]:
        smallest = rig
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)

def build_min_heap(A):
    for i in range(len(A) // 2, -1, -1):
        min_heapify(A, i)

A = [3, 7, 10, 16, 17, 2]
B = [3, 7, 10, 16, 17, 2]
print(f"this is a starting array: {A}")
build_max_heap(A)
print(f"this is max heap: {A}")
build_min_heap(B)
print(f"this is min heap: {B}")
