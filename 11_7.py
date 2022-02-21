class ComplexNumber:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return f'{self.number1} + {self.number2} * i'

    def __add__(self, other):
        return ComplexNumber(self.number1 + other.number1, self.number2 + other.number2)

    def __mul__(self, other):
        return ComplexNumber(self.number1 * other.number1 - self.number2 * other.number2,
                             self.number1 * other.number2 + other.number1 * self.number2)


if __name__ == "__main__":
    cn_1 = ComplexNumber(6, 17)
    cn_2 = ComplexNumber(9, 45)
    print(cn_1)
    print(cn_2)
    print(cn_1 + cn_2)
    print(cn_1 * cn_2)
