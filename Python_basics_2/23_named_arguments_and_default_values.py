"""Именованные аргументы и значения по умолчанию"""

#Задача 1. Работа с файлом
def ask_user(question,
             complaint='Введите да или нет',
             choices = 3):
    while True:
        answer = input(question)

        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0

        choices -= 1
        if choices == 0:
            print("Кол-во попыток истекло.")
            return -1

        print(complaint + '\n')
        print(f'Осталось попыток: {choices}')


#Задача 2. Накопление значений
def add_num(num, lst=None):
    if lst is None:
        lst = []

    lst.append(num)

    print(lst)


#Задача 3. Помощь другу
def create_dict(data, template={}):
    if isinstance(data, dict):
        return data

    if isinstance(data, (int, float, str)):
        return {data: data}

    return None


def data_preparation(old_list):
    new_dict = {}
    for item in old_list:
        result = create_dict(item)
        if result:
            new_dict.update(create_dict(item))

    return new_dict


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)
