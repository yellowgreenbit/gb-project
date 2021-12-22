# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def make_division(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    except Exception as e:
        return f'Ошибка ввода данных: {e}'


x = input('Введите первое число: ')
y = input('Введите второе число: ')

print(make_division(x, y))
