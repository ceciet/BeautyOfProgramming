__author__ = 'qdiao'
import random

def exchange(A, i, j):

    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def quickSort(A, p, r):

    if p < r:
        q = partition(A, p, r)
        print A
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def partition(A, p, r):

    i = p-1
    x = A[r]
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            exchange(A, i, j)
        # print i
        # print A

    exchange(A, i+1, r)
    return i + 1

if __name__ == "__main__":

    l = [random.randint(1,100) for e in range(0, 10)]
    print l
    #print Merge(l, 0, 5, 9)
    quickSort(l, 0, 9)
    print l
