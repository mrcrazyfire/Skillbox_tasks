from functools import wraps
from typing import Callable

def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции.
    Args:
        func: оборачиваемая функция.
    Returns:
        Возвращает обернутую функцию
    """

    @wraps(func)
    def wrapper(*args, **kwargs,):
        wrapper.count += 1
        print(wrapper.count)
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper



@counter
def test() -> None:
    """
    Функция, в которой что-то происходит.
    """
    print("Тут что-то происходит!")



test()
test()
test()