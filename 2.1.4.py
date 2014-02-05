__author__ = 'qdiao'

def bigAdd(A, B, n):

    C = [0]*(n+1)
    flag = 0

    for i in range(n-1, -1, -1):
        C[i+1]=(A[i]+B[i]+flag)%10
        flag = (A[i]+B[i]+flag)/10

    C[0] = flag
    return C


if __name__ == "__main__":

    A = [5,5,6,5]
    B = [5,4,8,6]

    print bigAdd(A, B, len(A))