"""Модуль os: генерация путей и метод listdir"""

import os


#Задача 1. Сисадмин
folder_name = "access"
file_name = "admin.bat"

path = os.path.join(folder_name, file_name)
abs_path = os.path.abspath(path)

print(f"Абсолютный путь до файла: {abs_path}")
print(f"Относительный путь до файла: {path}\n")


#Задача 2. Содержимое
my_dir = os.path.abspath("..")
print(f"Содержимое каталога {my_dir}")

for i_dir in os.listdir(my_dir):
    print(i_dir)


#Задача 3. Корень диска
path = os.path.abspath(os.sep).split(os.sep)[0]
print(f"\nКорень диска: {path}")