import random
from math import sqrt

import numpy as np

from SparseMatrix import SparseMatrix
from utils import io

EPSILON = 10 ** -10
KMAX = 1000


def is_symmetric(file):
    file_matrix1 = io.read_system(file, no_b=False)
    matrix1 = SparseMatrix(*file_matrix1)

    file_matrix2 = io.read_system(file, no_b=False)
    matrix2 = SparseMatrix(*file_matrix2, columns=True)

    return matrix1 == matrix2

def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)


def norm(vector):
    return sqrt(sum([x ** 2 for x in vector]))


def generate_random_vector(size):
    vector = [random.random() * 1000 for i in range(size)]
    n = norm(vector)

    return [x / n for x in vector]


def dot_product(v1, v2):
    return sum([i * j for i, j in zip(v1, v2)])


def power_method(A):
    v = generate_random_vector(A.size)
    print(norm(v))
    w = A.multiply_vector(v)
    l = dot_product(w, v)
    k = 0
    while k <= KMAX and norm([x - l * y for x, y in zip(w, v)]) > A.size * EPSILON:
        n = norm(w)
        v = [x / n for x in w]

        w = A.multiply_vector(v)
        l = dot_product(w, v)
        k += 1
    if k > KMAX:
        print("NU am gasit solutia")
    else:
        print("Am oprit dupa " + str(k) + " operatii")
        print(l)


def generate_random_symmetric_matrix(size):
    m = [[0 for x in range(size)] for y in range(size)]
    while not all([True if len(line) == size / 10 else False for line in m]):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)

        if len(m[i]) < size / 10 and len(m[j]) < size / 10:
            element = random.random() * 1000
            m[i][j] = element
            m[j][i] = element

    return m


def generate_random_symmetric_matrix2(size):
    m = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(i):
            prob = random.random()
            if prob < 0.07:
                element = random.random() * 1000
                m[i][j] = element
                m[j][i] = element

    return m


if __name__ == "__main__":
    file_matrix = io.read_system("../test/m_rar_sim_2018_300.txt", no_b=False)
    matrix1 = SparseMatrix(*file_matrix)

    # print(is_symmetric("../test/m_rar_sim_2018.txt"))

    power_method(matrix1)

    m2 = generate_random_symmetric_matrix2(1000)
    sizes = [len(list(filter(lambda x: x != 0, line))) for line in m2]
    print(sizes)
    print(check_symmetric(np.matrix(m2)))

    matrix2 = SparseMatrix(1000, [], from_matrix=m2)
    power_method(matrix2)

    # print(m2)

    # part 2

    n = 2
    m = 3

    a = np.array([[3, 2, 2],
                  [2, 3, -2]])

    # set numpy printing options
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=3)

    print("--- FULL ---")
    U, s, VT = np.linalg.svd(a, full_matrices=True)
    V = VT.transpose()

    print("U:\n {}".format(U))
    print("s:\n {}".format(s))
    print("VT:\n {}".format(VT))

    non_negative = list(filter(lambda x: x != 0, s))

    print("--- Valori singulare ---")
    print(non_negative)

    print("--- Rang ---")
    rank = len(non_negative)
    print(len(non_negative))

    print("--- Numar de conditionare ---")
    print(max(non_negative) / min(non_negative))

    print("--- Inversa Moore-Penrose ---")
    inverse_s = [[1 / s[i] if i < rank and i == j else 0 for j in range(n)] for i in range(m)]
    moore_penrose = np.dot(np.dot(np.matrix.transpose(VT), inverse_s), np.matrix.transpose(U))
    print(moore_penrose)

    print("--- Vectorul x1 --")
    b = [[7], [3]]
    print(np.dot(moore_penrose, b))

    s = int(input("Introdu s < {}:".format(rank)))
    print("--- Matricea A{} --".format(s))

    result = np.empty(shape=a.shape)
    for i in range(s):
        ui = U[:, i]
        vi = V[:, i]

        ui.shape = (n, 1)
        vi.shape = (1, m)

        ai = np.multiply(non_negative[i], np.dot(ui, vi))
        result = np.add(result, ai)

    print(result)
    print(np.linalg.norm(result, ord=np.inf))
