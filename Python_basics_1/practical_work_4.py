"""
Что входит в практическую работу:
1. «Я стал новым пиратом!»
2. Театр.
3. Марсоход-2.
4. Великий и могучий.
5. Коровы.
"""

"""
Задача 1. «Я стал новым пиратом!»
Старому капитану нужно пополнить команду, но на корабль попадут только достойные.
Он отобрал десять человек. Те, кто крикнет слово «Карамба», попадут на борт.

Что нужно сделать
Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».
"""

def karamba():
    words_counter = 0

    for _ in range(10):
        word = input("Введите слово: ")
        if word == "Карамба" or word == "карамба":
            words_counter += 1

    print(f'Количество слов "Карамба" - {words_counter}')


"""
Задача 2. Театр
В городе планируют построить театр под открытым небом, но для начала нужно оценить,
сколько сделать рядов, сидений в них и каким должно быть расстояние между рядами.

Что нужно сделать
Напишите программу, которая получает на вход количество рядов, сидений и свободных метров между рядами,
а затем выводит примерный макет театра на экран.

Рекомендации по выполнению
Можно воспользоваться синтаксическим сахаром: умножением строки на число и конкатенацией (объединение строк).
Для начала получите одну строку.
"""

def cinema():
    rows = int(input("Введите кол-во рядов: "))
    seats = int(input("Введите кол-во сидений в ряде: "))
    meters = int(input("Введите кол-во метров между рядами: "))

    print("\nСцена\n")

    for row in range(rows):
        print("=" * seats, "*" * meters, "=" * seats)


"""
Задача 3. Марсоход-2
К роботу Валли планируют отправить «коллегу» Билли.
Это первая высадка Билли на Марс, поэтому его тестируют в прямоугольном помещении размером 15 × 20 м.
Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору,
то есть пользователю вашей программы.

Программа спрашивает, в какую сторону оператор хочет направить робота: север (клавиша W), юг (клавиша S),
запад (клавиша A) или восток (клавиша D). Оператор делает выбор, марсоход перемещается в эту сторону на один метр,
а программа сообщает новую позицию робота. Если марсоход упёрся в стену,
он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется.

Что нужно сделать
Создайте программу для управления роботом Билли.

Пример

[Программа]: Марсоход находится на позиции 6, 19, введите команду:
[Оператор]: A
[Программа]: Марсоход находится на позиции 5, 19, введите команду:
[Оператор]: W
[Программа]: Марсоход находится на позиции 5, 20, введите команду:
[Оператор]: W
[Программа]: Марсоход находится на позиции 5, 20, введите команду:

Рекомендации по выполнению
Обращайте внимание на границы.
Попробуйте изменять положение марсохода только после проверки координат.
Ввод команд происходит только в верхнем регистре, учитывать нижний не нужно.
Старайтесь максимально уменьшать количество дублирований кода.
Если действие выполняется независимо от условий, не стоит дублировать его в каждом условии.
"""

def billy():
    x = 8
    y = 10

    while True:
        print(f"[Программа]: Марсоход находится на позиции {x}, {y}, введите команду:")
        command = input("[Оператор]: ")

        if command == "W":
            if y < 20:
                y += 1
        elif command == "S":
            if y > 1:
                y -= 1
        elif command == "A":
            if x > 1:
                x -= 1
        elif command == "D":
            if x < 15:
                x += 1
        else:
            break


"""
Задача 4. Великий и могучий
Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
Ему особенно понравилась книга «Преступление и наказание».
Паоло решил найти самое длинное слово в этой книге, чтобы сравнить его с аналогом на своём языке.

Что нужно сделать
Напишите программу, которая получает на вход текст и находит длину самого длинного слова в нём.
Слова в тексте разделяются одним пробелом.

Пример

Введите текст: Меня зовут Пётр.
Самое длинное слово, букв: 5.

Введите текст: Меня зовут Василий
Самое длинное слово, 7 букв

Рекомендации по выполнению
При помощи функции print убедитесь, что счётчики обнуляются в нужный момент.
Помните, что не все условия можно собирать в один условный блок.
Некоторые из них должны срабатывать независимо друг от друга.
"""

def longest_word_func():
    text = input("Введите текст: ")
    current_word_length = 0
    max_word_length = 0

    for char in text:
        if char != " ":
            current_word_length += 1
        else:
            if current_word_length > max_word_length:
                max_word_length = current_word_length
            current_word_length = 0

    if current_word_length > max_word_length:
        max_word_length = current_word_length

    print(f"Самое длинное слово, {max_word_length} букв")


"""
Задача 5. Коровы
Для коров есть 10 стойл. В каждом из них условия для животных разные, поэтому и молока они дают по-разному.
В первом стойле производят 2 литра в день, во втором — 4, в третьем — 6, далее — 8, 10, 12, 14, 16, 18 и 20.
При этом коровы находятся не во всех стойлах. Свободные и занятые обозначаются строкой из букв a и b,
где a — свободное стойло, b — занятое.

Что нужно сделать
Напишите программу для подсчёта получаемого молока в коровнике.
Важно учитывать следующее взаимодействие: пользователь вводит строку из десяти символов a и b.
Необходимо определить, сколько в итоге будет произведено молока за день.

Пример 1

Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:
abababaaaa

Произведено молока за день: 24

Пример 2

Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:
aaababbaab

Произведено молока за день: 54
"""

def cows():
    stables = input("Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:\n")
    milk_in_stable = 2
    total_milk = 0

    for stable in stables:
        if stable == "b":
            total_milk += milk_in_stable
        milk_in_stable += 2

    print(f"Произведено молока за день: {total_milk}")
