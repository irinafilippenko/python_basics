import argparse


def write_bakery(sum):
    with open('bakery.csv', 'a', encoding='utf-8') as bakery:
        bakery.write(f'{sum}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add sum to bakery.csv')
    parser.add_argument('sum', type=float, help='Input sum')
    args = parser.parse_args()
    write_bakery(args.sum)
