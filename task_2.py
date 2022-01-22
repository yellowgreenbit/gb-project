# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def make_division(a, b):
    try:
        if b == 0:
            raise OwnError('На ноль нельзя делить!')

        c = a / b
    except Exception as e:
        print(f'Ошибка: {e}')
    else:
        print(f'Результат: {c}')
        return c


make_division(10, 0)
make_division(10, 'xs2')
