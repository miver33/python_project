from math import sqrt, pow

#  ввод первой точки
x1: float = float(input("введите x1: "))
y1: float = float(input("введите y1: "))
#  ввод второй точки
x2: float = float(input("введите x2: "))
y2: float = float(input("введите y2: "))
# ввод 3 точки
x3: float = float(input("введите x3: "))
y3: float = float(input("введите y3: "))

a: float = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
b: float = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
c: float = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))
p: float = (a + b + c) / 2
s: float = sqrt(p * (p - a) * (p - b) * (p - c))

print(f"s = {s}")
# не уверен, что правильно.
