"""
Задача 2. Возраст
Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.

Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
и выводит результат в новый файл result.txt в формате «имя — возраст».
Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:

Попытка создания файла, который уже существует.
На чтение ожидался файл, но это оказалась директория.
Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
"""

def print_file(filename):
    with open(filename) as f:
        print(f.read())


def add_names(input_filename, output_filename):
    try:
        with open(input_filename, "r") as input_file:
            try:
                with open(output_filename, "x") as output_file:
                    alphabet = 'abcdefghijklmnopqrstuvwxyz'
                    for i, line in enumerate(input_file):
                        output_file.write(alphabet[i] + line + '\n')
            except FileExistsError:
                print(f"Файл с именем {output_filename} уже существует.")
    except FileNotFoundError:
        print(f"Файла с именем {input_filename} не обнаружено.")
    except IsADirectoryError:
        print(f"Вы ввели имя директории.")


add_names("ages.txt", "result.txt")

print_file("result.txt")