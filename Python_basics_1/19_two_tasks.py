"""
Задача 1. Пирамидка
Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран,
заполняя нечётными числами:
"""

def pyramid():
    rows = int(input("Введите количество ступенек: "))
    new_num = 1

    for line in range(rows):
        space_count = rows - line - 1
        print("   " * space_count, end="")
        for number in range(line + 1):
            print(new_num, end="   ")
            new_num += 2
        print()


"""
Задача 2. Яма
Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта.
"""

def pit():
    depth = int(input("Введите глубину ямы: "))

    for line in range(depth):
        for left_number in range(depth, depth - line - 1, -1):
            print(left_number, end="")
        point_count = 2 * (depth - line - 1)
        print("." * point_count, end="")
        for right_number in range(depth - line, depth + 1):
            print(right_number, end="")
        print()
