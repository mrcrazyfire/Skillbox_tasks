num_people = int(input("Кол-во человек: ")) #Вводим кол-во человек
num = int(input("Какое число в считалке? ")) #Вводим какой человек по счету выбывает
people = [i for i in range(1, num_people + 1)] #Заполняем список нужным кол-вом людей

print(f"Значит выбывает каждый {num}-й человек\n")

i_start = 0 #Индекс старта
i_leave = 0 #Индекс выбывающего элемента
while len(people) > 1:
    i_leave = (i_start + num - 1) % len(people) #Вычисляем индекс элемента который выбывает
    print(f"Текущий круг людей: {people}")
    print(f"Начало счета с номера {people[i_start]}")
    print(f"Выбывает человек под номером {people[i_leave]}\n")
    people.remove(people[i_leave])
    i_start = i_leave % len(people) #Обновляем стартовый индекс

print(f"Остался человек под номером {people[0]}")