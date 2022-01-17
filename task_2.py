from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def count_material(self):
        pass


class Coat(Clothes):

    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def count_material(self):
        return self.v / 6.5 + 0.5

    def __add__(self, other):
        return self.count_material + other.count_material


class Costume(Clothes):

    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def count_material(self):
        return self.h * 2 + 0.3

    def __add__(self, other):
        return self.count_material + other.count_material


palto = Coat('пальто', 13)
print(palto.count_material)

maskarad = Costume('маскарадный костюм', 10)
print(maskarad.count_material)

print(palto + maskarad)
