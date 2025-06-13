"""Задача 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
Напишите программу, которая выводит их сумму в выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt:
1
2
3
4
10

Содержимое файла answer.txt
20
"""

def create_file(path, numbers):
    with open(path, 'w', encoding="utf-8") as f:
        for num in numbers:
            f.write(str(num) + '\n')


def sum_numbers(path):
    summ = 0
    with open(path, 'r', encoding="utf-8") as f:
        for num in f:
            summ += int(num)

    return summ

numbers_list = [1, 2, 3, 4, 10]

create_file('numbers.txt', numbers_list)

print(sum_numbers('numbers.txt'))