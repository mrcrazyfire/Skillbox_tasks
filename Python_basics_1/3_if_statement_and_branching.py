"""Задача «Максимальное число»"""


def max_number():
    a, b, c = 5, 7, 1

    if a > b:
        if a > c:
            print("a biggest")
    elif b > c:
        print("b biggest")
    else:
        print("c biggest")
