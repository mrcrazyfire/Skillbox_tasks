"""Задача «Почта»"""


def mail():
    hour = int(input("Введите число от 0 до 23: "))

    if (8 <= hour < 22) and (hour != 14 and hour != 10 and hour != 18):
        print("Можно получить посылку")
    else:
        print("Посылку получить нельзя")
