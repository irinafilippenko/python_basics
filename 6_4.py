import argparse
from os import walk, path, stat


def get_size_files(dir):
    if path.isdir(dir):
        dict_size_files = {}
        for root, folders, files in walk(dir):
            for file in files:
                max_size = 10 ** len(str(stat(path.join(root, file)).st_size))
                if max_size in dict_size_files:
                    dict_size_files[max_size] += 1
                else:
                    dict_size_files[max_size] = 1
        print(dict(sorted(dict_size_files.items(), key=lambda item: item[0])))
    else:
        print(f'Каталог {dir} не существует.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Getting statistics from file sizes.')
    parser.add_argument('dir', type=str, help='directory')
    args = parser.parse_args()
    get_size_files(args.dir)
