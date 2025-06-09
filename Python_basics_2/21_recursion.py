"""Рекурсия"""

import math


#Задача 1. Challenge
def challenge(num):
    if num == 1:
        return 1

    return num * challenge(num - 1)


#Задача 2. Степень числа
def power(a, n):
    if n == 0:
        return 1

    return a * power(a, n - 1)


#Задача 3. Поиск элемента
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result

