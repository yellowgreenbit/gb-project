# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
class Storage:
    def __init__(self, name, square, address):
        self.name = name
        self.square = square
        self.address = address
        self.storage_items = []

    def add_item(self, item, count):
        item['count'] = count
        self.storage_items.append(item)


class Orgteh:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Printer(Orgteh):
    def __init__(self, name, age):
        super().__init__(name, age)

    def do_print(self):
        print('Печатаю')


class Scaner(Orgteh):
    def __init__(self, name, age):
        super().__init__(name, age)

    def do_scan(self):
        print('Сканирую')


class Xserox(Orgteh):
    def __init__(self, name, age):
        super().__init__(name, age)

    def do_xser(self):
        print('Ксерю')


s = Storage('Склад оргтехники', 3000, 'г. Пермь, ул. Уральская 76')
p = Printer('Принтер', 2)
sc = Scaner('Сканер', 3)
x = Xserox('Керокс', 4)

print(s.__dict__)

print(p.__dict__)
print(sc.__dict__)
print(x.__dict__)

p.do_print()
sc.do_scan()
x.do_xser()

s.add_item(p.__dict__, 32)
s.add_item(sc.__dict__, 21)
s.add_item(x.__dict__, 18)

print(s.storage_items)


def do_valid(val, type):
    if type == 'str' and val.isalnum():
        return val

    if type == 'int' and val.isdigit():
        return int(val)

    return 'Ошибка формата данных'


while True:
    if input('Добавить товар на склад (n - нет, Enter - да) ?: ') == 'n':
        break

    name = do_valid(input('Введите название товара: '), 'str')
    age = do_valid(input('Введите дату производства: '), 'int')

    item = {
        'name': name,
        'age': age
    }

