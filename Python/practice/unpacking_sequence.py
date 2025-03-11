import math

def distance_of_point(p, b):
    return math.sqrt(p**2 + b**2)

point = (3,4)

#distance = distance_of_point(point) Incorrect due to missing 1 more arguments.
distance = distance_of_point(*point) # * Helps to unpack the Sequences.
print(distance)