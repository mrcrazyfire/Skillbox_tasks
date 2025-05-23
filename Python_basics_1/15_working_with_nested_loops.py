""" Работа со вложенными циклами """

"""
Задача 1. Таблица умножения
Математик Паша недавно заметил, что у него уже есть куча разных таблиц степеней,
но нет самого основного — таблицы умножения.
Пора бы это исправить.

Напишите программу, которая выводит таблицу умножения для чисел от 1 до 9.
Для этого используйте конструкцию вложенного цикла: внешний отвечает за первый множитель,
а внутренний — за второй.

Дополнение: выведите настоящую таблицу умножения, без всяких знаков, только числа.
Чтобы она получилась красивой и ровной, используйте литерал \t внутри оператора end. \t — это литерал табуляции,
благодаря ему все числа выстраиваются в виде таблицы.
"""

def multiple_func():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i * j, end='\t')
        print()


"""
Задача 2. Таблица суммы
Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 0 до N.
"""

def sum_func():
    n = int(input("Введите число: "))

    for i in range(n + 1):
        for j in range(n + 1):
            print(i + j, end='\t')
        print()

"""
Задача 3. Анализ данных
"""

def data_analys():
    for i in range(10):
        for j in range(10):
            print(i - j, end='\t')
        print()
