import random
from math import sqrt

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
        print(l)
    if k > KMAX:
        print("NU am gasit solutia")
    else:
        print("Am oprit dupa " + str(k) + " operatii")
        print(l)


def generate_random_symmetric_matrix(size):
    m = [[0 for x in range(size)] for y in range(size)]
    for i in range((size ** 2) / 2):
        i = random.randint(0, size)
        j = random.randint(0, size)

        element = random.random() * 1000
        m[i][j] = element
        m[j][i] = element

    return m


if __name__ == "__main__":
    file_matrix = io.read_system("../test/m_rar_sim_2018.txt", no_b=False)
    matrix1 = SparseMatrix(*file_matrix)

    # print(is_symmetric("../test/m_rar_sim_2018.txt"))

    power_method(matrix1)

    # m2 = generate_random_symmetric_matrix(1000)
    # matrix2 = SparseMatrix(1000, [], m2)
