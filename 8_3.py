from functools import wraps
from itertools import chain


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for x in chain((x for x in args), (val for key, val in kwargs.items())):
            print(f'{func.__name__} ({x}: {type(func(x))})', end=', ')
        return result

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    return (x ** 3 for x in chain((x for x in args), (val for key, val in kwargs.items())))


if __name__ == "__main__":
    print(*calc_cube(5, 9, 4, number=7))
