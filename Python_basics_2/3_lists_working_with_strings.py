"""Списки: работа со строками"""


#Задача 1. Текстовый редактор: возвращение
def text_editor():
    s = input("Введите строку: ")
    s_list = list(s)

    count = 0
    index = 0
    for sym in s_list:
        if sym == ':':
            s_list[index] =  ';'
            count += 1
        index += 1

    for sym in s_list:
        print(sym, end='')

    print(f"\nКоличество замен: {count}")


#Задача 2. Соседи
def neighbours():
    s = input("Введите строку: ")
    i = int(input("Введите номер символа: "))
    s_list = list(s)

    count = 0
    for sym in s_list:
        if sym == s_list[i - 1]:
            count += 1

    print(f"\nСимвол слева: {s_list[i - 2]}")
    print(f"Символ справа: {s_list[i]}")

    if count - 1 == 1:
        print("Есть ровно один такой же символ")
    elif count == 2:
        print("Есть два таких же")
    else:
        print("Их нет")


#Задача 3. Улучшенная лингвистика
def linguistics():
    words_list = []
    counts_list = [0, 0, 0]

    for i in range(3):
        word = input(f"Введите {i + 1} слово: ")
        words_list.append(word)

    word = input("Слово из текста: ")
    while word != "end":
        for i in range(3):
            if words_list[i] == word:
                counts_list[i] += 1
        word = input("Слово из текста: ")

    print("\nПодсчёт слов в тексте")
    for i in range(3):
        print(f"{words_list[i]}: {counts_list[i]}")
