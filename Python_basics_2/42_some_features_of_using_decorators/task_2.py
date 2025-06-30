from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = {}

def logging(func: Callable):
    def wrapped(*args, **kwargs):
        PLUGINS[func.__name__] = func
        return func(*args, **kwargs)
    return wrapped

@logging
def say_hello(name: str) -> str:
    return f"Hello, {name}!"
@logging
def say_goodbye(name: str) -> str:
    return f"GoodBye, {name}!"




say_hello("Yury")
say_goodbye("Yury")
say_hello("Tom")
print(PLUGINS)
