"""
Задача 1. Иконки
Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска:
папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
(на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение.
Если путь указывает на файл, то также выведите его размер (сколько он весит в байтах).
Обеспечьте контроль ввода: проверка пути на существование.
"""

import os

def icons(elem):
    path = os.path.abspath(os.path.join("..", "..", elem))

    print("Путь:", path)

    if not os.path.exists(path):
        print("Указанного пути не существует")
        return

    if os.path.isdir(path):
        print("Это папка")
    elif os.path.isfile(path):
        print("Это файл")
        print("Размер файла:", os.path.getsize(path), "байт")


user_input = input("Введите название элемента: ")
icons(user_input)