import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, round(end - start, 2)
    return wrapped

@timer
def my_func(N) -> float:
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += i * j / (i + j)
    return round(sum, 3)


result, time = my_func(10_000)

print(result, time)