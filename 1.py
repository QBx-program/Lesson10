class Matrix:

    def __init__(self, *args):
        self.matrix = []
        for val in args:
            self.matrix.append(val)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            print('Сложение матриц разных размерностей не возможно')
        else:
            new_matrix = []
            new_value = []
            for n in range(len(self.matrix)):
                new_matrix.append([])
                if len(self.matrix[n]) != len(other.matrix[n]):
                    raise print('Сложение матриц разных размерностей не возможно')
                else:
                    for i in range(len(self.matrix) - 1):
                        a = self.matrix[n][i] + other.matrix[n][i]
                        new_value.append(a)
                    new_matrix[n] = new_value
                    new_value = []
        return f'Новая матрица: {new_matrix}'


    def __repr__(self):
        return f'{self.matrix}'


a1 = Matrix([31, 22], [37, 43], [51, 86])
a2 = Matrix([9, 8], [3, 7], [9, 4])

print(a1)
print(a2)
print(a1+a2)


