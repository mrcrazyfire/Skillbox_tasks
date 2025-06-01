text = "утиное филе;фланк-стейк;банановый пирог;плов"

menu_list = text.title().split(';')

print("На данный момент в меню есть:", ', '.join(menu_list))