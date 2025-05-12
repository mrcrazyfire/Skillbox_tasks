"""
Сумма чисел.
Функция в функции.
Апгрейд калькулятора.
Текстовый редактор.
Недоделка.
"""


# Задача 1. Сумма чисел
def summa_n(n):
    summa = 0
    for number in range(1, n + 1):
        summa += number
    print(f"Сумма чисел от 1 до {n} равна {summa}")


num = int(input("Введите число: "))


# Задача 2. Функция в функции
def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test():
    number = int(input("Введите число: "))

    if number > 0:
        positive()
    else:
        negative()


# Задача 3. Апгрейд калькулятора
def sum_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print(f"Сумма цифр: {total}")


def max_digit(num):
    current_max = 0

    while num > 0:
        digit = num % 10

        if digit > current_max:
            current_max = digit

        num //= 10

    print(f"Максимальная цифра: {current_max}")


def min_digit(num):
    current_min = 9

    while num > 0:
        digit = num % 10

        if digit < current_min:
            current_min = digit

        num //= 10

    print(f"Минимальная цифра: {current_min}")


while True:
    num = int(input("Введите число: "))
    print("Введите номер действия:\n"
          "1 - сумма цифр\n"
          "2 - максимальная цифра\n"
          "3 - минимальная цифра: ", end='')
    choice = int(input())

    if choice == 1:
        sum_digits(num)
    elif choice == 2:
        max_digit(num)
    elif choice == 3:
        min_digit(num)
    else:
        print("Ошибка ввода")
        break


# Задача 4. Текстовый редактор
def count_letters():
    text = input("Введите текст: ")
    number = input("Какую цифру ищем? ")
    letter = input("Какую букву ищем? ")

    count_letter = 0
    count_number = 0

    for item in text:
        if item == letter:
            count_letter += 1
        elif item == number:
            count_number += 1

    print(f"Количество цифр {number}: {count_number}")
    print(f"Количество букв {letter}: {count_letter}")


# Задача 5. Недоделка
def rock_paper_scissors():
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ")
    computer_choice = "камень"

    if user_choice == "камень":
        print("Ничья")
    elif user_choice == "ножницы":
        print("Проиграли")
    elif user_choice == "бумага":
        print("Победили")
    else:
        print("Ошибка ввода")


def guess_the_number():
  computer_number = 7

  while True:
    print("Угадайте число от 1 до 9")
    user_number = int(input("Введите число: "))

    if user_number == computer_number:
        print("Вы угадали")
        break
    else:
        print("Не правильно, попробуйте еще раз")


def main_menu():
    print("Добро пожаловать")
    print('Для игры в "Камень, ножницы, бумага" выберите 1')
    print('Для игры в "Угадай число" выберите 2')
    choice = int(input("Ваш выбор: "))

    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    else:
        print("Ошибка ввода")
