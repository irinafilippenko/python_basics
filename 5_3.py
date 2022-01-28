from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# klasses = ['9А', '7В', '9Б', '9В']


def gen_klass_tutor():
    for tutor, klass in zip_longest(tutors, klasses):
        if tutor:
            yield tutor, klass
    # без yield
    # return ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor)


if __name__ == '__main__':
    print(type(gen_klass_tutor()))
    for n in gen_klass_tutor():
        print(n, end=' ')
    # распаковка * без for
    # print(*gen_klass_tutor())
