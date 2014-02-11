__author__ = 'qdiao'
import random
import math

flag = 500


def Merge(A, p, q, r):

    B = A[p:q+1]
    C = A[q+1:r+1]

    B.append(flag)
    C.append(flag)
    #print B
    #print C
    i = 0
    j = 0

    for k in range(p, r+1):
        if B[i] <= C[j]:
            #print i
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1

    return A[p:r+1]

def MergeSort(A, p, r):
    if p < r:
        q = (p+r)/2
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)
    return A

if __name__ == "__main__":

    l = [random.randint(1,100) for e in range(0, 10)]
    print l
    #print Merge(l, 0, 5, 9)
    print MergeSort(l, 0, 9)
