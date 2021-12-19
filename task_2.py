# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
import random

numbers = []

# вводим числа
# числа четные / нечетные - случайное от 3 до 6
for i in range(random.randint(3, 6)):
    num = int(input(f'Введите число {i + 1}: '))
    numbers.append(num)

for key, n in enumerate(numbers):
    if key % 2:
        numbers[key], numbers[key - 1] = numbers[key - 1], n

print(numbers)

