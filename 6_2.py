from collections import Counter


def date_from_logs(name_file_logs):
    with open(name_file_logs, 'r') as read_file, open('date_from_logs.txt', 'w+') as write_file:
        for line in read_file:
            line_log = line.split()
            write_file.write(f'{(line_log[0], line_log[5][1:], line_log[6])}\n')
        write_file.seek(0)
        print(Counter([line.split(',')[0][2:-1] for line in write_file]).most_common(1))


if __name__ == '__main__':
    date_from_logs('nginx_logs.txt')
