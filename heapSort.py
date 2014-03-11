__author__ = 'qdiao'

import heapq

def parent(i):
    return (i - 1)/2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i

    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        #print A[largest]
        tmp = A[largest]
        A[largest] = A[i]
        A[i] = tmp
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    for i in range((len(A)-1)/2, -1, -1):
        max_heapify(A, i, heap_size)


def heap_increase_key(A, i, key):
    try:
        if key < A[i]:
            raise BaseException
        else:
            A[i] = key
            print parent(i)
            while i > 0 and A[parent(i)] < A[i]:
                tmp = A[parent(i)]
                A[parent(i)] = A[i]
                A[i] = tmp
                i = parent(i)
    except BaseException as e:
        print "Error: key must be large than A[i]"



def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(len(A)-1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        heap_size -= 1
        max_heapify(A, 0, heap_size)

def heap_sort2(A):
    heapq.heapify(A)
    heap = []
    while A:
        heap.append(heapq.heappop(A))
    A[:] = heap
    return A

if __name__ == "__main__":

    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    heap_sort(A)
    print A
    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print heap_sort2(A)
    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    build_max_heap(A)
    print A
    A.append(-100)
    heap_increase_key(A, len(A)-1, 10)
    print A
