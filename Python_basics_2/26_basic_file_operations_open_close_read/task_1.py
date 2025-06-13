import os

group_1_path = os.path.join(os.getcwd(), "task", "group_1.txt")
group_2_path = os.path.join(os.getcwd(), "task", "Additional_info", "group_2.txt")


summa = 0
diff = 0
with open(group_1_path, 'r', encoding='utf-8') as group_1:
    for line in group_1:
        info = line.split()
        score = int(info[2])
        summa += score
        diff -= score

print("Сумма очков 1й-группы:", summa)
print("Разница очков 1й-группы:", diff)

compose = 1
with open(group_2_path, 'r', encoding='utf-8') as group_2:
    for line in group_2:
        info = line.split()
        score = int(info[2])
        compose *= score

print("Произведение очков 2й-группы:", compose)