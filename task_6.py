# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
import re
from functools import reduce

my_dict = {}

# Получаем сумму
def get_sum(prev, curr):
    return int(prev) + int(curr)


# Чтение из файла и обработка
with open('files_task_6/test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_list = line.split(':')
        lesson_name = line_list[0]
        lessons_hours = re.sub('[^0-9 ]', '', line).split()
        lessons_hours = reduce(get_sum, lessons_hours)
        my_dict[lesson_name] = int(lessons_hours)

print(my_dict)
