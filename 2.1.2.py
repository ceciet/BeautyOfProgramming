__author__ = 'qdiao'

def insert_sort2(A):

    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]<key:
            A[i+1]=A[i]
            i=i-1
        A[i+1] = key

    return A



def insert_sort(A):

    N = len(A)
#    print N
    for i in range(1, N):
        tmp = A[i]
        #print tmp
        for j in range(0, i):
            print A[i-j-1]
            if tmp >= A[i-j-1]:
                A[i-j] = A[i-j-1]
            else:
                break
        if j != 0:
            A[i-j-1] = tmp

        print "-------------------------------"
    return A


if __name__ == "__main__":

    A = [4,3,5,12,421,2]
    print insert_sort(A)
    A = [4,3,5,12,421,2]
    print insert_sort2(A)
