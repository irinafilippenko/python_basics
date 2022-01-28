def get_odd_numbers(get_number):
    for number in range(1, get_number + 1, 2):
        yield number


if __name__ == '__main__':
    for n in get_odd_numbers(int(input('Введите число: '))):
        print(n, end=' ')
