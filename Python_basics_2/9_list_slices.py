"""Срезы списков"""
import random

#Задача 1. Анализ цен
def prices():
    original_prices = [random.randint(-10, 10) for _ in range(5)]

    new_prices = original_prices[:]

    for i in range(len(new_prices)):
        if new_prices[i] < 0:
            new_prices[i] = 0

    print("Мы потеряли: ", sum(original_prices) - sum(new_prices))


#Задача 2. Срезы
def slices():
    nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

    print(nums[:5])
    print(nums[:-2])
    print(nums[::2])
    print(nums[1::2])
    print(nums[::-1])
    print(nums[::-2])


#Задача 3. Удаление части
def del_part():
    N = int(input("Введите размер списка: "))
    A = random.randint(3, 5)
    B = random.randint(6, 10)

    nums = [random.randint(1, 10) for _ in range(N)]
    print(nums)
    nums = [nums[i] for i in range(N) if i < A or i > B]

    print(A, B)
    print(nums)
