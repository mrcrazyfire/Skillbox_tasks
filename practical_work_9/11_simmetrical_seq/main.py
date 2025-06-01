def is_palindrome(numbers): #Проверяем последовательность на симметрию
    return numbers == numbers[::-1]

def to_append(numbers): #Ищем наименьший индекс с которого последовательность является палиндромом
    i = 0
    while i < N:
        if is_palindrome(numbers[i:]):
            break
        i += 1
    return numbers[:i][::-1] #Сначала делаем срез [:i], а после переворачиваем список [::-1]


N = int(input("Кол-во чисел: ")) #Вводим кол-во чисел в последовательность
numbers = [] #Список последовательность

for _ in range(N): #Заполняем последовательность
    numbers.append(int(input("Число: ")))

print(f"Последовательность: {numbers}") #Выводим последовательность

if is_palindrome(numbers): #Проверяем последовательность на симметрию
    print("Последовательность симметрична") #Если симметрична, то ничего делать не надо
else:
    append_numbers = to_append(numbers) #Иначе вызываем функцию
    print(f"Нужно прописать чисел: {len(append_numbers)}")
    print(f"Сами числа: {append_numbers}")