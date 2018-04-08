import matplotlib.pyplot as plt
import numpy as np

# from Polynomial import Polynomial
#
# x0 = 1
# xn = 5
# n = 4
# h = (xn - x0) / n
#
# p = Polynomial('../test/poli.txt')
#
#
# def f1(value, function):
#     mapping = dict()
#
#     for i in range(n):
#         mapping[x0 + i * h] = function(x0 + i * h)
#
#     return mapping[value]

x0 = 0
xn = 5
n = 5
h = (xn - x0) / n


def f2(value):
    mapping = dict()
    mapping[0] = 50
    mapping[1] = 47
    mapping[2] = -2
    mapping[3] = -121
    mapping[4] = -310
    mapping[5] = -545

    return mapping[value]


def get_Lagrange_interpolation_value_dumb(value, value_function):
    sum = 0
    for i in range(n):
        product = 1
        for j in range(n):
            if i == j:
                continue
            product *= (value - get_x(j)) / (get_x(i) - get_x(j))
        sum += product * value_function(get_x(i))

    return sum


def get_Lagrange_interpolation_value(value, value_function):
    t = (value - x0) / h
    y0 = value_function(x0)

    deltas = get_delta_f_x0(value_function)
    sks = get_sks_dumb(t)

    lagrange_value = y0
    for i in range(n):
        lagrange_value += deltas[i + 1] * sks[i]

    return lagrange_value


def get_delta_f_x0(value_function):
    deltas = [value_function(x0)]

    for i in range(n):
        deltas.append(value_function(get_x(i)))

    for i in range(n):
        for j in range(n, i, -1):
            deltas[j] = deltas[j] - deltas[j - 1]

    return deltas


def get_x(i):
    return x0 + (i + 1) * h


def get_sks_dumb(t):
    sks = []

    for k in range(1, n + 1):
        result = 1
        for i in range(0, k):
            result *= (t - i)
        for i in range(1, k + 1):
            result /= k

        sks.append(result)
    return sks


def get_sks(t):
    sks = [t]

    for k in range(1, n):
        sks.append(sks[k - 1] * ((t - k + 1) / k))

    return sks


def get_least_squares_value(value):
    pass


print(get_Lagrange_interpolation_value(1.5, f2))
print(get_sks(10))
print(get_sks_dumb(10))

xs = np.arange(x0, xn, h)
ys = [f2(x) for x in xs]
plt.plot(xs, ys, linewidth=2.0)

xs = np.arange(x0, xn, h / 100)
ys = [get_Lagrange_interpolation_value(x, f2) for x in xs]
plt.plot(xs, ys, linewidth=2.0)
plt.show()
