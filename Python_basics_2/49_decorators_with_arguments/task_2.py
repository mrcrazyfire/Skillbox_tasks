from time import sleep
from functools import wraps


def sleeper(_func=None, *, seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)


@sleeper(seconds=5)
def test():
    print("Hello, World!")

test()



