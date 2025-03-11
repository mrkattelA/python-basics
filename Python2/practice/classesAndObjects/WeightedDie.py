import random
from Die2 import Die

class WeightedDie(Die):
    "A weighted Die"
    def __init__(self, weights, sides= 6):
        """creates a new weighted die
        
        keyword arguments:
        sides(int) -- number of die sides
        weights(list) -- a list of integers holding the weights
                        for each die side
        """
        if len(weights) != sides:
            raise Exception(f"weights must be a list of length {sides}.")
        super().__init__(sides)
        self._weights = weights

    def roll(self):
        """Returns the value form 1 and number of sides"""
        options = []
        for i in range(self._sides):
            for j in range(self._weights[i]):
                options.append(i + 1)
        roll = random.choice(options)
        self._rolls.append(roll)
        return roll