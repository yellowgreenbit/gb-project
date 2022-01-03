# 4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_nums = ['один', 'два', 'три', 'четыре']


def get_str(index):
    return f'{rus_nums[index - 1]} — {index}\n'


with open('files_task_4/test_2.txt', 'w', encoding='utf-8') as f_2:
    with open('files_task_4/test_1.txt', 'r', encoding='utf-8') as f_1:
        for line in f_1:
            line_num = int(line.split()[-1])
            f_2.write(get_str(line_num))
