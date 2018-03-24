from SparseMatrix import SparseMatrix
from utils import io

if __name__ == "__main__":
    file_matrix1 = io.read_system("../test/a.txt")
    a = SparseMatrix(*file_matrix1)

    file_matrix2 = io.read_system("../test/b.txt")
    b = SparseMatrix(*file_matrix2)

    file_matrix3 = io.read_system("../test/aplusb.txt")
    aplusb = SparseMatrix(*file_matrix3)

    result = a + b

    print(result - aplusb)

    file_matrix1 = io.read_system("../test/a.txt")
    a = SparseMatrix(*file_matrix1)

    file_matrix2 = io.read_system("../test/b.txt")
    b = SparseMatrix(*file_matrix2, True)

    file_matrix3 = io.read_system("../test/aorib.txt")
    aorib = SparseMatrix(*file_matrix3)

    result = a * b

    print(result - aorib)


