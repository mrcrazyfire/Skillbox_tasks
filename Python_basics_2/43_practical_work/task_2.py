"""
Задача 2. Замедление кода
В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
"""


import time
from functools import wraps
from typing import Callable, Any


def slowing_code(func: Callable) -> Callable:
    """Декоратор, который замедляет выполнение декорируемой функции"""
    @wraps(func)
    def wrapper():
        time.sleep(3)
        return func()
    return wrapper


@slowing_code
def test():
    """Функция, которая выводит на экран слово Hello!"""
    print("Hello!")


test()