# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость машины: {self.speed}')

    def go(self):
        print('Машина поехала')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print('Машина остановилась')
        self.show_speed()

    def turn(self, direction):
        print(f'Машина повернула {direction}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость машины: {self.speed}{". Превышение скорости!" if self.speed > 60 else ""}')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость машины: {self.speed}{". Превышение скорости!" if self.speed > 40 else ""}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


tcar = TownCar(speed=70, color='red', name='Лада')
tcar.go()
tcar.turn(direction='направо')
tcar.turn(direction='налево')
tcar.stop()
print(tcar.is_police)

pcar = PoliceCar(speed=80, color='red', name='Нива')
pcar.go()
pcar.turn(direction='направо')
pcar.turn(direction='налево')
pcar.stop()
print(pcar.is_police)
print(pcar.ar)