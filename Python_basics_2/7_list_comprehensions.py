"""List comprehensions"""
from pyexpat.errors import messages


#Задача 1. Кубы и квадраты
def cubes_squares():
    A = int(input("Левая граница: "))
    B = int(input("Правая граница: "))

    cubes = [x ** 3 for x in range(A, B + 1)]
    squares = [x ** 2 for x in range(A, B + 1)]

    print(f"\nСписок кубов чисел в диапазоне от {A} до {B}: {cubes}")
    print(f"Список квадратов чисел в диапазоне от {A} до {B}: {squares}")


#Задача 2. Сообщение
def message():
    text = input("Введите строку: ")
    sym = input("Введите дополнительный символ: ")

    first_list = [letter * 2 for letter in text]
    second_list = [letter + sym for letter in first_list]

    print(f"Список удвоенных символов: {first_list}")
    print(f"Склейка с дополнительным символом: {second_list}")


#Задача 3. Повышение цен
def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)

def price_up():
    prices = []

    for _ in range(5):
        price = float(input("Цена на товар: "))
        prices.append(price)

    first_percent = int(input("Повышение на первый год: "))
    second_percent = int(input("Повышение на второй год: "))

    prices_first = [get_higher_price(first_percent, price) for price in prices]
    prices_second = [get_higher_price(second_percent, price) for price in prices_first]

    print(f"Сумма цен за каждый год: {round(sum(prices), 2)}, {round(sum(prices_first), 2)}, {round(sum(prices_second), 2)}")
