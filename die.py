from random import randint

class die():

    def roll(self):
        self.value = self.sides[randint(0,5)]

    def __init__(self, sides):
        self.used = False
        self.sides = sides[:]
        self.connections = []
        self.roll()
