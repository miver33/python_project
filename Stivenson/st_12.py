from math import radians, sin, cos, acos

AVERAGE_EARTH_RADIUS = 6371.01

#  ввод первой точки
t1: float = float(input("введите t1: "))
g1: float = float(input("введите g1: "))
#  ввод второй точки
t2: float = float(input("введите t2: "))
g2: float = float(input("введите g2: "))

distance: float = AVERAGE_EARTH_RADIUS * acos(sin(radians(t1)) * sin(radians(t2)) + cos(radians(t1))
                                              * cos(radians(t2)) * cos(radians(g1) - radians(g2)))

print(f" дистанция = {distance:.1f}")
# Не работает arccos
