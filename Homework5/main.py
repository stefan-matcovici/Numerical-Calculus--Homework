import numpy as np

from utils.matrix_generator import generate_random_matrix

K_MAX = 1000
EPSILON = 10 ** -10


def complete_super_diagonal(matrix, order, value):
    matrix.ravel()[1:max(0, order - 1) * order:matrix.shape[1] + 1] = [value for i in range(order - 1)]


def get_A(order):
    a = np.zeros((order, order))
    np.fill_diagonal(a, 1)
    complete_super_diagonal(a, order, 4)

    return a


def get_random(order):
    return np.random.rand(order, order)


def get_first_norm(a):
    return max(abs(np.sum(a, axis=0)))


def get_infinite_norm(a):
    return max(np.sum(a, axis=1))


def compute_v1_1(v, a):
    result = np.dot(np.multiply(a, -1), v)
    diagonal = result.diagonal()
    np.fill_diagonal(result, diagonal + 2)

    result = np.dot(v, result)
    return result


def compute_v1_2(v, a):
    result1 = np.dot(np.multiply(a, -1), v)
    intermediate_result = np.copy(result1)

    diagonal = result1.diagonal()
    np.fill_diagonal(result1, diagonal + 3)

    result = np.dot(intermediate_result, result1)
    diagonal = result.diagonal()
    np.fill_diagonal(result, diagonal + 3)

    result = np.dot(v, result)

    return result


def compute_v1_3(v, a):
    result1 = np.dot(v, np.multiply(a, -1))
    intermediate_result = np.copy(result1)

    diagonal = result1.diagonal()
    np.fill_diagonal(result1, diagonal + 3)

    diagonal = intermediate_result.diagonal()
    np.fill_diagonal(intermediate_result, diagonal + 1)

    result = np.multiply(1.0 / 4, np.dot(intermediate_result, result1))
    result = np.dot(result, result1)

    diagonal = result.diagonal()
    np.fill_diagonal(result, diagonal + 1)

    result = np.dot(result, v)

    return result


def compute_inverse(order, compute_v0, compute_v1):
    a = get_A(order)
    # a = get_random(order)

    v1 = compute_v0(a)
    k = 0
    delta = 1
    while k < K_MAX and EPSILON <= delta <= 10 ** 10:
        v0 = v1
        v1 = compute_v1(v1, a)
        delta = get_first_norm(np.subtract(v1, v0))
        k = k + 1

    if delta < EPSILON:
        print("convergenta dupa " + str(k) + " iteratii")
        print(v1)
        print(delta)
        result = np.dot(a, v1)
        diagonal = result.diagonal()
        np.fill_diagonal(result, diagonal - 1)
        print(get_first_norm(result))
    else:
        print("divergenta")


def compute_v0_1(a):
    a1 = get_first_norm(a)
    a2 = get_infinite_norm(a)
    return np.divide(a.transpose(), a1 * a2)


def compute_v0_2(a):
    result = np.zeros(a.shape)
    diagonal = a.diagonal()

    np.fill_diagonal(result, 1.0 / diagonal)
    return result


if __name__ == "__main__":
    compute_inverse(10, compute_v0_1, compute_v1_1)
    compute_inverse(10, compute_v0_1, compute_v1_2)
    compute_inverse(10, compute_v0_1, compute_v1_3)
