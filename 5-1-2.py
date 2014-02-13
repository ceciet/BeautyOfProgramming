__author__ = 'qdiao'
import random
import math


def randomAB(a, b):

    m = int(math.log(b-a, 2))
    add = 0
    for i in range(0, m):
        j = random.randint(0, 1)
        add += math.pow(2, i)*j

    return int(a + add)


if __name__ == "__main__":

    print randomAB(10, 20)