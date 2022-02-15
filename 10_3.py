class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return self.num_cell + other.num_cell

    def __sub__(self, other):
        if (self.num_cell > other.num_cell):
            return self.num_cell - other.num_cell
        else:
            print('Разность <= 0')

    def __mul__(self, other):
        return self.num_cell * other.num_cell

    def __floordiv__(self, other):
        try:
            return self.num_cell // other.num_cell
        except ZeroDivisionError:
            print('Нельзя делить на ноль.')

    def __truediv__(self, other):
        try:
            return round(self.num_cell / other.num_cell, 2)
        except ZeroDivisionError:
            print('Нельзя делить на ноль.')

    def make_order(self, num_row):
        print('\n'.join(''.join(chr(128521) for _ in range(num_row)) for _ in range(self.num_cell // num_row)))
        if self.num_cell % num_row != 0:
            print(chr(128521) * (self.num_cell % num_row))


if __name__ == "__main__":
    cell_1 = Cell(1587)
    cell_2 = Cell(561)
    cell_3 = Cell(17)
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 * cell_2)
    print(cell_1 // cell_2)
    print(cell_1 / cell_2)
    cell_3.make_order(4)
