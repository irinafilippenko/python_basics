class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        print(
            f'Для покрытия дороги ({self._length} м х {self._width} м) потребуется {self._length * self._width * 25 * 5 / 1000:,.2f} т. асфальта')


if __name__ == "__main__":
    r = Road(20, 5000)
    r.calculate_mass()
