class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":
    try:
        divident = float(input('Введите первое число (делимое):'))
        divider = float(input('Введите второе число (делитель):'))
    except ValueError:
        print('Неверный формат числа.')
    try:
        if (divider == 0):
            raise ZeroDiv('Нельзя делить на ноль.')
    except ZeroDiv as err:
        print(err)
    else:
        print(f'Результат деления: {divident / divider:,.2f}')
