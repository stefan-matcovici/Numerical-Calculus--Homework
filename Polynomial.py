import random
from math import sqrt


class Polynomial:
    def __init__(self, file_name):
        with open(file_name) as file:
            file_content = file.readlines()

            self.n = int(file_content[0])
            self.coefficients = [int(coefficient) for coefficient in file_content[1].split(" ")]

            assert len(self.coefficients) == self.n + 1

            self.r = (abs(self.coefficients[0]) + max([abs(coefficient) for coefficient in self.coefficients])) / abs(
                self.coefficients[0])

    # def __init__(self, n, coefficients):
    #     self.n = n
    #     self.coefficients = coefficients
    #
    #     assert len(self.coefficients) == self.n + 1
    #
    #     self.r = (abs(self.coefficients[0]) + max([abs(coefficient) for coefficient in self.coefficients])) / abs(
    #         self.coefficients[0])

    def approximate_roots(self, step_length, retries, kmax, epsilon, f):
        roots = set()

        nr_steps = int(2 * self.r / step_length)

        for step in range(nr_steps):
            for retry in range(retries):
                xk = random.uniform(-self.r + step * step_length, -self.r + step * step_length + step_length)
                xk_1 = random.uniform(-self.r + step * step_length, -self.r + step * step_length + step_length)
                xk_2 = random.uniform(-self.r + step * step_length, -self.r + step * step_length + step_length)

                for k in range(kmax):
                    a, b, c = self.__get_abc__(xk, xk_1, xk_2, f)

                    if b * b - 4 * a * c > 0:
                        new_xk, delta, maxi = self.__get_next_xk__(a, b, c, xk)

                        if abs(maxi) < epsilon:
                            break

                        xk_2 = xk_1
                        xk_1 = xk
                        xk = new_xk

                        if abs(delta) < epsilon or abs(delta) > 10 ** 8:
                            break
                    else:
                        delta = 100000

                if abs(delta) < epsilon:
                    roots.add('%.3f' % xk)

        return roots

    def get_local_minimums(self, interval):
        pass

    def get_derivative_value1(self, value, h=1):
        return (3 * self.get_result_horner(value) -
                4 * self.get_result_horner(value - h) +
                self.get_result_horner(value - 2 * h)
                ) / 2 * h

    def get_derivative_value2(self, value, h=1):
        return (-self.get_result_horner(value + 2 * h)
                + 8 * self.get_result_horner(value + h)
                - 8 * self.get_result_horner(value - h)
                + self.get_result_horner(value - 2 * h)
                ) / 12 * h

    def get_second_derivative_value(self, value, h=1):
        return (
                   -self.get_result_horner(value + 2 * h)
                   + 16 * self.get_result_horner(value + h)
                   - 30 * self.get_result_horner(value)
                   + 16 * self.get_result_horner(value - h)
                   - self.get_result_horner(value - 2 * h)
               ) / 12 * h

    def get_result(self, value):
        result = 0
        for i in range(self.n + 1):
            result += self.coefficients[i] * pow(value, self.n - i)

        return result

    def get_result_horner(self, value):
        bi = self.coefficients[0]
        for i in range(1, self.n + 1):
            bi = self.coefficients[i] + bi * value

        return bi

    def __get_abc__(self, xk, xk_1, xk_2, f):
        h0 = xk_1 - xk_2
        h1 = xk - xk_1

        delta_0 = (f(xk_1) - f(xk_2)) / h0
        delta_1 = (f(xk) - f(xk_1)) / h1

        a = (delta_1 - delta_0) / (h1 + h0)
        b = a * h1 + delta_1
        c = f(xk)

        return a, b, c

    def __get_next_xk__(self, a, b, c, xk):
        aux = sqrt(b * b - 4 * a * c)

        if aux == 0:
            return 0, 0, 0

        delta = 2 * c / max(b + aux, b - aux)

        return xk - delta, delta, max(b + aux, b - aux)
