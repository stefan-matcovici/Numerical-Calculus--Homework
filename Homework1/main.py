import problem1
import problem2
import problem3
from Matrix import Matrix

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22], [23, 24, 25, 26]]

matrix3 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
matrix4 = [[11, 12, 13], [15, 16, 17], [19, 20, 21]]

print(problem1.get_machine_precision())
print(problem2.get_nonassociative_numbers())
print(problem3.strassen_multiplication(matrix1, matrix2))
print(Matrix(matrix1) @ Matrix(matrix2))
print(Matrix(matrix3) @ Matrix(matrix4))