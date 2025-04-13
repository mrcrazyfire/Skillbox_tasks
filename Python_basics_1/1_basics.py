"""1. Найти пропавшую переменную.
2. Исправить программу с названиями цвета.
3. Вывести на экран фразу о животных.
4. Исправить программу о доступе к системе.
5. Написать запрос о городах вылета и прилёта.
6. Поменять местами значения двух переменных (задача повышенной сложности)."""


def task_1():
    client = "Петя"
    pet = "Кот"
    print(client)
    print(" и ")
    print(pet)


def task_2():
    r = "Red"
    g = "Green"
    b = "Blue"

    print(r, b, g, r + g + b, b, g + b)


def task_3():
    first_animal, second_animal = "Заяц", "Черепаха"

    print(f"{first_animal} спит, {second_animal} идёт")


def task_4():
    first_name = input("Введите имя пользователя: ")
    greeting = "Привет,"
    intro = "К сожалению, у Вас нет доступа к системе."
    info = "Пожалуйста, обратитесь к системному администратору."

    print(greeting, first_name)
    print(intro)
    print(info)


def task_5():
    departure_city = input("Введите город вылета: ")
    arrival_city = input("Введите город прилёта: ")
    result = f"{departure_city} - {arrival_city}"

    print(result)


def task_6():
    a = input("Введите первое слово: ")
    b = input("Введите второе слово: ")

    print(a, b)

    a, b = b, a

    print(a, b)
