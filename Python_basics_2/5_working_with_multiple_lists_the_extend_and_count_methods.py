"""Работа с несколькими списками. Методы extend и count"""


#Задача 1. Задачи компаний
def count_tasks():
    main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    first_company = [0, 0, 0]
    second_company = [1, 0, 0, 1, 1]
    third_company = [1, 1, 1, 0, 1]

    main.extend(first_company)
    main.extend(second_company)
    main.extend(third_company)

    print("Общий список задач:", main)
    print("Количество невыполненных задач:", main.count(0))


#Задача 2. Вредоносное ПО
def count_malware():
    first_message = input("Первое сообщение: ")
    second_message = input("Второе сообщение: ")

    first_count = first_message.count("!") + first_message.count("?")
    second_count = second_message.count("!") + second_message.count("?")

    if first_count > second_count:
        print(first_message + second_message)
    else:
        print(second_message + first_message)


#Задача 3. Пакеты
def count_packages():
    pack = []
    decode = []
    error_count = 0

    pack_atm = int(input("Введите кол-во пакетов: "))

    for i_pack in range(pack_atm):
        print("Пакет №", i_pack + 1)
        for i_bit in range(4):
            bit = int(input(f"Введите {i_bit + 1}й бит: "))
            pack.append(bit)
        if pack.count(-1) <= 1:
            decode.extend(pack)
        else:
            error_count += 1
        pack = []
        print()

    print("Декодированные пакеты:", decode)
    print("Количество ошибок:", decode.count(-1))
    print("Количество битых пакетов:", error_count)
