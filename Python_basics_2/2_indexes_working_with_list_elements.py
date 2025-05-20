"""Индексы. Работа с элементами списка"""


#Задача 1. Гугл
def min_max_num():
    n = int(input('Кол-во чисел в списке: '))
    nums_list = []

    for _ in range(n):
        num = int(input('Очередное число: '))
        nums_list.append(num)

    maximum = nums_list[0]
    minimum = nums_list[0]

    for i in nums_list:
        if maximum < i:
            maximum = i

        if minimum > i:
            minimum = i

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)


#Задача 2. Кратность
def divide():
    n = int(input('Кол-во чисел в списке: '))
    nums_list = []

    for i in range(n):
        num = int(input(f'Введите {i + 1} число: '))
        nums_list.append(num)

    divider = int(input('\nВведите делитель: '))

    summa = 0
    for i in range(n):
        if nums_list[i] % divider == 0:
            print(f'Индекс числа {nums_list[i]}: {i}')
            summa += i

    print(f'Сумма индексов: {summa}')


#Задача 3. Собачьи бега
def dog_running():
    n = int(input('Введите ко-во собак: '))
    dogs_list = []

    for _ in range(n):
        score = int(input('Введите кол-во очков собаки: '))
        dogs_list.append(score)

    minimum = dogs_list[0]
    i_minimum = 0
    maximum = dogs_list[0]
    i_maximum = 0

    for i in range(n):
        if dogs_list[i] < minimum:
            minimum = dogs_list[i]
            i_minimum = i

        if dogs_list[i] > maximum:
            maximum = dogs_list[i]
            i_maximum = i

    print(dogs_list)

    dogs_list[i_minimum] = maximum
    dogs_list[i_maximum] = minimum

    print(dogs_list)
