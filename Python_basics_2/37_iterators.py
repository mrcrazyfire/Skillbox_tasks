import random

n = int(input("Введите количество чисел: "))
numbers = [random.randint(-100, 100) for _ in range(n)]

buffer_iter = iter(numbers)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration:
        print("Конец!")
        break