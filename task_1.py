# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

def add(x, y):
    return x + y


album = [
    'Blackout',  # строка
    2020,  # целое число
    -4.53,  # вещественное число
    complex(10, 5),
    ['Scar', 'The Dawn', 'Ravens in the Sky'],
    None,
    b'music',
    {'Unspoken', 'Tension', 'Holy Ground'},
    (4.57, 4.17, 3.50),
    {
        'band': 'Dance With the Dead',
        'members': ['Justin Pointer', 'Tony Kim']
    },
    True,
    add,
    Exception
]

for element in album:
    print(element, type(element))
