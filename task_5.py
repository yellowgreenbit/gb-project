# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [i for i in range(100, 1000, 2)]


def get_increase(prev_el, el):
    return prev_el * el


print(reduce(get_increase, my_list))
