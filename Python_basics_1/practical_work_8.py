"""
Что входит в работу
Урок информатики 2.
Функция максимума.
Число наоборот.
Недоделка-2.
Маятник.
"""


import math

#Задача 1. Урок информатики 2

def floating_point_format(number):
    degree = int(math.floor(math.log10(number)))
    mantissa = number / (10 ** degree)
    # Получаем мантиссу и степень
    print(f"Формат плавающей точки: x = {mantissa} * 10 ** {degree}")


number = float(input("Введите число: "))

floating_point_format(number)


#Задача 2. Функция максимума

def maximum_of_two(a, b):
    return a if a > b else b


def maximum_of_three(a, b, c):
    return maximum_of_two(maximum_of_two(a, b), c)


a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

print(f"Самое большое число: {maximum_of_three(a, b, c)}")


#Задача 3. Число наоборот

def reverse_number(number):
    reversed_number = ''

    while number > 0:
        digit = number % 10
        reversed_number += str(digit)
        number //= 10

    return reversed_number


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print()
print(f"Первое число наоборот: {reverse_number(first_number)}")
print(f"Второе число наоборот: {reverse_number(second_number)}")

#Задача 4. Недоделка-2

def count_numbers(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def change_numbers(n):
    length = count_numbers(n)

    last_digit = n % 10
    first_digit = n // 10 ** (length - 1)
    between_digits = n % 10 ** (length - 1) // 10
    n = last_digit * 10 ** (length - 1) + between_digits * 10 + first_digit

    return n


def main():
    first_n = int(input("Введите первое число: "))
    if count_numbers(first_n) < 3:
        print("В первом числе меньше трёх цифр.")
        return

    second_n = int(input("Введите второе число: "))
    if count_numbers(second_n) < 4:
        print("Во втором числе меньше четырёх цифр.")
        return

    new_first_n = change_numbers(first_n)
    new_second_n = change_numbers(second_n)

    print(f"\nИзменённое первое число: {new_first_n}")
    print(f"Изменённое второе число: {new_second_n}")
    print(f"\nСумма чисел: {new_first_n + new_second_n}")


#Задача 5. Маятник

def amplitude_counter(amplitude, stopping_amplitude):
    count = 0
    while amplitude > stopping_amplitude:
        last_amplitude = amplitude * 0.084
        amplitude -= last_amplitude
        count += 1

    return count


amplitude = float(input("Введите начальную амплитуду: "))
stopping_amplitude = float(input("Введите амплитуду остановки: "))

result =  amplitude_counter(amplitude, stopping_amplitude)
print(f"Маятник считается остановившимся через {result} колебаний")
