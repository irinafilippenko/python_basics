def get_odd_numbers(get_number):
    return [number for number in range(1, get_number + 1, 2)]


if __name__ == '__main__':
    for n in get_odd_numbers(int(input('Введите число: '))):
        print(n, end=' ')

    # список без функции, с if
    print(*[number for number in range(1, int(input('Введите число: ')) + 1) if number % 2 != 0])