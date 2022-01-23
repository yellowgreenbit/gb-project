# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from task_4_5 import s


def param_validate(val, type):
    if type == 'str' and val.isalnum():
        return val

    if type == 'int' and val.isdigit():
        return int(val)

    return False


# Зацикленный ввод, пока пользователь не введет что требуется
def loop_input(message, type_val):
    while True:
        input_val = input(message)

        val = param_validate(input_val, type_val)
        if val:
            return val
        else:
            if val == False:
                print('Параметр указан неправильно')
            elif val == '':
                print('Параметр обязателен для заполения')


while True:
    if input('Добавить товар на склад (n - нет, Enter - да) ?: ') == 'n':
        break

    name = loop_input('Введите название товара: ', 'str')
    age = loop_input('Введите дату производства: ', 'int')
    count = loop_input('Введите кол-во: ', 'int')

    item = {
        'name': name,
        'age': age
    }

    s.add_item(item, count)

print(f'Товары на складе: {s.storage_items}')
