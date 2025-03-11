from collections import Counter

class NonNegativeCounter(Counter):
    "counter that disallows the negative value"
    def __setitem__(self, key, value):
        value = 0 if value < 0 else value
        return super().__setitem__(key, value)