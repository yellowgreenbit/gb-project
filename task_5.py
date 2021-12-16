# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

earnings = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

profit = earnings - costs

if profit > 0:
    print(f'Прибыль фирмы: {profit}. Вы молодец!')
    rent = profit / earnings
    print(f'Рентабельность: {rent}')
    personal_count = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль в расчете на каждого: {round(profit / personal_count, 2)}')
else:
    print(f'Убыток фирмы: {-profit}. Не повезло :(')

