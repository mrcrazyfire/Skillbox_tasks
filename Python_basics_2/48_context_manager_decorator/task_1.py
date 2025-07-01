import time
from contextlib import contextmanager
from collections.abc import Iterator


"""
Задача 1. Таймер
Реализуйте функцию (не класс) timer в качестве контекст-менеджера:
функция должна работать с оператором with и замерять время работы вложенного кода.
"""

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    finally:
        print(time.time() - start)



