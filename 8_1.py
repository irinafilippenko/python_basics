from re import match


def email_parse(email):
    try:
        test_email = match('(([A-Za-z0-9]+[.\-_])*[A-Za-z0-9]+)@([A-Za-z0-9-]+(\.[A-Z|a-z]{1,})+)', email)
        print({test_email.group(1): test_email.group(3)})
    except:
        raise ValueError(f'wrong email: {email}')


if __name__ == "__main__":
    email_parse(input('Введите email: '))
