"""Функция enumerate. Перебор нескольких значений"""

#Задача 1. Саботаж!
def sabotage():
    text = "so~mec~od~e"

    for index, value in enumerate(text):
        if value == '~':
            print(index, end=' ')


#Задача 2. Словари из списков
def dicts_from_lists():
    list_1 = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
    list_2 = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

    dict_1 = {}
    dict_2 = {}

    for key, value in enumerate(list_1):
        dict_1[key] = value

    for key, value in enumerate(list_2):
        dict_2[key] = value

    print("Первый словарь: {}".format(dict_1))
    print("Второй словарь: {}".format(dict_2))


#Задача 3. Универсальная программа
def universal_program(iterable):
    if isinstance(iterable, dict):
        iterable = list(iterable.keys())

    return [value for index, value in enumerate(iterable) if index % 2 == 0]
