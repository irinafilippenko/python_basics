from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.calculate_cloth + other.calculate_cloth

    @property
    @abstractmethod
    def calculate_cloth(self):
        '''Подсчет расхода ткани'''


class Coat(Dress):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def calculate_cloth(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Dress):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def calculate_cloth(self):
        return 2 * self.height + 0.3


if __name__ == "__main__":
    c = Coat('элегантное', 46)
    s = Suit('деловой', 1.82)
    print(c.calculate_cloth)
    print(s.calculate_cloth)
    # print(c.calculate_cloth+s.calculate_cloth)
    print(s + c)
