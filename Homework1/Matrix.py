import math
import copy


class Matrix:
    def __init__(self, matrix):
        self.size = len(matrix)
        self.data = copy.deepcopy(matrix)
        self.unpad_size = self.size

    def __add__(self, other):
        """
        Sums two matrices

        :param other: matrix to add
        :raise ValueError if the 2 matrixes don't have the same dimensions
        :return new matrix which is the sum of self and other
        """
        if other.size != self.size:
            raise ValueError("Invalid matrix to add" + str(other) + str(self))
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.size)] for i in range(self.size)])

    def __sub__(self, other):
        """
        Sums two matrixes

        :param other: matrix to subtract
        :raise ValueError if the 2 matrices don't have the same dimensions
        :return new matrix which is the difference of self and other
        """
        if other.size != self.size:
            raise ValueError("Invalid matrix to sub")
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.size)] for i in range(self.size)])

    def strassen_multiply(self, other, order):
        """
        Multiplies two matrices using strassen algorithm

        :param other: matrix to multiply with
        :param order: the order of matrix from where to perform simple multiplication
        :return new matrix which is the product of self and other
        """
        if self.size == 2 ** order:
            return self * other

        self.pad()
        other.pad()

        half = self.size // 2

        a = self.slice(half)
        b = other.slice(half)

        p1 = (a[0][0] + a[1][1]).strassen_multiply(b[0][0] + b[1][1], order)
        p2 = (a[1][0] + a[1][1]).strassen_multiply(b[0][0], order)
        p3 = a[0][0].strassen_multiply(b[0][1] - b[1][1], order)
        p4 = a[1][1].strassen_multiply(b[1][0] - b[0][0], order)
        p5 = (a[0][0] + a[0][1]).strassen_multiply(b[1][1], order)
        p6 = (a[1][0] - a[0][0]).strassen_multiply(b[0][0] + b[0][1], order)
        p7 = (a[0][1] - a[1][1]).strassen_multiply(b[1][0] + b[1][1], order)

        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 + p3 - p2 + p6

        self.unpad()
        other.unpad()

        return self.recompose(c11, c12, c21, c22)

    def __len__(self):
        return self.size

    def __mul__(self, other):
        """
        Multiplies two matrices using classic algorithm

        :param other: matrix to multiply with
        :return new matrix which is the product of self and other
        """
        r = []
        m = []
        for i in range(self.size):
            for j in range(self.size):
                sums = 0
                for k in range(self.size):
                    sums = sums + (self.data[i][k] * other.data[k][j])
                r.append(sums)
            m.append(r)
            r = []
        return Matrix(m)

    def __str__(self):
        result = ""
        for i in range(self.size):
            for j in range(self.size):
                result += str(self.data[i][j]) + " "
            result += "\n"
        return result

    def slice(self, size):
        """
        Slices self in four matrices

        :param size: place of slicing
        :return 2x2 matrix containing Matrix objects
        """
        return [[Matrix([x[:size] for x in self.data[:size]]),
                 Matrix([x[size:] for x in self.data[:size]])],
                [Matrix([x[:size] for x in self.data[size:]]),
                 Matrix([x[size:] for x in self.data[size:]])]]

    def recompose(self, c11, c12, c21, c22):
        """
            Opposite of slicing, forms a new matrix from 4 matrices

            :param c11, c12, c21, c22: parts of the desired matrix
            :return new matrix
            """
        result = Matrix(self.data)
        size = len(c11)
        for i in range(size):
            for j in range(size):
                c11.data[i].append(c12.data[i][j])
                c21.data[i].append(c22.data[i][j])

        for i in range(size):
            c11.data.append(c21.data[i])

        result.data = c11.data
        return result

    def next_power_of_2(self):
        return 1 if self.size == 0 else 2 ** math.ceil(math.log2(self.size))

    def pad(self):
        """
        Pads self with zeros in order to become a quadratic matrix of order a power of two
        """
        self.size = self.next_power_of_2()
        pad_blank_line1 = [0] * self.size
        pad_blank_line2 = [0] * (self.size - self.unpad_size)

        for i in range(self.unpad_size):
            self.data[i][self.unpad_size:] = pad_blank_line2

        for i in range(self.size - self.unpad_size):
            self.data.append(pad_blank_line1)

    def unpad(self):
        """
        Eliminates zeros added when padded was done in order to extract the result
        """
        for i in range(self.size):
            self.data[i] = self.data[i][:self.unpad_size]

        self.size = self.unpad_size
        self.data = self.data[:self.size]
