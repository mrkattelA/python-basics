import random
from WeightedDie import WeightedDie

class WeightingDie(WeightedDie):
    "A Weighting Die"
    def __init__(self, sides = 6):
        """creates a die that favors sides it has previously rolled
        
        keyword arguments:
        sides (int) -- number of die sides.
        """
        self._weights = [1] * sides
        super().__init__(self._weights, sides)

    def roll(self):
        "Retrurn the value between 1 and number of sides"
        result = super().roll()
        self._weights[result - 1] += 1
        return result