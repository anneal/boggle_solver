""" This module includes a generic n-sided Die class. """

from random import randint

class Die():
    """ A Die may be initialized with a list of values for the sides.
        A value will be assigned with the roll() function.
        Attributes of a Die include:
            sides: list of possible side values
            value: the current instance value
            used: boolean used in traversing applications
            connections: list used in traversing applications
    """

    def __init__(self, sides = []):
        self.sides = sides[:]
        self.roll()
        self.used = False
        self.connections = []


    def roll(self):
        """ The roll() function randomly selects one of the sides."""
        if len(self.sides) > 1:
            self.value = self.sides[randint(0,len(self.sides)-1)]
        else:
            self.value = self.sides
