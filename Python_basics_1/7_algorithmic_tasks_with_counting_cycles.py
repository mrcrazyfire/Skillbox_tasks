def cubes():
    n = int(input("Введите число: "))
    for number in range(1, n // 2 + 1):
        number *= 2
        print(f"{number}^3 = {number ** 3}")

def cells():
    total_hours = int(input("Введите количество часов: "))
    hours = 0
    cells = 1
    for i in range(total_hours // 3):
        cells *= 2
        hours += 1
    print(f"Прошло часов: {hours * 3}, количество клеток: {cells}, осталось часов: {total_hours % 3}.")

def squares():
    n = int(input("Введите число: "))
    for number in range(1, n // 2 + n % 2 + 1):
        number = number * 2 - 1
        print(f"{number}^2 = {number ** 2}")