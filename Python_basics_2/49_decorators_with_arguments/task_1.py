import functools


def repeat(n):
    def do_twice(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return do_twice


@repeat(5)
def test():
    print("Hello, World!")

test()







