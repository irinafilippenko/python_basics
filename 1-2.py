cube_list = []
cube_list_plus = []
sum_all_1 = 0
sum_all_2 = 0
sum_all_3 = 0

for number in range(1, 1000):
    if number % 2 != 0:
        cube_list.append(number ** 3)

for number in cube_list:
    sum_number = 0
    change_number = number
    while change_number:
        part_number = change_number % 10
        change_number //= 10
        sum_number += part_number
    if sum_number % 7 == 0:
        sum_all_1 += number

print('Задание 2.')
print(f'Сумма чисел, сумма цифр которых делится нацело на 7: {sum_all_1}')

cube_list_plus = cube_list.copy()
# копия списка через append (copy не было на уроке)
# for number in cube_list:
#     cube_list_plus.append(number)

for n in range(len(cube_list_plus)):
    cube_list_plus[n] += 17

for number in cube_list_plus:
    change_number = number
    sum_number = 0
    while change_number:
        part_number = change_number % 10
        change_number //= 10
        sum_number += part_number
    if sum_number % 7 == 0:
        sum_all_2 += number

print(f'К каждому элементу добавить 17 и заново вычислить сумму: {sum_all_2}')

for number in cube_list:
    number += 17
    change_number = number
    sum_number = 0
    while change_number:
        part_number = change_number % 10
        change_number //= 10
        sum_number += part_number
    if sum_number % 7 == 0:
        sum_all_3 += number

print(f'Без создания нового списка: {sum_all_3}')
