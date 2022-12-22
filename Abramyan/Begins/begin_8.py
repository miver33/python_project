# math - пакет(модуль) с математическими функциями
from math import sqrt  # достали из модуля math функцию sqrt

print("введите  a")
a: float = float(input())
print("введите  b")
b: float = float(input())

# mean: float = (a * b) ** 0.5
mean: float = sqrt(a * b)

print(f"среднее арифметическое {mean}")
