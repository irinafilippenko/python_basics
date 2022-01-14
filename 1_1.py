duration = int(input('Введите промежуток времени в секундах: '))
change_duration = duration

message = f'{change_duration % 60} сек'
change_duration = change_duration // 60
if change_duration:
    message = f'{change_duration % 60} мин {message}'
    change_duration = change_duration // 60
    if change_duration:
        message = f'{change_duration % 24} час {message}'
        change_duration = change_duration // 24
        if change_duration:
            message = f'{change_duration} дн {message}'

print(f'Промежуток времени {duration} секунд равен: {message}')
