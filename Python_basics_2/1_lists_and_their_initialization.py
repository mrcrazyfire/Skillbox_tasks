"""Списки и их инициализация"""


#Задача 1. Таблица степеней
def table_of_powers():
    numbers = [3, 7, 5]

    while True:
        number = int(input('Новое число: '))
        numbers.append(number)

        print('Текущий список чисел:', numbers)

        for i in numbers:
            print(i ** 2, i ** 3, i ** 4)
        print()


#Задача 2. Очень простая задача
def simple_task():
    numbers = []

    for i in range(101):
        numbers.append(i)

    print(numbers)


#Задача 3. Контроль
def control():
    emp_count = int(input('Введите количество сотрудников: '))
    employees_id = []

    for _ in range(emp_count):
        employee_id = input('Введите ID сотрудника: ')
        employees_id.append(employee_id)

    find_id = input('Какой ID ищем: ')

    if find_id in employees_id:
        print('ID найден')
    else:
        print('ID не найден')
