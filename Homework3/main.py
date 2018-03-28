from SparseMatrix import SparseMatrix
from utils import io
import numpy as np

if __name__ == "__main__":
    # addition
    file_matrix1 = io.read_system("../test/a.txt")
    a = SparseMatrix(*file_matrix1)
    a.verify()

    file_matrix2 = io.read_system("../test/b.txt")
    b = SparseMatrix(*file_matrix2)
    b.verify()

    file_matrix3 = io.read_system("../test/aplusb.txt")
    aplusb = SparseMatrix(*file_matrix3)

    result = a + b

    print(result - aplusb)
    print(result == aplusb)

    # multiplication
    file_matrix2 = io.read_system("../test/b.txt")
    b = SparseMatrix(*file_matrix2, True)

    file_matrix3 = io.read_system("../test/aorib.txt")
    aorib = SparseMatrix(*file_matrix3)

    result = a * b

    print(result - aorib)
    print(result == aorib)

    # vector multiplication

    v = [i for i in range(2018, 0, -1)]
    result = a.multiply_vector(v)

    print(np.linalg.norm([x - y for x, y in zip(result, a.b)]))

    file_matrix2 = io.read_system("../test/b.txt")
    b = SparseMatrix(*file_matrix2)

    result = b.multiply_vector(v)
    print(np.linalg.norm([x - y for x, y in zip(result, b.b)]))
