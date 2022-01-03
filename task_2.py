# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
from random import randrange, choice
import string


# Про создание файла непрограммное написано, а про сохранение нескольких строк нет)
# Функция генерации случайного контента
def generate_content():
    result = ''
    count = randrange(30)
    for i in range(count):
        result += choice(string.ascii_letters + ' ' * 5)

    return result + '\n'


# Дозапись в файл
with open('files_task_2/test.txt', 'a', encoding='utf-8') as f:
    count = randrange(3, 6)
    for i in range(count):
        f.write(generate_content())


# Функция подсчета контента файла
def calculate_content():
    with open('files_task_2/test.txt', 'r', encoding='utf-8') as f:
        lines_count = words_count = chars_count = 0

        for line in f:
            lines_count += 1
            chars_count += len(line)
            words_count += len(line.split())
            # print(line.replace('\n', ''))

        print(f'Строк: {lines_count}, символов: {chars_count}, слов: {words_count}')


calculate_content()
