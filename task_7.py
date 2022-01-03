# 7. Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json

sum_profit = 0
count_profit_firms = 0
firms_dict = {}

# Чтение из файла и обработка
with open('files_task_7/test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        profit = int(line_list[2]) - int(line_list[3])
        firms_dict[line_list[0]] = profit
        if profit > 0:
            count_profit_firms += 1
            sum_profit += profit

    firms_dict['average_profit'] = sum_profit / count_profit_firms

# Запись в файл
with open('files_task_7/result.json', 'w') as write_f:
    json.dump(firms_dict, write_f)
