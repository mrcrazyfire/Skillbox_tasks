def func_1(x):
    return x + 10


def func_2(func, *args, **kwargs):
    return func(*args, **kwargs) * func(*args, **kwargs)

print(func_2(func_1, 9))