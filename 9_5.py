class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет записку.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} набрасывает эскиз.')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} пишет на информационной доске.')


if __name__ == "__main__":
    p1 = Pen('Капиллярная ручка')
    p1.draw()
    p2 = Pencil('Черный карандаш')
    p2.draw()
    h = Handle('Маркер')
    h.draw()
