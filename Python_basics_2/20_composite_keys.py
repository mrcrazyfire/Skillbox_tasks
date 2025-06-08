"""Составные ключи"""

#Задача 1. Паспортные данные
def pass_data():
    data = {
        (5000, 123456): ('Иванов', 'Василий'),
        (6000, 111111): ('Иванов', 'Петр'),
        (7000, 222222): ('Медведев', 'Алексей'),
        (8000, 333333): ('Алексеев', 'Георгий'),
        (9000, 444444): ('Георгиева', 'Мария')
    }

    string = input("Введите серию и номер паспорта: ")
    passport = tuple(map(int, string.split()))

    if passport in data:
        print(data[passport])


#Задача 2. Контакты 2
def contacts():
    phonebook = dict()

    while True:
        name = input("Введите имя: ")
        if name == '':
            break
        surname = input("Введите фамилию: ")
        phone = int(input("Введите номер: "))

        phonebook[(surname, name)] = phone

    print(phonebook)
