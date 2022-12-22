from math import sqrt, pow

#  ввод первой точки
x1: float = float(input("введите x1: "))
y1: float = float(input("введите y1: "))
#  ввод второй точки
x2: float = float(input("введите x2: "))
y2: float = float(input("введите y2: "))

distance: float = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f"расстояние {distance}")
