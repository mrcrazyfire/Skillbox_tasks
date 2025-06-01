"""Методы строк: startswith, endswith, upper, lower"""

#Задача 1. Шифр Цезаря 2
def encrypt():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    message = input("Введите сообщение: ")
    K = int(input("Введите сдвиг: "))
    encrypted_message = [
        alphabet[(alphabet.find(symbol) + K) % len(alphabet)] if symbol in alphabet
        else symbol
        for symbol in message.lower()
    ]
    print(''.join(encrypted_message))


#Задача 2. Путь к файлу
def file_path():
    path = input("Путь к файлу: ")
    disk = input("На каком диске должен лежать файл: ")
    extension = input("Требуемое расширение файла: ")

    if path.startswith(disk) and path.endswith(extension):
        print("Путь корректен!")
    else:
        print("Ошибка ввода!")


#Задача 3. Удаление части
def del_part():
    text = input("Введите текст: ")
    lowers = len([letter for letter in text if letter.islower()])
    uppers = len([letter for letter in text if letter.isupper()])

    if lowers > uppers:
        print("Результат:", text.lower())
    else:
        print("Результат:", text.upper())
