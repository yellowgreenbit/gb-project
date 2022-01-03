# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randrange
from functools import reduce


# Функция генерации случайного контента
def generate_content():
    return (str(randrange(10)) + ' ' for i in range(10))


def get_sum(prev, curr):
    return int(prev) + int(curr)


# запись в файл
with open('files_task_5/test.txt', 'w', encoding='utf-8') as f:
    f.writelines(generate_content())


# чтение из файла
with open('files_task_5/test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f'Список элементов: {line.split()}')
        print(f'Сумма чисел: {reduce(get_sum, line.split())}')
