"""Primary application entrypoint.
"""
import locale
import logging
import os
import sys
import warnings
from typing import List, Optional

from pip._internal.cli.autocompletion import autocomplete
from pip._internal.cli.main_parser import parse_command
from pip._internal.commands import create_command
from pip._internal.exceptions import PipError
from pip._internal.utils import deprecation

logger = logging.getLogger(__name__)


# Do not import and use main() directly! Using it directly is actively
# discouraged by pip's maintainers. The name, location and behavior of
# this function is subject to change, so calling it directly is not
# portable across different pip versions.

# In addition, running pip in-process is unsupported and unsafe. This is
# elaborated in detail at
# https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program.
# That document also provides suggestions that should work for nearly
# all users that are considering importing and using main() directly.

# However, we know that certain users will still want to invoke pip
# in-process. If you understand and accept the implications of using pip
# in an unsupported manner, the best approach is to use runpy to avoid
# depending on the exact location of this entry point.

# The following example shows how to use runpy to invoke pip in that
# case:
#
#     sys.argv = ["pip", your, args, here]
#     runpy.run_module("pip", run_name="__main__")
#
# Note that this will exit the process after running, unlike a direct
# call to main. As it is not safe to do any processing after calling
# main, this should not be an issue in practice.


def main(args: Optional[List[str]] = None) -> int:
    if args is None:
        args = sys.argv[1:]

    # Suppress the pkg_resources deprecation warning
    # Note - we use a module of .*pkg_resources to cover
    # the normal case (pip._vendor.pkg_resources) and the
    # devendored case (a bare pkg_resources)
    warnings.filterwarnings(
        action="ignore", category=DeprecationWarning, module=".*pkg_resources"
    )

    # Configure our deprecation warnings to be sent through loggers
    deprecation.install_warning_logger()

    autocomplete()

    try:
        cmd_name, cmd_args = parse_command(args)
    except PipError as exc:
        sys.stderr.write(f"ERROR: {exc}")
        sys.stderr.write(os.linesep)
        sys.exit(1)

    # Needed for locale.getpreferredencoding(False) to work
    # in pip._internal.utils.encoding.auto_decode
    try:
        locale.setlocale(locale.LC_ALL, "")
    except locale.Error as e:
        # setlocale can apparently crash if locale are uninitialized
        logger.debug("Ignoring error %s when setting locale", e)
    command = create_command(cmd_name, isolated=("--isolated" in cmd_args))

    return command.main(cmd_args)








































from typing import List, Optional


