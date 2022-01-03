# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


# Читаем из файла
with open('files_task_3/test.txt', 'r', encoding='utf-8') as f:
    staff = salary = summ_salary = 0

    for line in f:
        line_list = line.split('-')

        # здесь беру 1 часть с фио и вырезаю пробел в конце
        fio = line_list[0][:-1]
        salary = int(line_list[1])

        staff += 1
        summ_salary += salary

        if salary < 20_000:
            print(f'Оклад менее 20 тыс: {fio}')

print(f'Кол-во сотрудников: {staff}, средний доход: {summ_salary / staff}')
