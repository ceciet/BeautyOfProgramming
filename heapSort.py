__author__ = 'qdiao'


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
    #return A


def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(len(A)-1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        heap_size -= 1
        max_heapify(A, 0, heap_size)

if __name__ == "__main__":

    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    heap_sort(A)
    print A
