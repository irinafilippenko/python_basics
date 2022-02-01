import argparse
from itertools import islice


def read_bakery(index_1, index_2):
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        index_1, index_2 = (i - 1 if i else i for i in (index_1, index_2))
        print(*islice(bakery, index_1, index_2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read sum from bakery.csv')
    parser.add_argument('index_1', type=int, default=None, nargs='?', help='First index')
    parser.add_argument('index_2', type=int, default=None, nargs='?', help='Second index')
    args = parser.parse_args()
    read_bakery(args.index_1, args.index_2)
