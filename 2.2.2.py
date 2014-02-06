__author__ = 'qdiao'
import random

def selectSort(A):

    for i in range(0, len(A)):
        min = A[i]
        index = i
        for j in range(i+1, len(A)):
            if min>A[j]:
                min = A[j]
                index = j
        if index!=i:
            A[index]=A[i]
            A[i] = min
    return A

if __name__ == "__main__":

    l = [random.randint(1,100) for e in range(random.randint(10,20))]
    print l
    print selectSort(l)
