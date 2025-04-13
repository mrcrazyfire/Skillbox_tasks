"""Задача 1. Режем число на части"""


def task_1():
    number = 1234
    digit_1 = number // 1000
    digit_2 = number // 100 % 10
    digit_3 = number % 100 // 10
    digit_4 = number % 10

    print(digit_1, digit_2, digit_3, digit_4)


"""Задача 2. Поменять местами"""


def task_2():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    print(a, b)

    a += b
    b = a - b
    a = a - b

    print(a, b)
