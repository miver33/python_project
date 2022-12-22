from math import sqrt

a: float = float(input("enter a"))
b: float = float(input("enter b"))

c: float = sqrt((a + b))
p: float = a + b + c

print(f"c = {c}")
print(f"p = {p}")
