from re import compile


def date_from_logs(name_file_logs):
    with open(name_file_logs, 'r') as read_file, open('date_from_logs.txt', 'w+') as write_file:
        REC_LOG = compile(
            r'((?:\d{1,3}[./-]){3}\d{1,3}).{5}(?:\[(.+)\])\s"([A-Z]{3,})\s([/\w+]{1,}).+"\s(\d{1,})\s(\d{1,})')
        for line in read_file:
            line_log = REC_LOG.findall(line)
            print(*line_log, file=write_file)


if __name__ == '__main__':
    date_from_logs('nginx_logs.txt')
