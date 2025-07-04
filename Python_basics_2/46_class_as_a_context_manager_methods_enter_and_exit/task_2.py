class Example:
    def __init__(self):
        print("Вызов __init__")

    def __enter__(self):
        print("Вызов __enter__")
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызов __exit__")
        if exc_type:
            print(f"Тип ошибки: {exc_type}")
            print(f"Значение ошибки: {exc_val}")
            print(f'"След" ошибки: {exc_tb}')
            return True


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')