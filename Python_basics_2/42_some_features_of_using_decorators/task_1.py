from typing import Callable

def bread(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        print("</----------\\>")
        func(*args, **kwargs)
        print("<\\______/>")
    return wrapped

def fillings(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")
    return wrapped

@bread
@fillings
def sandwich(filling: str) -> None:
    print(f"--{filling}--")



sandwich("ветчина")