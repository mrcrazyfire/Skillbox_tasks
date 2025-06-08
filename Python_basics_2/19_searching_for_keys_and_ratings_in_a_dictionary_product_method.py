""" Перебор ключей и значений в словаре. Метод items"""

#Задача 1. Кризис минова
def crisis():
    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }

    for name, cost in incomes.items():
        print(f"{name} -- {cost}")


#Задача 2. Сервер
def server():
    server_data = {
        "server": {
            "host": "127.0.0.1",
            "port": "10"
        },
        "configuration": {
            "access": "true",
            "login": "Ivan",
            "password": "qwerty"
        }
    }

    for k_data, v_data in server_data.items():
        print(f"{k_data}:")
        for key, value in v_data.items():
            print(f"\t{key}: {value}")


#Задача 3. В одну строчку
def in_one_line():
    print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])


