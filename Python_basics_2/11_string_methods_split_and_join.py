"""Методы строк: split и join"""

#Задача 1. Улучшенная лингвистика 2
def linguistics():
    words = [input("Введите слово: ") for _ in range(3)]
    text = input("Введите текст: ")
    words_count = [text.count(word) for word in words]

    print(words_count)


#Задача 2. Бабушка
def grandmother():
    text = "У       нас         пошёл                    снег    ! "

    print(' '.join(text.split()))


#Задача 3. Разделители символов
def sym_divides():
    while True:
        text = input("Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ")
        if "{name" in text and "{age}" in text:
            break
        print("Ошибка! Отсутствует одна или несколько конструкций!")

    names_list = input("Список людей через запятую: ").split(", ")
    ages_list = input("Возраст людей через пробел: ").split()

    for i_person in range(len(names_list)):
        print(text.format(name=names_list[i_person], age=ages_list[i_person]))
