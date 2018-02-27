import problem1
import problem2
import problem3
from Matrix import Matrix
import numpy as np
from utils import io
from utils import matrix_generator

import timeit

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22], [23, 24, 25, 26]]

matrix3 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
matrix4 = [[11, 12, 13], [15, 16, 17], [19, 20, 21]]

matrix5 = [[i for i in range(1, 17)] for x in range(16)]

matrix6 = [[1] * 16 for i in range(16)]

matrix7 = [[1, 2], [1, 2]]
matrix8 = [[-2, -2], [-2, -2]]

# problem 1
print(problem1.get_machine_precision())

# problem 2
m = problem1.get_machine_precision()
print(problem2.get_nonassociative_numbers())
print(problem2.test_sum_nonassociativity(1.0, 2, 3))
print(problem2.test_sum_nonassociativity(1.0, 10 ** -m, 10 ** -m))

print(problem2.test_multiplication_nonassociativity(2, 3, 4))
print(problem2.test_multiplication_nonassociativity(0.7, 0.2, 0.1))
print((0.7 * 0.2) * 0.1)
print(0.7 * (0.2 * 0.1))

# problem 3
# print(Matrix(matrix1))
# print(Matrix(matrix2))
print(Matrix(matrix1).strassen_multiply(Matrix(matrix2), 1))
print(np.dot(matrix1, matrix2))

# print(Matrix(matrix3))
# print(Matrix(matrix4))
print(Matrix(matrix3).strassen_multiply(Matrix(matrix4), 1))
print(np.dot(matrix3, matrix4))


print(Matrix(matrix7))
print(Matrix(matrix8))
print(Matrix(matrix7).strassen_multiply(Matrix(matrix8), 0))
print(Matrix(matrix7) * Matrix(matrix8))
print(np.dot(matrix7, matrix8))

# random_matrix1 = matrix_generator.generate_random_matrix(10, 10, 1000)
# random_matrix2 = matrix_generator.generate_random_matrix(10, 10, 1000)
#
# print(Matrix(random_matrix1))
# print()
# print(Matrix(random_matrix2))
#
# print()
#
# print(timeit.timeit("Matrix(random_matrix1).strassen_multiply(Matrix(random_matrix2), 8)",
#                     setup="from Matrix import Matrix\nfrom utils import matrix_generator\nrandom_matrix1 = matrix_generator.generate_random_matrix(1024, 1024, 1000)\nrandom_matrix2 = matrix_generator.generate_random_matrix(1024, 1024, 1000)",
#                     number=1))
#
# print(timeit.timeit("Matrix(random_matrix1) * Matrix(random_matrix2)",
#                     setup="from Matrix import Matrix\nfrom utils import matrix_generator\nrandom_matrix1 = matrix_generator.generate_random_matrix(1024, 1024, 1000)\nrandom_matrix2 = matrix_generator.generate_random_matrix(1024, 1024, 1000)",
#                     number=1))
