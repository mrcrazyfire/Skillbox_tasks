## Задача 2. Сжатие
Из-за увеличения объёма данных понадобилось сжать их, но так, чтобы не потерять важную информацию. Для этого было придумано специальное кодирование: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'. То есть группы одинаковых символов исходной строки заменяются на эти символы и количество их повторений в строке.

Напишите программу, которая считывает строку, кодирует её, используя предложенный алгоритм, и выводит закодированную последовательность на экран. Код должен учитывать регистр символов.

Пример:
```
Введите строку: aaAAbbсaaaA
Закодированная строка: a2A2b2с1a3A1
```