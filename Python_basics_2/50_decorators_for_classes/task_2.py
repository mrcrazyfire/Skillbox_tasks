import datetime
from functools import wraps


def logged(func):
    def wrapped(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.datetime.now())
        return func(*args, **kwargs)

    return wrapped

def decorator(cls):
    for method in dir(cls):
        if not method.startswith("__"):
            a = getattr(cls, method)
            if hasattr(a, '__call__'):
                decorated_a = logged(a)
                setattr(cls, method, decorated_a)
    return cls




@decorator
class MyClass:
    def __init__(self, number):
        self.number = number

    def numbers_sum(self):
        """Функция возвращает сумму чисел от 1 до N."""
        return sum(num for num in range(1, self.number + 1))

    def numbers_milt(self):
        """Функция возвращает произведение чисел от 1 до N."""
        res = 1
        for num in range(1, self.number + 1):
            res *= num
        return res


my_class = MyClass(500)

my_class.numbers_sum()
my_class.numbers_milt()