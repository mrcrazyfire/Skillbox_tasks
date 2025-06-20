## Цель домашнего задания
- Закрепить представление информации в Python в виде списка и отработать использование новых методов списка, чтобы уметь:
  - вставлять объект в конкретное место в списке;
  - определять индекс элемента в списке;
  - удалять элемент из списка;
  - расширять один список другим;
  - считать количество определённых элементов в списке.
- Отработать использование функций list и range для генерации списка.
- Отработать навык работы с элементами вложенных списков.
## Что входит в задание
1.	Видеокарты.
2.	Кино.
3.	Бегущие цифры.
4.	Анализ слова — 2.
5.	Сортировка.
6.	Уникальное объединение списков.
7.	Детали.
8.	Песни.
9.	Ролики.
10.	Считалка.
11.	Симметричная последовательность.

## Задача 1. Видеокарты.
### Что нужно сделать
В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий хранятся только числа, которые обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт. Самые старшие поколения разобрали за пару дней.

Напишите программу, которая удаляет списка видеокарт наибольшие элементы.

**Пример:**

```bash
Количество видеокарт: 5
1 Видеокарта: 3070
2 Видеокарта: 2060
3 Видеокарта: 3090
4 Видеокарта: 3070
5 Видеокарта: 3090

Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
Новый список видеокарт: [ 3070 2060 3070 ]
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).


## Задача 2. Кино
### Что нужно сделать
Илья зашёл на любительский киносайт, на котором пользователи оставляют рецензии на фильмы. Их список:

```python
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
```

Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить часть фильмов в список любимых, чтобы позже прочитать рецензии на них.

Напишите программу, в которой пользователь вводит фильм. Если он есть в перечне, то добавляется в список любимых. Если его нет, то выводится ошибка. В конце выведите весь список любимых фильмов.

**Пример:**

```
Сколько фильмов хотите добавить? 3
Введите название фильма: Леон
Введите название фильма: Безумный Макс
Ошибка: фильма Безумный Макс у нас нет :(
Введите название фильма: Мементо
Ваш список любимых фильмов: Леон, Мементо
```
### Ваш список любимых фильмов: Леон, Мементо
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).


## Задача 3. Бегущие цифры
### Что нужно сделать
Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа. Например, как в метро, автобусах или трамваях.

Даны список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций. Используйте минимально возможное количество операций присваивания.

**Пример 1:**

```
Сдвиг: 1
Изначальный список: [1, 2, 3, 4, 5]
Сдвинутый список: [5, 1, 2, 3, 4]
```

**Пример 2:**

```
Сдвиг: 3
Изначальный список: [1, 4, -3, 0, 10]
Сдвинутый список: [-3, 0, 10, 1, 4]
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).


## Задача 4. Анализ слова 2
### Что нужно сделать
Продолжите писать анализаторы для текста. Теперь необходимо реализовать код, с помощью которого можно определять палиндромы. То есть нужно находить слова, которые одинаково читается слева направо и справа налево. 

Напишите такую программу.

**Пример 1:**

```
Введите слово: мадам

Слово является палиндромом
```

**Пример 2:**

```
Введите слово: abccba

Слово является палиндромом
```

**Пример 3:**

```
Введите слово: abbd

Слово не является палиндромом
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 5. Сортировка
### Что нужно сделать
Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран. Дополнительный список **использовать нельзя**.

Также нельзя использовать готовые функции `sorted`/`min`/`max` и метод `sort`.

Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

**Пример:**

```
Изначальный список: [1, 4, -3, 0, 10]

Отсортированный список: [-3, 0, 1, 4, 10]
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 6. Уникальное объединение списков
### Контекст
Вы работаете в команде разработки программного обеспечения для компании, которая занимается обработкой и анализом данных. Ваша команда получает данные из различных источников, вам нужно объединить их в один отсортированный список для дальнейшей обработки. Однако источники данных возвращают отсортированные списки с возможными дубликатами, и ваша задача — создать программу, которая объединит эти списки в один отсортированный список без дубликатов.

### Задача
Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный список без дубликатов.

### Пример:
```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
```
### Вывод в консоли:
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
### Советы
- Учтите, что один список может быть короче другого.
- Проверьте ваше решение с различными тестовыми данными, включая случаи с пустыми списками, списками без дубликатов и списками с 
  повторяющимися элементами.
- Требование отсутствия дубликатов значительно усложняет задачу. Убедитесь, что в вашем итоговом списке дубликатов не будет.





## Задача 7. Детали
### Что нужно сделать
В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:

```python
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
```

Продавец решил, что считать количество и стоимость деталей вручную не очень удобно, поэтому решил попросить помощи у программиста, чтобы оптимизировать этот процесс.

Напишите программу, которая запрашивает у пользователя деталь, считает их количество, а также общую стоимость.

Пример:

```
Название детали: седло
Кол-во деталей — 3  
Общая стоимость — 4500
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 8. Песни
### Что нужно сделать
Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode. Каждая песня состоит из названия и продолжительности с точностью до долей минут:

```python
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
```

Из этого списка Ваня хочет выбрать N песен и добавить их в особый плейлист с другими треками. И при этом ему важно, сколько времени в сумме эти N песен будут звучать.

Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен, а на экран выводит общее время их звучания.

Пример:

```
Сколько песен выбрать? 3
Название 1-й песни: Halo
Название 2-й песни: Enjoy the Silence
Название 3-й песни: Clean

