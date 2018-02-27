import numpy as np
import copy
from utils import io
from utils import matrix_generator
import numpy as np

epsilon = 10 ** -5


def nonzero(x):
    return np.abs(x) > epsilon


def argmax(lst):
    return lst.index(max(lst))


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
    m = io.read_matrix("../test/system3.test")
    size = len(m)

    B = copy.deepcopy([x[size] for x in m])
    A = copy.deepcopy([x[:size] for x in m])

    a = copy.deepcopy([A[i][i] for i in range(size)])
    b = copy.deepcopy([A[i][i + 1] for i in range(size - 1)])
    c = copy.deepcopy([A[i + 1][i] for i in range(size - 1)])

    print(a)
    print(b)
    print(c)

    b_prime = []
    for i in range(size - 1):
        if i == 0:
            b_prime.append(b[0] / a[0])
        else:
            b_prime.append(b[i] / (a[i] - c[i-1] * b_prime[i - 1]))

    d_prime = []
    for i in range(size):
        if i == 0:
            d_prime.append(B[0] / a[0])
        else:
            d_prime.append((B[i] - c[i - 1] * d_prime[i - 1]) / (a[i] - c[i - 1] * b_prime[i - 1]))

    x = [0 for i in range(size)]
    x[size - 1] = d_prime[size - 1]
    for i in range(size - 2, -1, -1):
        x[i] = d_prime[i] - b_prime[i] * x[i + 1]

    print(x)
    print(np.linalg.solve(A, B))

    print(np.linalg.norm(A @ np.array(x) - B))
    print(np.linalg.norm(x - np.linalg.solve(A, B)))
    print(np.linalg.norm(x - np.linalg.inv(A).dot(B)))
