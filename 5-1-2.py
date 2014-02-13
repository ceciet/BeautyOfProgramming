__author__ = 'qdiao'
import random
import math

def biasedRandom():

    i = random.randint(0, 3)
    if i >= 1:
        i = 1
    return i


def equalRandom():

    while True:
        i = biasedRandom()
        j = biasedRandom()
        if (i+j)!=1:
            continue
        if i == 0 and j == 1:
            return 0
        if i == 1 and j == 0:
            return 1

def test():

    m = 0
    n = 0
    for i in range(0, 501):
        i = equalRandom()
        if i == 1:
            m += 1
        else:
            n += 1
    return m, n

def randomAB(a, b):

    m = int(math.log(b-a, 2))
    add = 0
    for i in range(0, m):
        j = random.randint(0, 1)
        add += math.pow(2, i)*j

    return int(a + add)


if __name__ == "__main__":

    print randomAB(10, 20)
    #equalRandom()
    print test()