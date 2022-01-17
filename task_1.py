from random import randint


class Matrix:

    def __init__(self, data):
        self.matrix_data = data

    def __str__(self):
        # вывод матрицы в привычном виде
        s = ''
        for i in range(len(self.matrix_data)):
            for k in self.matrix_data[i]:
                s += str(k) + '    '
            s += '\n'

        return s

    def __add__(self, other):
        # сложение матриц
        new_matrix = []
        for i in range(len(self.matrix_data)):
            new_matrix.append([])
            for r, k in enumerate(self.matrix_data[i]):
                new_matrix[i].append(k + other.matrix_data[i][r])

        return new_matrix


# генерация матриц
def generate_dataset(width, height):
    dataset = []
    for i in range(width):
        dataset.append([])
        for k in range(height):
            dataset[i].append(randint(1, 9))

    return dataset


m1 = Matrix(generate_dataset(3, 3))
print(m1.matrix_data)
print(str(m1))

m2 = Matrix(generate_dataset(3, 3))
print(m2.matrix_data)
print(str(m2))

print(m1 + m2)
