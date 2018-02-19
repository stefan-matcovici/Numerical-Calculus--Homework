def add_matrix(matrix1, matrix2):
    size = len(matrix1)
    return [[matrix1[i][j] + matrix2[i][j] for j in range(size)] for i in range(size)]


def simple_multiplication(matrix1, matrix2):
    r = []
    m = []
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            sums = 0
            for k in range(len(matrix1)):
                sums = sums + (matrix1[i][k] * matrix2[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m


def sub_matrix(matrix1, matrix2):
    size = len(matrix1)
    return [[matrix1[i][j] - matrix2[i][j] for j in range(size)] for i in range(size)]


def recompose_matrix(c11, c12, c21, c22):
    size = len(c11)
    print(c11, c12, c21, c22)


def strassen_multiplication(matrix1, matrix2):
    half = len(matrix1) // 2
    if half == 1:
        return simple_multiplication(matrix1, matrix2)

    a = slice_matrix(half, matrix1)
    b = slice_matrix(half, matrix2)

    p1 = strassen_multiplication(add_matrix(a[0][0], a[1][1]), add_matrix(b[0][0], b[1][1]))
    p2 = strassen_multiplication(add_matrix(a[1][0], a[1][1]), b[0][0])
    p3 = strassen_multiplication(a[0][0], sub_matrix(a[0][1], a[1][1]))
    p4 = strassen_multiplication(a[1][1], sub_matrix(a[1][0], a[0][0]))
    p5 = strassen_multiplication(add_matrix(a[0][0], a[0][1]), b[1][1])
    p6 = strassen_multiplication(sub_matrix(a[1][0], a[0][0]), add_matrix(b[0][0], b[0][1]))
    p7 = strassen_multiplication(sub_matrix(a[0][1], a[1][1]), add_matrix(b[1][0], b[1][1]))

    c11 = sub_matrix(add_matrix(p1, p4), add_matrix(p5, p7))
    c12 = add_matrix(p3, p5)
    c21 = add_matrix(p2, p4)
    c22 = sub_matrix(add_matrix(p1, p3), add_matrix(p2, p6))

    return recompose_matrix(c11, c12, c21, c22)


def slice_matrix(size, matrix):
    return [[[x[:size] for x in matrix[:size]],
             [x[size:] for x in matrix[:size]]],
            [[x[:size] for x in matrix[size:]],
             [x[size:] for x in matrix[size:]]]]
