src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def get_unique_numbers(numbers):
    result = []
    unique_numbers = set(numbers)
    for number in numbers:
        if number in unique_numbers and numbers.count(number) == 1:
            result.append(number)
            unique_numbers.discard(number)
    return result


# реализация по методичке
# def get_unique_numbers(numbers):
#     result = []
#     tmp = []
#     for el in numbers:
#         if el not in tmp:
#             result.append(el)
#         elif el in result:
#             result.remove(el)
#         tmp.append(el)
#     return result


print(*src)
print(*get_unique_numbers(src))
