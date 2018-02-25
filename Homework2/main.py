import numpy as np

from utils import io

epsilon = 10 ** -5


def nonzero(x):
    return np.abs(x) > epsilon


def tridiagonal(matrix, l, size):
    lower_elements = matrix.transpose()[l][l:]
    nonzero_elements = np.where(nonzero(lower_elements))

    if len(nonzero_elements[0]) == 0:
        return None

    i0 = nonzero_elements[0][0] + l

    matrix[[i0, l]] = matrix[[l, i0]]

    for i in range(l + 1, size):
        f = matrix[i, l] / matrix[l][l]
        for j in range(l + 1, size + 1):
            matrix[i, j] = matrix[i, j] - f * matrix[l, j]
        matrix[i, l] = 0


if __name__ == '__main__':
    m = np.array(io.read_matrix("../test/matrix2.test"), dtype="float64")
    size = m.shape

    b = np.copy(m[:, size[0]])
    a = np.copy(m[:, :size[0]])

    for i in range(size[0]):
        tridiagonal(m, i, size[0])

    print(m)

    x = [0 for i in range(size[0])]
    for i in range(size[0] - 1, -1, -1):
        s = 0
        for j in range(i + 1, size[0]):
            s += x[j] * m[i, j]
        x[i] = (m[i][size[0]] - s) / m[i, i]

    print(x)

    print(a @ np.array([0.2941176, -0.3529412, -0.8235294]))
    print(a @ np.array(x))
