# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

index_month = 0

while True:
    month = input('Введите номер месяца: ')

    if not(month.isdigit()):
        print('Номер месяца должен быть числом')
    elif int(month) not in range(1, 13):
        print('Номер месяца должен быть числом от 1 до 12')
    else:
        index_month = int(month)
        break

# 1. решение через 1 список
seasons_list = ['зима', [12, 1, 2], 'весна', [3, 4, 5], 'лето', [6, 7, 8], 'осень', [9, 10, 11]]
seasons_list_count = 1
while True:
    if index_month in seasons_list[seasons_list_count]:
        print(f'На улице {seasons_list[seasons_list_count-1]}')
        break
    seasons_list_count += 2

# 2. решение через 2 cписка
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_list_nums = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# получаем индекс месяца в списке
month_index = seasons_list_nums.index(index_month) // 3
print(f'На улице {seasons_list[month_index]}')

# 3. решение через словарь
seasons = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

for season, nums_seasons in seasons.items():
    if index_month in nums_seasons:
        print(f'На улице {season}')
        break
