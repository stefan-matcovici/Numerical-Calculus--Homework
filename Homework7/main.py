from Polynomial import Polynomial

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


def get_Lagrange_interpolation_value(value, value_function):
    t = (value - x0) / h
    y0 = value_function(x0)

    deltas = get_delta_f_x0(value_function)
    sks = get_sks(t)

    lagrange_value = y0
    for i in range(n):
        lagrange_value += deltas[i] * sks[i]

    return lagrange_value


def get_delta_f_x0(value_function):
    deltas = [value_function(x0)]

    for i in range(n):
        deltas.append(value_function(x0 + (i + 1) * h))

    for i in range(n):
        for j in range(n, i, -1):
            deltas[j] = deltas[j] - deltas[j - 1]

    return deltas


def get_sks(t):
    sks = [t]

    for k in range(1, n):
        sks.append(sks[k - 1] * (t - k + 1) / k)

    return sks


def get_least_squares_value(value):
    pass


print(get_Lagrange_interpolation_value(1.5, f2))