import numpy as np
import copy
from utils import io
from utils import matrix_generator
import math

epsilon = 10 ** -12


def nonzero(x):
    return np.abs(x) > epsilon


def argmax(lst):
    return lst.index(max(lst, key=lambda x: abs(x)))


def get_pivot(lower_elements):
    return argmax(lower_elements)


def tridiagonal(matrix, l, size):
    lower_elements = [matrix[i][l] for i in range(l, size)]
    pivot = get_pivot(lower_elements)

    i0 = pivot + l

    matrix[i0], matrix[l] = matrix[l], matrix[i0]

    if not nonzero(matrix[l][l]):
        return False

    for i in range(l + 1, size):
        f = matrix[i][l] / matrix[l][l]
        for j in range(l + 1, size + 1):
            matrix[i][j] = matrix[i][j] - f * matrix[l][j]
        matrix[i][l] = 0

    return True


def print_matrix(m, size):
    for i in range(size):
        for j in range(size):
            print(str(m[i][j]), end=" ")
        print()
    print()


if __name__ == '__main__':
    m = io.read_matrix("../test/system2.test")
    m = matrix_generator.generate_random_matrix(100, 101, 100)
    m[0][0] = epsilon * 10
    size = len(m)

    b = copy.deepcopy([x[size] for x in m])
    a = copy.deepcopy([x[:size] for x in m])

    # print(a)
    # print(b)

    for i in range(size):
        if not tridiagonal(m, i, size):
            print('Matrix is not singular')
            exit()

    x = [0 for i in range(size)]
    for i in range(size - 1, -1, -1):
        s = 0
        for j in range(i + 1, size):
            s += x[j] * m[i][j]
        if not nonzero(m[i][i]):
            print("Matrix is singular")
            exit()
        x[i] = (m[i][size] - s) / m[i][i]

    print(x)

    print(np.linalg.norm(a @ np.array(x) - b))
    print(np.linalg.norm(x - np.linalg.solve(a, b)))
    print(np.linalg.norm(x - np.linalg.inv(a).dot(b)))
