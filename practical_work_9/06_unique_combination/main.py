def merge_sorted_lists(list1, list2):
    merged_list = list1 + list2 #Обьединяем 2 списка в 1

    for current_num in range(len(merged_list)):  # Сортируем список
        for next_num in range(current_num + 1, len(merged_list)):
            if merged_list[current_num] > merged_list[next_num]:
                merged_list[current_num], merged_list[next_num] = merged_list[next_num], merged_list[current_num]

    index = 0
    while index < len(merged_list) - 1: # Удаляем дубликаты
        if merged_list[index] == merged_list[index + 1]:
            merged_list.remove(merged_list[index])
        index += 1

    return merged_list



# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)