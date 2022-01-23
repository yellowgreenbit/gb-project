# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

lst = []


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_item(i):
    try:
        if i.isdigit():
            return i
        else:
            raise OwnError('Тип данных не число')
    except Exception as e:
        print(f'Ошибка: {e}')


def add_items(item):
    if check_item(item):
        lst.append(item)


while True:
    user_int = input('Введите число (пустая строка - конец ввода): ')
    if user_int:
        add_items(user_int)
    else:
        break

print(lst)
