class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname} - {self.position}')

    def get_total_income(self):
        print(f'Получил доход: {self._income["wage"] + self._income["bonus"]:,.2f}')


if __name__ == "__main__":
    p = Position('Сергей', 'Сапронов', 'продавец', 30000, 15000)
    p.get_full_name()
    p.get_total_income()
