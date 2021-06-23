class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            print('Первая клетка должна быть больше второй')

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, in_row):
        row = self.cell // in_row
        end_row = self.cell % in_row
        string = ''
        for i in range(row):
            string = f'{string}{"*" * in_row}/n'
        string = f'{string}{"*" * end_row}'
        return string

c1 = Cell(15)
c2 = Cell(7)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 // c2)
print(c2 // c1)
print(c1.make_order(5))



