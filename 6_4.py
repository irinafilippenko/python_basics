from itertools import zip_longest


def dict_users_hobbyes(users_file, hobby_file, txt_file):
    with open(users_file, 'r', encoding='utf-8') as read_users, open(hobby_file, 'r',
                                                                     encoding='utf-8') as read_hobby, open(txt_file,
                                                                                                           'w',
                                                                                                           encoding='utf-8') as write_file:
        lines_users = [line.strip().replace(',', ' ') for line in read_users]
        lines_hobby = [line.strip() for line in read_hobby]
        if len(lines_users) < len(lines_hobby):
            exit(1)
        for user, hobby in zip_longest(lines_users, lines_hobby):
            write_file.write(f'{user}: {hobby}\n')


if __name__ == '__main__':
    dict_users_hobbyes('users.csv', 'hobby.csv', 'users_hobby.txt')
