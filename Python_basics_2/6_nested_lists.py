"""Вложенные списки"""


#Задача 1. Матрица
def matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


#Задача 2. Олимпиада
def olympian():
    num_participants = int(input("Введите кол-во участников: "))
    team_size = int(input("Кол-во человек в команде: "))
    participants = []
    num = 1

    for _ in range(num_participants // team_size):
        participants.append(list(range(num, num + team_size)))
        num += team_size

    print(participants)


#Задача 3. Лавка
def shop():
    goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

    print(f"Текущий ассортимент: {goods}\n")

    fruit_name = input("Новый фрукт: ")
    price = int(input("Цена: "))

    goods.append([fruit_name, price])

    print(f"\nНовый ассортимент: {goods}")

    for fruit in goods:
        fruit[1] += fruit[1] * 8 / 100

    print(f"\nНовый ассортимент с увел. ценой: {goods}")
