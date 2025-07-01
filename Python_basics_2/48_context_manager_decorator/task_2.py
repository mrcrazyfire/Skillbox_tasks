import os
from contextlib import contextmanager
from collections.abc import Iterator


"""
Задача 2. Директории
Реализуйте функцию in_dir, которая принимает в качестве аргумента путь
и временно меняет текущую рабочую директорию на новую. Функция должна быть контекст-менеджером.
Также реализуйте обработку ошибок (например, если такого пути не существует).
Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию.

Пример основного кода:
with in_dir('C:\\'):
    print(os.listdir())
Результат:
<тут содержимое папки>
"""

@contextmanager
def in_dir(path):
    original_path = os.getcwd()
    try:
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Путь не существует: {path}")
        os.chdir(path)
        yield
    finally:
        os.chdir(original_path)


with in_dir('C:\\'):
    print(os.listdir())
