import numpy as np

from utils import io

from SparseMatrix import SparseMatrix

if __name__ == "__main__":
    file_matrix1 = io.read_system("../test/m_rar_2018_1.txt")
    matrix = SparseMatrix(*file_matrix1)
    matrix.verify()

    solution = matrix.solve_Gauss_Sidel(0.0001, 1)

    print(solution)

    print(np.linalg.norm(matrix.multiply_vector(solution) - matrix.b))