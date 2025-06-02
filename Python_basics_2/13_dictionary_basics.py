"""Словарь: основы"""

#Задача 1. Словарь квадратов чисел
def dict_nums():
    nums = {}

    n = int(input("Введите целое число: "))

    for i in range(1, n + 1):
        nums[i] = i ** 2

    print(nums)


#Задача 2. Студент
def student():
    student_dict = {}
    info_str = input(
        "Введите информацию о студенте через пробел\n"
        "(имя, фамилия, город, место учёбы, оценки): "
    )

    info_list = info_str.split()

    student_dict["name"] = info_list[0]
    student_dict["surname"] = info_list[1]
    student_dict["city"] = info_list[2]
    student_dict["study"] = info_list[3]
    student_dict["grade"] = [num for num in info_list[4:]]

    for student in student_dict:
        print("{0} - {1}".format(student, student_dict[student]))


#Задача 3. Контакты
def contacts():
    contact_dict = {}

    while True:
        for contact in contact_dict:
            print("{0} {1}".format(contact, contact_dict[contact]))

        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")

        if name == '' or phone == '':
            break
        elif name not in contact_dict:
            contact_dict[name] = phone
        else:
            print("Такое имя уже есть в контактах")
