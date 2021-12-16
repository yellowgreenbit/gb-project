# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

st = 'Артёмка уехал в Лондон'
fl = 0.5
num = 11
bln = False
nobody = None

print(st, type(st))
print(fl, type(fl))
print(num, type(num))
print(bln, type(bln))
print(nobody, type(nobody))

name = input('Как Вас зовут:')
cat_age = input('Сколько лет вашему коту: ')

print(f'Вас зовут {name}. У вас есть кот, ему {cat_age} года (лет)')
