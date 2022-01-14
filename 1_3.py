print('Задание 3.')
print('Склонение слова «процент» во фразе «N процентов» (от 1 до 100):')

for procent in range(1, 100):
    procent_remainder = procent % 100
    if (procent_remainder > 10 and procent_remainder < 20):
        print(f'{procent} процентов')
    elif (procent_remainder % 10 == 1):
        print(f'{procent} процент')
    elif (procent_remainder % 10 > 1 and procent_remainder % 10 < 5):
        print(f'{procent} процента')
    else:
        print(f'{procent} процентов')
