class Hands:

    def __init__(self, hand, size):
        self.hand = hand
        self.size = size
        self.coth = 0

    def __repr__(self):
        return f'Одежда: {self.hand} размер: {self.size} расход ткани: {self.coth}'

class Coat(Hands):

    def __init__(self, hand, size):
        self.hand = hand
        self.size = size
        self.coth = size * 10 / 65 +0.5

class Suit(Hands):

    def __init__(self, hand, size):
        self.hand = hand
        self.size = size
        self.coth = size * 2 + 0.3

h1 = Coat('Пальто', 20)
s1 = Suit('Костюм', 10)

print(h1)
print(s1)
