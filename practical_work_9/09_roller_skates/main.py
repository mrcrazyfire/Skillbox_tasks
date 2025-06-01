skates = [] #Список с размерами роликов
people = [] #Список с размерами ног людей

skates_count = int(input("Кол-во коньков: ")) #Получаем кол-во коньков в наличии
for i_skate in range(skates_count): #Получаем размеры роликов в наличии
    size = int(input(f"Размер {i_skate + 1}-й пары: "))
    skates.append(size)

people_count = int(input("\nКол-во людей: ")) #Получаем кол-во желающих взять ролики
for i_people in range(people_count): #Получаем размеры ног людей
    size = int(input(f"Размер ноги {i_people + 1}-го человека: "))
    people.append(size)

count = 0 #Счетчик кол-ва людей, которые смогут взять ролики
for person in people: #Подсчитываем ролики, которые будут выданы, если они есть в наличии
    if person in skates:
        count += 1
        skates.remove(person) #Удаляем выданные из списка выданные ролики

print(f"Наибольшее кол-во людей, которые могут взять ролики: {count}") #Выводим кол-во роликов которые можно выдать