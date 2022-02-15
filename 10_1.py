from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(''.join(f'{x:>6}' for x in row) for row in self.matrix)

    def __add__(self, other):
        return Matrix(
            [map(sum, zip_longest(*i, fillvalue=0)) for i in zip_longest(self.matrix, other.matrix, fillvalue=[0])])


if __name__ == "__main__":
    matrix_1 = Matrix([[1, 2, 3], [1, 2, 3], [9, 4]])
    matrix_2 = Matrix([[51, 48, 3], [7, 158, -83, 104]])
    print(matrix_1 + matrix_2)