def main(args: Optional[List[str]] = None) -> int:
    """This is preserved for old console scripts that may still be referencing
    it.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)








































text = input("Введите текст: ")
vowels = "аеёиоуыэюя"

letters = [char for char in text if char in vowels]

print(f"Список гласных букв: {letters}")
print(f"Длинна списка {len(letters)}")








































N = int(input("Введите длину списка: "))

nums = [1 if num % 2 == 0 else num % 5 for num in range(0, N)]

print(nums)







































import random


team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10)) for _ in range(20)]

winners = [max(team_1[i], team_2[i]) for i in range(20)]

print(f"Первая команда: {team_1}")
print(f"Вторая команда: {team_2}")
print(f"Победители тура: {winners}")








































alphabet = 'abcdefg'

print(alphabet[:])
print(alphabet[::-1])
print(alphabet[::2])
print(alphabet[1::2])
print(alphabet[:1])
print(alphabet[-1:])
print(alphabet[3:4])
print(alphabet[-3:])
print(alphabet[3:5])
print(alphabet[4:2:-1])








































text = input("Введите строку: ")

first_h = text.index("h")
last_h = text.rindex("h")

reversed_text = text[first_h + 1: last_h][::-1]

print("Развёрнутая последовательность между первым и последним h:", reversed_text)








































num_lists = [[i + j * 4 for j in range(3)] for i in range(1, 5)]

print(num_lists)







































nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [num for sublist in nice_list for inner_list in sublist for num in inner_list]

print(new_list)







































def encrypt(text, shift):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    encrypted_text = ""

    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text


message = input("Введите сообщение: ")
K = int(input("Введите сдвиг: "))

encrypted_message = encrypt(message, K)

print(encrypted_message)








































text = "утиное филе;фланк-стейк;банановый пирог;плов"

menu_list = text.title().split(';')

print("На данный момент в меню есть:", ', '.join(menu_list))







































text = "aaAAbbсaaaA"
encoded = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        encoded += text[i - 1] + str(count)
        count = 1

encoded += text[-1] + str(count)  # Добавляем последний символ

print(encoded)







































def cyclic_shift(s1, s2):
    if len(s1) != len(s2):  # Если строки разной длины, сдвиг невозможен
        return "Первую строку нельзя получить из второй с помощью циклического сдвига."

    double_s2 = s2 + s2  # Создаём удвоенную строку для поиска подстроки
    shift = double_s2.find(s1)

    if shift != -1:
        return f"Первая строка получается из второй со сдвигом {shift}."
    else:
        return "Первую строку нельзя получить из второй с помощью циклического сдвига."

# Ввод данных
s1 = "abcd"
s2 = "cdab"

print(cyclic_shift(s1, s2))







































def check_ip(ip_address):
    split_ip_address = ip_address.split(".")
    if len(split_ip_address) == 4:
        for part_ip_address in split_ip_address:
            if not part_ip_address.isdigit():
                print(f'\tОшибка: {part_ip_address} не целое число.')
                break
            elif not int(part_ip_address) <= 255:
                print(f'\tОшибка: {part_ip_address} превышает 255.')
                break
        else:
            print('\tIP-адрес корректен')
            return ip_address
    else:
        print('Ошибка: адрес — это четыре числа, разделённые точками.')

def check_file_name(file_name):
    incorrect_endings = '.txt', '.docx'
    special_symbols = '@', '№', '$', '%', '^', '&', '*', '(', ')', '\\'

    if file_name.startswith(special_symbols):
        print('\tОшибка: название начинается на один из специальных символов')
    elif not file_name.endswith(incorrect_endings):
        print('\tОшибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('\tФайл назван верно.')
        return file_name

def maximum_length(text):
    text = text[0].split()
    return max(text, key=len)

data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
    ["192.c8.1.10", ["file_432.txt  &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
]

valid_info = []
for info in data:
    print(f"Проверяю ip {info[0]}")
    ip_address = check_ip(info[0])

    print(f"Ищу самый длинный файл для ip {info[0]}")
    maxi_length = maximum_length(info[1])

    print(f"\tЭто файл {maxi_length}. \nПроверяю корректность имени")
    file_name = check_file_name(maxi_length)

    if ip_address and file_name:
        valid_info.append([ip_address, info[1]])
    print("=" * 50)

print(f"Новая структура данных\n[")
for i in valid_info:
    print(f"\t{i}")
print("]")







































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








































films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

num_films = int(input("Сколько фильмов хотите добавить? ")) #Кол-во добавляемых фильмов
favorite_films = [] #Список любимых фильмов

for _ in range(num_films): #Добавляем нужное кол-во фильмов в наш список
    film = input("Введите название фильма: ")
    if film in films:
        favorite_films.append(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

print(f"Ваш список любимых фильмов: {favorite_films}") #Выводим наш список







































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







































def is_palindrome(text):
    for index in range(0, len(word)):
        if text[index] != text[len(word) - index - 1]:
            return False
    return True


word = input("Введите слово: ")

if is_palindrome(word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")








































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







































violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs = int(input("Сколько песен выбрать? ")) #Кол-во песен
my_songs = [] #Плейлист
total_time = 0 #Общее время плейлиста

for i_song in range(num_songs): #Цикл из кол-ва песен
    song_name = input(f"Название {i_song + 1} песни: ") #Вводим название песни
    for song in violator_songs: #Ищем нужную песню в списке
        if song[0] == song_name: #Если находим, то добавляем ее в наш плейлист и суммируем время
            total_time += song[1]
            my_songs.append(song)

print(f"Общее время звучания песен: {round(total_time, 2)} минуты") #Выводим общее время плейлиста








































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







































def is_palindrome(numbers): #Проверяем последовательность на симметрию
    return numbers == numbers[::-1]

def to_append(numbers): #Ищем наименьший индекс с которого последовательность является палиндромом
    i = 0
    while i < N:
        if is_palindrome(numbers[i:]):
            break
        i += 1
    return numbers[:i][::-1] #Сначала делаем срез [:i], а после переворачиваем список [::-1]


N = int(input("Кол-во чисел: ")) #Вводим кол-во чисел в последовательность
numbers = [] #Список последовательность

for _ in range(N): #Заполняем последовательность
    numbers.append(int(input("Число: ")))

print(f"Последовательность: {numbers}") #Выводим последовательность

if is_palindrome(numbers): #Проверяем последовательность на симметрию
    print("Последовательность симметрична") #Если симметрична, то ничего делать не надо
else:
    append_numbers = to_append(numbers) #Иначе вызываем функцию
    print(f"Нужно прописать чисел: {len(append_numbers)}")
    print(f"Сами числа: {append_numbers}")







































