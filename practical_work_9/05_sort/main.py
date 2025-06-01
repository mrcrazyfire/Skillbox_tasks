import random


N = int(input("Введите кол-во элементов в списке: ")) #Вводим кол-во элементов списка
nums = [] #Список чисел

for _ in range(N): #Заполняем список случайными числами от 1 до 10
    nums.append(random.randint(1, 10))

print(f"Изначальный список: {nums}") #Выводим изначальный список

for current_num in range(len(nums)): #Сортируем список
    for next_num in range(current_num + 1, len(nums)):
        if nums[current_num] < nums[next_num]:
            nums[current_num], nums[next_num] = nums[next_num], nums[current_num]

print(f"Отсортированный список: {nums}") #Выводим отсортированный список