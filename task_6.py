# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: Название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например Название, а значение — список значений-характеристик, например список названий товаров.

# products = [
#     (1, {"Название": "компьютер", "Цена": 20000, "Количество": 5, "Ед": "шт."}),
#     (2, {"Название": "принтер", "Цена": 6000, "Количество": 2, "Ед": "шт."}),
#     (3, {"Название": "сканер", "Цена": 2000, "Количество": 7, "Ед": "шт."})
# ]

products = []


# Зацикленный ввод, пока пользователь не введет что требуется
def loop_input(message, type_val):
    while True:
        input_val = input(message)
        if param_validate(input_val, type_val):
            return type_val(input_val)
        else:
            print('Параметр указан неправильно')


# Валидация параметров на тип
def param_validate(param, type_val):
    if type_val == int and param.isdigit():
        return True
    elif type_val == str and param.isalnum() and len(param) > 0:
        return True
    else:
        False


# Добавление продукта
def add_product(name, costs, count, unit_type):
    products.append(
        (
            len(products),
            {
                "Название": name,
                "Цена": costs,
                "Кол-во": count,
                "Ед.": unit_type
            }
        )
    )


# Соираем статистику
def get_statistic(prods):
    statistics = {}

    for product in prods:
        for key, val in product[1].items():
            if statistics.get(key):
                statistics[key].append(val)
            else:
                statistics[key] = [val]

    print(statistics)


while True:
    product_name = input('Введите Название товара (пустая строка - конец): ')

    if not product_name:
        print('Конец ввода')
        break
    else:
        product_costs = loop_input('Введите цену: ', int)
        product_count = loop_input('Введите количество: ', int)
        product_unit_type = loop_input('Введите ед. измерения: ', str)

        add_product(product_name, product_costs, product_count, product_unit_type)

get_statistic(products)

print(products)
