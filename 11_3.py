class IsNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":
    numbers = []
    while True:
        value = input('Введите элемент списка: ')
        if value == 'stop':
            break
        try:
            if not value.replace('.', '').replace('-', '').isdigit():
                raise IsNumber('Вы ввели не число.')
        except IsNumber as err:
            print(err)
        else:
            numbers.append(value)

    print(numbers)
