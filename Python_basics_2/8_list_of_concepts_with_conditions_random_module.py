"""List comprehensions с условиями. Модуль random"""
import random

#Задача 1. Список чётных чисел
def even_numbers():
    A = int(input("Введите откуда заполнять список: "))
    B = int(input("Введите докуда заполнять список: "))
    numbers = [num for num in range(A, B + 1) if num % 2 == 0]
    print(numbers)


#Задача 2. Магазин
def shop():
    original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
    new_prices = [(price if price > 0 else 0) for price in original_prices]

    print("Старые цены:", original_prices)
    print("Новые цены:", new_prices)


#Задача 3. Отряды
def squads():
    squad_1 = [random.randint(50, 80) for _ in range(10)]
    squad_2 = [random.randint(30, 60) for _ in range(10)]
    squad_3 = [("Погиб" if squad_1[i_damage] + squad_2[i_damage] > 99 else "Выжил") for i_damage in range(10)]

    print("Первый отряд:", squad_1)
    print("Второй отряд:", squad_2)
    print("Результат:", squad_3)
