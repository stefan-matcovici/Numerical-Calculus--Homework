import numpy as np
import copy

class SparseMatrix:
    def __init__(self, size, b):
        self.size = size
        self.b = b
        self.data = [[] for i in range(self.size)]

    def store(self, a):
        for line in a:
            self.append_element(line[1], [line[0], line[2]])

    def insert_element(self, line, element):
        self.data[line].insert(self.get_index_of_insertion(self.data[line], element[1]), element)

    def append_element(self, line, element):
        pos = self.search_index(self.data[line], element[1])
        if pos != -1:
            self.data[line][pos][0] += element[0]
        else:
            self.data[line].insert(self.get_index_of_insertion(self.data[line], element[1]), copy.deepcopy(element))

    def get_index_of_insertion(self, line, column):
        size = len(line)

        if size == 0:
            return 0

        left = 0
        right = size - 1
        mid = 0
        while left < right:
            mid = (left + right) // 2
            if line[mid][1] == column:
                return mid + 1

            if column < line[mid][1]:
                right = mid - 1
            else:
                left = mid + 1

        return left + 1 if column > line[left][1] else left

    def __add__(self, other):
        result = SparseMatrix(self.size, [0 for i in range(self.size)])

        result.b = [x + y for x, y in zip(self.b, other.b)]

        for i in range(len(self.data)):
            for element in self.data[i]:
                result.append_element(i, element)

        for i in range(len(other.data)):
            for element in other.data[i]:
                result.append_element(i, element)

        return result

    def search_index(self, line, column):
        size = len(line)

        left = 0
        right = size - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if line[mid][1] == column:
                return mid

            if column < line[mid][1]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def compare(self, other):
        diff = np.linalg.norm([x - y for x, y in zip(self.b, other.b)])

        for i in range(len(self.data)):
            for element in self.data[i]:
                pos = other.search_index(other.data[i], element[1])
                if pos != -1:
                    diff += np.linalg.norm(element[0]-other.data[i][pos][0])
                else:
                    print("error")
                    diff += np.linalg.norm(element[0])

        for i in range(len(other.data)):
            for element in other.data[i]:
                pos = self.search_index(self.data[i], element[1])
                if pos != -1:
                    diff += np.linalg.norm(element[0]-self.data[i][pos][0])
                else:
                    print("error")
                    diff += np.linalg.norm(element[0])

        return diff

    def print(self):
        print(self.size)
        print()

        for i in range(len(self.data)):
            for element in self.data[i]:
                print((element[0], i, element[1]))