from random import shuffle, randint, choice


def get_jokes(num=1, no_repeat=True):
    """
    Returns num jokes formed from three random words
    :param num: number of jokes
    :param no_repeat: flag to allow word repetitions
    :return: list of num jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    for i in range(num, 0, -1):
        if no_repeat:
            jokes.append(
                f'{nouns.pop(randint(0, i - 1))} {adverbs.pop(randint(0, i - 1))} {adjectives.pop(randint(0, i - 1))}')
        else:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return jokes


print('Задание 5.\n')
print(get_jokes(5, no_repeat=True))


# def get_jokes_2(num=1):
#     nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#     adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#     adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#     shuffle(nouns)
#     shuffle(adverbs)
#     shuffle(adjectives)
#     jokes = list(zip(nouns, adverbs, adjectives))
#     for i in range(num):
#         print(f'{jokes[i][0]} {jokes[i][1]} {jokes[i][2]}')


# print(get_jokes_2(5))
