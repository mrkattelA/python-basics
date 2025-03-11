from collections import Counter
c = Counter(['green', 'blue', 'blue', 'red', 'yellow', 'green', 'blue'])
print(c)
print('Colors Counter:', c, sep='\n', end='\n\n')
#Counter({'blue': 3, 'green': 2, 'red': 1, 'yellow': 1}) VALUE OF C

c.update(["green","black","red"])
print(c)
# NEW VALUE OF C AFTER UPDATE Counter({'green': 3, 'blue': 3, 'red': 2, 'yellow': 1, 'black': 1})

c.subtract(["yellow", "green"])
print(c)
#NEW VALUE OF C AFTER SUBTRACT Counter({'blue': 3, 'green': 2, 'red': 2, 'black': 1, 'yellow': 0})
print(c.most_common())
#value of most common [('blue', 3), ('green', 2), ('red', 2), ('black', 1), ('yellow', 0)]
