"""Вложенные словари и значения по умолчанию в get"""


#Задача 1. Заказ фруктов
def order_fruits():
    order = {'apple': 2,
             'banana': 3,
             'pear': 1,
             'watermelon': 10,
             'chocolate': 5
    }

    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'grapefruit': 300.40,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }

    result = 0
    for product in order:
        price = incomes.get(product, 0)
        result += price * order[product]

    print(result)


#Задача 2. Игроки
def players():
    players_dict = {
        1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
        2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
        3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
        4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
        5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
        6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
        7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
        8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
    }

    # Все члены команды A, которые отдыхают
    team_a_resting = [player['name'] for player in players_dict.values() if
                      player['team'] == 'A' and player['status'] == 'Rest']
    print("Отдыхающие члены команды A:", team_a_resting)

    # Все члены команды B, которые тренируются
    team_b_training = [player['name'] for player in players_dict.values() if
                       player['team'] == 'B' and player['status'] == 'Training']
    print("Тренирующиеся члены команды B:", team_b_training)

    # Все члены команды C, которые путешествуют
    team_c_traveling = [player['name'] for player in players_dict.values() if
                        player['team'] == 'C' and player['status'] == 'Travel']
    print("Путешествующие члены команды C:", team_c_traveling)
