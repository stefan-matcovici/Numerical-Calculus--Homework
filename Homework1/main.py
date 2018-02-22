import problem1
import problem2
import problem3
from Matrix import Matrix
import numpy as np
from utils import io

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22], [23, 24, 25, 26]]

matrix3 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
matrix4 = [[11, 12, 13], [15, 16, 17], [19, 20, 21]]

matrix5 = [[i for i in range(1,17)] for x in range(16)]

matrix6 = [[1]*16 for i in range(16)]

matrix7 = [[1, 2], [1, 2]]
matrix8 = [[-2, -2], [-2, -2]]

print(problem1.get_machine_precision())
print(problem2.get_nonassociative_numbers())
print(problem3.strassen_multiplication(matrix1, matrix2))
print(Matrix(matrix1) @ Matrix(matrix2))
# TODO make it work
print(Matrix(matrix3) @ Matrix(matrix4))
print(np.dot(matrix3, matrix4))

print(Matrix(matrix7) @ Matrix(matrix8))
print(Matrix(matrix7) * Matrix(matrix8))
print(np.dot(matrix7, matrix8))

print(io.read_matrix("matrix1.test"))