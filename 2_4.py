employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

print('Задание 4.\n')

for employer in employees:
    name = employer.split()[-1].title()
    # name = employer.split()[-1].capitalize()
    print(f'Привет коллега, {name}!')
