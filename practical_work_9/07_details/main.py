shop = [
        ['каретка', 1200],
        ['шатун', 1000],
        ['седло', 300],
        ['педаль', 100],
        ['седло', 1500],
        ['рама', 12000],
        ['обод', 2000],
        ['шатун', 200],
        ['седло', 2700]
]

detail_name = input("Название детали: ") #Вводим название детали
detail_count = 0 #Счетчик деталей
detail_price = 0 #Общая стоимость

for detail in shop: #Перебираем детали в списке
        if detail[0] == detail_name:
                detail_count += 1
                detail_price += detail[1]

print(f"Кол-во деталей: {detail_count}")
print(f"Общая стоимость: {detail_price}")