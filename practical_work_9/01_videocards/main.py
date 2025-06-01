num_cards = int(input("Количество видеокарт: ")) #Кол-во видеокарт
cards = [] #Список всех видеокарт

for i_card in range(num_cards): #Добавляем нужное кол-во видеокарт в список
    card = int(input(f"{i_card + 1} Видеокарта: "))
    cards.append(card)

print(f"\nСтарый список видеокарт: {cards}") #Выводим список видеокарт

max_card = max(cards) #Получаем номер старшей видеокарты в линейке
while max_card in cards: #Удаляем из списка все видеокарты старшей линейки
    cards.remove(max_card)

print(f"Новый список видеокарт: {cards}") #Выводим обновленный список
