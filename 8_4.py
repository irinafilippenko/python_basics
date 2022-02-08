from functools import wraps


def val_checker(is_positive):
    def _val_checker(func):
        @wraps(func)
        def wrapper(x):
            if (is_positive(x)):
                result = func(x)
                print(f'{func.__name__} ({x}: {type(func(x))})')
                return result
            else:
                raise ValueError(f'wrong val {x}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == "__main__":
    print(calc_cube(-63))
