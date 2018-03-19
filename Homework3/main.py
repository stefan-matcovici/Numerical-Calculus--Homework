from Homework3.SparseMatrix import SparseMatrix
from utils import io

if __name__ == "__main__":
    file_matrix1 = io.read_system("../test/a.txt")
    a = SparseMatrix(file_matrix1[0], file_matrix1[2])
    a.store(file_matrix1[1])

    file_matrix2 = io.read_system("../test/b.txt")
    b = SparseMatrix(file_matrix2[0], file_matrix2[2])
    b.store(file_matrix2[1])

    file_matrix3 = io.read_system("../test/aplusb.txt")
    aplusb = SparseMatrix(file_matrix3[0], file_matrix3[2])
    aplusb.store(file_matrix3[1])

    result = a + b


    # a.print()
    # result.print()
    print(result.compare(aplusb))

