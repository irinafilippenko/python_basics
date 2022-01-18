prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
all_prices = ''

for price in prices:
    if str(price).find('.') == -1:
        ruble = str(price)
        penny = '0'
    else:
        ruble, penny = str(price).split('.')
    add_price = f' {ruble} руб. {penny:0<2} коп.'
    # add_price = f' {ruble} руб. {penny.ljust(2, "0")} коп.'
    all_prices = ','.join([all_prices, add_price])

print('Задание 5.\n')
print('5. A.')
print(all_prices.lstrip(', '))

print('\n5. B.')
print(f'Список цен: {prices}')
print(f'Id списка цен до сортировки: {id(prices)}')
print(f'\nСортировка по возрастанию: {sorted(prices)}')
print(f'Id списка цен после сортировки: {id(prices)}')

prices_sort_desc = sorted(prices, reverse=True)
print('\n5. C.')
print(f'Новый список, отсортированный по убыванию: {prices_sort_desc}')

print('\n5. D.')
print(f'Цены пяти самых дорогих товаров: {sorted(prices)[-5:]}')