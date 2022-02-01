def date_from_logs(name_file_logs):
    with open(name_file_logs, 'r') as read_file:
        for line in read_file:
            line_log = line.split()
            print(f'{(line_log[0], line_log[5][1:], line_log[6])}')


if __name__ == '__main__':
    date_from_logs('nginx_logs.txt')
