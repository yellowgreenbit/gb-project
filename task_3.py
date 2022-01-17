import math


class Ceil:

    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        size = math.floor(self.size + other.size)
        return Ceil(size)

    def __sub__(self, other):

        sub_result = math.floor(self.size - other.size)

        if sub_result < 0:
            print('Клетка 1 занимает меньше ячеек 2')
        else:
            return Ceil(sub_result)

    def __mul__(self, other):
        size = math.floor(self.size * other.size)
        return Ceil(size)

    def __truediv__(self, other):
        size = math.floor(self.size / other.size)
        return Ceil(size)

    def __str__(self):
        return str(self.size)

    def make_order(self, nums):
        print(('*' * nums + '\n') * (self.size // nums) + '*' * (self.size % nums))


first = Ceil(30)

second = Ceil(20)

print(first - second)
print(first + second)
print(first * second)
print(first / second)

first.make_order(8)
