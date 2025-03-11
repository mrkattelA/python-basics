import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    # add a roll() method

    def roll(self):
        r = random.randint(1, self.sides)
        return r