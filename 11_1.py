from datetime import datetime


class Date:
    def __init__(self, date):
        self.date = date
        self.date_to_int(date)

    @classmethod
    def date_to_int(cls, date):
        try:
            day, month, year = map(int, date.split("-"))
        except ValueError:
            print('Неверный формат числа (тип).')
        else:
            try:
                return cls.valid_date(day, month, year)
            except ValueError:
                print('Неверный формат даты.')

    @staticmethod
    def valid_date(day, month, year):
        return datetime.strptime(f'{day}-{month}-{year}', '%d-%m-%Y')


if __name__ == "__main__":
    date1 = Date('01-feb-2001')
    date2 = Date('01-19-2001')
    date3 = Date('01-12-2001')
