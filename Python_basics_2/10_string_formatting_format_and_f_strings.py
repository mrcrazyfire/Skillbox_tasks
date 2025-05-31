"""Форматирование строк: format и f-strings"""


#Задача 1. Заказ
def order():
    name = input("Имя: ")
    order_num = int(input("Номер заказа: "))

    print("Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!".format(name, order_num))


#Задача 2. Долги
def debts():
    name = input("Введите имя: ")
    debt = int(input("Введите долг: "))

    print("{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}! ".format(name, debt))


#Задача 3. IP-адрес
def ip_address():
    ip_addr = "{0}.{1}.{2}.{3}"
    numbers = []
    count = 0
    while count < 4:
        number = int(input("Введите число: "))
        if 0 <= number <= 255:
            numbers.append(number)
            count += 1

    print(ip_addr.format(*numbers))
