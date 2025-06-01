import random


N = int(input("Введите кол-во элементов в списке: ")) #Вводим кол-во элементов списка
K = int(input("Введите сдвиг: ")) #Вводим сдвиг списка
original_list = [] #Изначальный список
shifted_list = [] #Сдвинутый список

for _ in range(N): #Заполняем список случайными числами от 1 до 10
    original_list.append(random.randint(1, 10))

print(f"Изначальный список: {original_list}") #Выводим изначальный список

for index in range(K, len(original_list)): #Заполняем список элементами которые идут после сдвига
    shifted_list.append(original_list[index])

for index in range(0, K): #Заполняем список элементами которые идут до сдвига
    shifted_list.append(original_list[index])

print(f"Сдвинутый список: {shifted_list}") #Выводим сдвинутый список