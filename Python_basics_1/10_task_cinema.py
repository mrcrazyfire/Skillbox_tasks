"""
Задача «Кинотеатр»
X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд места в одном ряду.
Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам,
чтобы рядом с каждым мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.

На вход подаются два числа: количество мальчиков X и количество девочек Y. В ответе выведите какую-нибудь строку,
в которой будет ровно X символов B, обозначающих мальчиков, и Y символов G, обозначающих девочек,
что соответствует условиям задачи. Пробелы между символами выводить не нужно.
Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку «Нет решения».

Пример 1:

Введите количество мальчиков: 5
Введите количество девочек: 5
Ответ: BGBGBGBGBG

Пример 2:
Введите количество мальчиков: 5
Введите количество девочек: 3
Ответ: BGBGBBGB

Пример 3:
Введите количество мальчиков: 100
Введите количество девочек: 1
Ответ: Нет решения
"""

boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
answer = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения')
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girls - k):
        answer += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        answer += 'GBG'
    for gb in range(boys - k):
        answer += 'GB'

print(answer)
