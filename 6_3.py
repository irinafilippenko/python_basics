from itertools import zip_longest
import json


def dict_users_hobbyes(users_file, hobby_file, json_file):
    with open(users_file, 'r', encoding='utf-8') as read_users, open(hobby_file, 'r', encoding='utf-8') as read_hobby:
        lines_users = [line.strip().replace(',', ' ') for line in read_users]
        # или с помощью readlines
        # lines_users = list(map(str.strip, read_users.readlines()))
        lines_hobby = [line.strip() for line in read_hobby]
        # lines_hobby = list(map(str.strip, read_hobby.readlines()))
        if len(lines_users) < len(lines_hobby):
            exit(1)
        users_hobbyes = {user: hobby for user, hobby in zip_longest(lines_users, lines_hobby)}

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(users_hobbyes, f)

    with open(json_file, 'r', encoding='utf-8') as f:
        export = json.load(f)
    print(export)


if __name__ == '__main__':
    dict_users_hobbyes('users.csv', 'hobby.csv', 'users_hobbyes.json')
