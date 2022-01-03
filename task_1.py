# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# Функция открытия файла и опросника юзера
def my_func(clb):
    with open('files_task_1/test.txt', 'w', encoding='utf-8') as f:
        user_str = None
        while user_str or not isinstance(user_str, str):
            user_str = input('Введите данные: ')
            clb(user_str, f)

        print('Конец ввода')


# Вариант 1 write
def do_single_write(user_str, f):
    f.write(user_str + '\n')


my_func(do_single_write)


# Вариант 2 writelines
user_str_list = []


def collect_list(user_str, f):
    user_str_list.append(user_str + '\n')
    if not user_str:
        f.writelines(user_str_list)


my_func(collect_list)
