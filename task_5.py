# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

sum_num = 0
spec_char = 'n'


def get_list_nums(user_string):  # Функция, возвращающая спикок интов из строки
    try:
        return [int(n) for n in user_string.split()]
    except Exception as e:
        return e


while True:
    user_str = input(f'Введите строку числел, разделенных пробелом ({spec_char} - выход): ')

    if user_str == spec_char:
        print('Выход')
        break
    elif user_str.count(spec_char):
        user_str = user_str.split(spec_char)[0]
        sum_num += sum(get_list_nums(user_str))
        print(f'Сумма чисел: {sum_num} ... Выход')
        break
    else:
        num_list = get_list_nums(user_str)
        if isinstance(num_list, Exception):
            print('Ошибка: ', num_list)
            continue

        sum_num += sum(get_list_nums(user_str))

    print(f'Сумма чисел: {sum_num}')
