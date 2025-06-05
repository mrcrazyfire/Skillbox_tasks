"""Кортежи"""
import random, math

#Задача 1. Создание кортежей
def create_tuples():
    tuple_1 = tuple(random.randint(0, 5) for _ in range(10))
    tuple_2 = tuple(random.randint(-5, 0) for _ in range(10))
    tuple_3 = tuple_1 + tuple_2

    print("{}".format(tuple_3))
    zero_count = tuple_3.count(0)
    print("Количество нулей: {}".format(zero_count))


#Задача 2. Цилиндр
def cylinder():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))

    size = 2 * math.pi * r * h
    s = math.pi * r ** 2
    full = size + 2 * s

    return size, full


#Задача 3. Неправильный код
def change(nums):
    index = random.randint(0, len(nums) - 1)
    value = random.randint(100, 1000)
    nums = nums[:index] + (value,) + nums[index + 1:]
    return nums, value


my_nums = (1, 2, 3, 4, 5)
new_nums, rand_val_1 = change(my_nums)
print(new_nums, rand_val_1)
new_nums, rand_val_2 = change(new_nums)
rand_val = rand_val_1 + rand_val_2

print(new_nums, rand_val)