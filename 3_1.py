def num_translate(num_eng):
    dict_numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                    'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return dict_numbers.get(num_eng)


print('Задание 1.\n')
print(num_translate(input('Введите число от 0 до 10 (англ.): ')))
