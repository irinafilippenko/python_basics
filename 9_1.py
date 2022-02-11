from time import sleep
from turtle import pencolor, fillcolor, begin_fill, circle, end_fill


class TrafficLight:
    def __init__(self):
        self.__color = {'red': [7, 41], 'yellow': [2, 43], 'green': [7, 42]}

    def running(self):
        for color in self.__color:
            # print(f'\033[30m\033[{self.__color[color][1]}m{color:^30}')
            # sleep(self.__color[color][0])
            pencolor('black')
            fillcolor(color)
            begin_fill()
            circle(120)
            end_fill()
            sleep(self.__color[color][0])


if __name__ == "__main__":
    tl = TrafficLight()
    tl.running()
