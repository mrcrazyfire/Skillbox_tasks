from typing import Callable, Any
from functools import wraps

def do_twice(func: Callable) -> Callable:
    @wraps(func)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped




@do_twice
def greeting(name: str) -> None:
    """
    Функция, которая выводит в консоль сообщение с приветствием.
    :param name: Имя для приветствия
    """
    print(f"Привет, {name}!")


greeting("Yury")