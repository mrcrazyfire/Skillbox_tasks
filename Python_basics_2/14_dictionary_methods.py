"""Методы словаря"""


#Задача 1. Склады
def storages():
    small_storage = {
        'гвозди': 5000,
        'шурупы': 3040,
        'саморезы': 2000
    }

    big_storage = {
        'доски': 1000,
        'балки': 150,
        'рейки': 600
    }

    big_storage.update(small_storage)

    product = input("Введите название товара: ").lower()

    if big_storage.get(product):
        print("{0}: {1}".format(product.title(), big_storage[product]))
    else:
        print("Данного товара нет")


#Задача 2. Кризис фруктов
def fruits():
    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'grapefruit': 300.40,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }

    total_income = sum(incomes.values())
    print("Общий доход за год составил {} рублей".format(total_income))

    min_fruit = min(incomes, key=incomes.get)
    min_income = incomes[min_fruit]
    print("Самый маленький доход у {0}. Он составляет {1} рублей".format(min_fruit, min_income))

    del incomes[min_fruit]

    print(f"Итоговый словарь: {incomes}")



#Задача 3. Гистограмма частоты
def histogram():
    text = input("Введите текст: ").lower()

    hist_dict = dict()
    for sym in text:
        if sym in hist_dict:
            hist_dict[sym] += 1
        else:
            hist_dict[sym] = 1



    for key, value in sorted(hist_dict.items()):
        print(f"{key}: {value}")
