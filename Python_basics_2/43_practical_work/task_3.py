"""
Задача 3. Логирование
Реализуйте декоратор logging, который будет отвечать за логирование функций.
На экран выводится название функции и её документация. Если во время выполнения декорируемой функции возникла ошибка,
то в файл function_errors.log записывается название функции и ошибки.

Постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
"""

import datetime
from functools import wraps
from typing import Callable, Any

def logging(func: Callable) -> Callable:
    """
    Декоратор, который при возникновении ошибки записывает её в лог-файл.
    Также выводит имя функции и её документацию.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"{func.__name__}: {func.__doc__}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("function_errors.log", "a", encoding="utf-8") as log:
                log.write(f"[{now}] {func.__name__}: {str(e)}\n")
    return wrapper

# Пример использования

@logging
def test() -> str:
    """Функция, которая что-то делает"""
    return "<Тут что-то происходит...>"

@logging
def boom() -> None:
    """Функция с ошибкой"""
    return 1 / 0  # Деление на ноль

# Вызовы:
print(test())
boom()