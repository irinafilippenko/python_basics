class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул на {direction}.')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется на скорости {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил допустимую скорость в 60 км/ч (ваша скорость: {self.speed} км/ч).')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил допустимую скорость в 40 км/ч (ваша скорость: {self.speed} км/ч).')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == "__main__":
    tc = TownCar(70, 'белый', 'honda', False)
    # print(tc.speed, tc.color, tc.name, tc.is_police)
    tc.show_speed()
    sc = SportCar(200, 'красный', 'ferrari', False)
    # print(sc.speed, sc.color, sc.name, sc.is_police)
    sc.show_speed()
    wc = WorkCar(50, 'синий', 'lada', False)
    # print(wc.speed, wc.color, wc.name, wc.is_police)
    wc.show_speed()
    pc = PoliceCar(90, 'белый', 'ford')
    # print(pc.speed, pc.color, pc.name, pc.is_police)
    pc.show_speed()
