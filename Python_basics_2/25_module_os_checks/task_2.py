"""
Задача 2. Поиск файла
В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
Однако, как мы понимаем, файлов с таким названием может быть несколько.

Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла,
проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

Пример:
Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
Имя файла: lesson2
"""

import os

def find_file(path, target):
    for element in os.listdir(path):
        cur_path = os.path.join(path, element)

        if os.path.isfile(cur_path):
            if element == target:
               print(cur_path)
        elif os.path.isdir(cur_path):
            find_file(cur_path, target)

abs_path = input("Ищем в: ")
filename = input("Имя файла: ")


print("Найденные файлы: ")
find_file(abs_path, filename)