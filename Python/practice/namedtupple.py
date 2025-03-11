from collections import namedtuple

Point = namedtuple("Point", "x, y")

target_pos = Point(100, 200)

print(target_pos.x)
print(target_pos.y)
print(target_pos)
print(Point)