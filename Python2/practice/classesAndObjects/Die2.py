import random

class Die:
    "A Die"
    def __init__(self, sides = 6):
        """creates a new standard die
        
        keyword arguments: 
                sides (init) -- number of die sides."""
        if type(sides) != int or sides < 1:
            raise Exception('sides must be a positive integer')
        self._sides = sides
        self._rolls = []

    @property
    def rolls(self):
        "history of rolls"
        return self._rolls
    
    def roll(self):
        "Returns the value between 1 and number of sides"
        roll = random.randint(1, self._sides)
        self._rolls.append(roll)
        return roll