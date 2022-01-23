# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. # Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import datetime as dt


class Date:
    date_str = ''

    def __init__(self, date_str):
        Date.date_str = date_str

    @classmethod
    def convert_to_int(cls):
        return list(int(c) for c in cls.date_str.split('-'))

    @staticmethod
    def check_valid(date_str):
        # вариант из коробки
        try:
            dt.datetime.strptime(date_str, '%d-%m-%Y')
        except Exception as N:
            print('Ошибка в формате данных:', N)
            return False

        return True


a = Date('14-06-1984')

print(Date.convert_to_int())

print(a.check_valid('30-06-1984'))
print(a.check_valid('31-09-1989'))
print(a.check_valid('31-19-1989'))
print(a.check_valid('31-01-2989'))
print(a.check_valid('31-01-222s'))
