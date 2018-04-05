from Polynomial import Polynomial

x0 = 1
xn = 5
n = 4

p = Polynomial('../test/poli.txt')


def f1(value, function):
    mapping = dict()
    h = (xn - x0) / n

    for i in range(n):
        mapping[x0 + i * h] = function(x0 + i * h)

    return mapping[value]


def f2(value):
    mapping = dict()
    mapping[0] = 50
    mapping[1] = 47
    mapping[2] = -2
    mapping[3] = -121
    mapping[4] = -310
    mapping[5] = -545

    return mapping[value]

