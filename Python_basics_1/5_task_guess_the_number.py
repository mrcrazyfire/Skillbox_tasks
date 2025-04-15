"""Задача «Угадай число»"""


def guess_number():
    start = 1
    finish = 100
    count = 1

    while True:
        n = (start + finish) // 2
        print("Загаданное число равно, меньше или больше", n)
        answer = int(input("1 - равно, 2 - меньше, 3 - больше "))

        if answer == 2:
            finish = n - 1
        elif answer == 3:
            start = n + 1
        elif answer == 1:
            print("Я угадал! Ура! с ", count, "попытки")
            break
        count += 1
