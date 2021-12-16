# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = input('Введите целое число: ')
index = 0
max_num = 0

while index < len(num):
    str_num = int(num[index])
    if max_num < str_num:
        max_num = str_num
    index += 1

print(f'Максимальное число: {max_num}')
