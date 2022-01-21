def num_translate_adv(num_eng):
    dict_numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                    'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if num_eng.istitle():
        return dict_numbers.get(num_eng.lower()).title()
    else:
        return dict_numbers.get(num_eng)


print('Задание 2.\n')
print(num_translate_adv(input('Введите число от 0 до 10 (англ.): ')))
