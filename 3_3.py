def thesarus(*args):
    dict_names = {}
    for name in args:
        dict_names.setdefault(name[0], list(filter(lambda n: n.startswith(name[0]), args)))
    return dict_names


print('Задание 3.\n')
print(thesarus('Иван', 'Мария', 'Петр', 'Илья'))
