"""Работа со списками: методы insert, remove, index"""

#Задача 1. Зоопарк
def zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

    zoo.insert(1, "bear")
    zoo.remove("elephant")

    print(f"Зоопарк: {zoo}")
    print(f"Лев сидит в клетке номер {zoo.index('lion') + 1}")
    print(f"Обезьяна сидит в клетке номер {zoo.index('monkey') + 1}")


#Задача 2. сокращения
def abbs():
    employees = int(input("Введите кол-во сотрудников: "))
    salaries = []

    for i in range(employees):
        salary = int(input(f"Зарплата {i + 1} сотрудника: "))

        if salary > 0:
            salaries.append(salary)

    print(f"Осталось сотрудников: {len(salaries)}")
    print(f"Зарплаты: {salaries}")
    print(f"Минимальная зарплата: {min(salaries)}")
    print(f"Максимальная зарплата: {max(salaries)}")


#Задача 3. Кино
def movie():
    n = int(input("Сколько фильмов выбрать? "))
    your_films = []
    for _ in range(n):
        print("Ваш текущий топ фильмов:", your_films)
        film_name = input("Имя фильма: ")
        print("Команды: добавить, вставить, удалить")
        command = input("Введите команду: ")
        if film_name not in your_films:
            if command == "добавить":
                your_films.append(film_name)
            elif command == "вставить":
                insert_index = int(input("Введите индекс для вставки "))
                insert_index %= len(your_films)  # ограничим индекс списка, чтобы он не вылезал за границу списка
                your_films.insert(insert_index, film_name)
        else:
            if command == "удалить":
                your_films.remove(film_name)
            elif command == "добавить" or command == "вставить":
                print("Этот фильм уже есть в вашем списке.")

    print("Ваш текущий топ фильмов:", your_films)

movie()