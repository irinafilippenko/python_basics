words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for n in range(len(words)):
    if not words[n].isalpha() and words[n].find('.') == -1:
        if words[n][0].isdigit():
            plus_minus = ''
            number = words[n]
        else:
            plus_minus = words[n][0]
            number = words[n][1:]
        words[n] = ''.join(['"', plus_minus, number.zfill(2), '"'])
        # words[n] = ''.join(['"', plus_minus, f'{number:0>2}', '"'])

print('Задание 2.\n')
print(' '.join(words))