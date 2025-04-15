"""Цель заданий:
Научиться работать с операторами while, break,
логическим типом True/False, счётчиками, а также с бесконечным циклом."""


def task_1():
    n = int(input("Введите число: "))

    counter = 1
    while counter <= n:
        print(f"{counter} ** {n} = {counter**3}")
        counter += 1


def task_2():
    number = int(input("Введите число: "))

    if number < 0:
        print("Введите положительное число")
    else:
        counter = 1
        while number > 0:
            if number // 10 == 0:
                print(f"Кол-во цифр в числе: {counter}")
                break
            number //= 10
            counter += 1


def task_3():
    print("Начался восьмичасовой рабочий день.")

    hour = 1
    tasks = 0
    call = 0
    while hour <= 8:
        print(f"{hour}-й час")
        tasks += int(input("Сколько задач решит Максим? "))
        if call < 1:
            call += int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
        hour += 1

    print(f"Рабочий день закончился. Всего выполнено задач: {tasks}")
    if call > 0:
        print("Нужно зайти в магазин.")


def task_4():
    deposit = int(input("Вклад в банке: "))
    percent = int(input("Проценты: "))
    threshold = int(input("Порог вклада: "))

    year = 1
    while deposit < threshold:
        deposit += deposit * percent // 100
        print(f"{year} год. {deposit}")
        year += 1

    print(f"Кол-во лет для достижения порога: {year}")


def task_5():
    number_1 = int(input("Загадайте число от 1 до 10: "))

    counter = 1
    while True:
        number_2 = int(input("Введите число: "))
        if number_1 == number_2:
            print(f"Вы угадали! Число попыток: {counter}")
            break
        elif number_1 > number_2:
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
        else:
            print("Число больше, чем нужно. Попробуйте ещё раз!")
        counter += 1