Общее время звучания песен: 14.93 минуты
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).


## Задача 9. Ролики
### Что нужно сделать
Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики только своего размера.

Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей. Реализуйте код, который определяет, какое наибольшее число человек может одновременно взять ролики и пойти кататься.
Пример:

```
Кол-во коньков: 4
Размер 1-й пары: 41
Размер 2-й пары: 40
Размер 3-й пары: 39
Размер 4-й пары: 42

Кол-во людей: 3
Размер ноги 1-го человека: 42
Размер ноги 2-го человека: 41
Размер ноги 3-го человека: 42

Наибольшее кол-во людей, которые могут взять ролики: 2
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

### Советы и рекомендации
- Помните, по условиям задачи размер роликов должен быть равен размеру ноги.
- Чтобы подобрать максимальное количество пар, старайтесь найти наименьший возможный размер роликов для каждого размера ноги. 

## Задача 10. Считалка
### Что нужно сделать
N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание, где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.

На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это номер человека, который останется в кругу последним.

Пример:

```
Кол-во человек: 5
Какое число в считалке? 7
Значит, выбывает каждый 7-й человек

Текущий круг людей: [1, 2, 3, 4, 5]
Начало счёта с номера 1
Выбывает человек под номером 2

Текущий круг людей: [1, 3, 4, 5]
Начало счёта с номера 3
Выбывает человек под номером 5

Текущий круг людей: [1, 3, 4]
Начало счёта с номера 1
Выбывает человек под номером 1

Текущий круг людей: [3, 4]
Начало счёта с номера 3
Выбывает человек под номером 3

Остался человек под номером 4
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

### Советы и рекомендации
- Чтобы индекс не вышел за пределы списка, нужно ограничить его рост. Для этого подходит операция %: (индекс + число) % длина списка. Так индекс не будет равен длине списка или не превысит её, а значит не выйдет за пределы списка.

## Задача 11. Симметричная последовательность
### Что нужно сделать
Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево. Например, следующие последовательности являются симметричными:

```
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
```

Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет, какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.

Пример 1:

```
Кол-во чисел: 5
Число: 1
Число: 2
Число: 1
Число: 2
Число: 2

Последовательность: [1, 2, 1, 2, 2]
Нужно приписать чисел: 3
Сами числа: [1, 2, 1]
```

Пример 2:

```
Кол-во чисел: 5
Число: 1
Число: 2
Число: 3
Число: 4
Число: 5

Последовательность: [1, 2, 3, 4, 5]
Нужно приписать чисел: 4
Сами числа: [4, 3, 2, 1]
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

### Советы и рекомендации
- Убедитесь что ваш алгоритм работает с разными последовательностями.  
   Например, с такими:
    ```
    [1, 2, 1] — в этом случае ничего добавлять не нужно.
    [1, 2, 3, 4, 3] — в этом случае надо добавить минимум, то есть числа 2 и 1.
    ```
  

## Что оценивается в домашнем задании
- Практическая работа сдана через GitLab.
- Структура папок и файлов репозитория соответствует репозиторию python_basic.
- Все задачи выполнены в соответствующих папках и файлах `main.py`.
- Описания коммитов осмысленны и понятны: `111`, `done`, `«я сделалъ»` — неверно; `added m15 homework`, `14.3 fix: variables naming` — верно.
- Использованы именованные индексы, не просто `i` (подробнее в видео 7.2).
- Использованы правильные числа, без дополнительных действий со стороны пользователя, без `+1` (подробнее об этом в видео 7.4).
- Правильно оформлен `input`, без пустого приветствия для ввода (подробнее об этом в видео 2.3).
- Переменные и функции имеют значащие имена, не только `a`, `b`, `c`, `d` (подробнее об этом в видео 2.3).
- Есть пробелы после запятых и при бинарных операциях.
- Нет пробелов после имён функций и перед скобками: `print ()`, `input ()` — неверно; `print()` — верно.
- Правильно оформлены блоки `if-elif-else`, циклы и функции; отступы одинаковы во всех блоках одного уровня.

## Советы и рекомендации
- Арифметические операции [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) остаются в приоритете. Необходимо вводить and, or.
- Руководство по стилю Python [PEP8](https://www.python.org/dev/peps/pep-0008/) на английском языке.
- Руководство по стилю Python [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html) на русском языке.
- [Список встроенных функций](https://docs.python.org/3.7/library/functions.html).

## Как отправить задание на проверку
Чтобы выполнить домашнее задание, обновите репозиторий python_basic на своём компьютере при помощи IDE PyCharm. Задачи находятся в папке Module16.

Сдайте домашние работы этого модуля через систему контроля версий Git сервиса Skillbox Gitlab. В уроке с домашним заданием напишите «Сделано» и прикрепите ссылку на репозиторий. Ссылки на реплит оставлять не нужно.

