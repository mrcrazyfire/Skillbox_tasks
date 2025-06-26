import time


def timer(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return round(end - start, 5)


def func_1():
    sum = 0
    for i in range(1000):
        sum += i

def func_2(n):
    sum = 0
    for i in range(n):
        sum += i * n



print(timer(func_1))
print()
print(timer(func_2, 100000000))