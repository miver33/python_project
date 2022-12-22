from math import pow

print("введите  a")
a: float = float(input())
print("введите  b")
b: float = float(input())

# sum_of_squares: float = (a ** 2) + (b ** 2)
sum_of_squares: float = pow(a, 2) + pow(b, 2)
dif_of_squares: float = pow(a, 2) - pow(b, 2)
prod_of_squares: float = pow(a, 2) * pow(b, 2)
div_of_squares: float = pow(a, 2) / pow(b, 2)

sum_of_abs: float = abs(a) + abs(b)
abs_of_sum: float = abs(a + b)
dis_of_abs: float = abs(a) - abs(b)
prod_of_abs: float = abs(a) * abs(b)
div_of_abs: float = abs(a) / abs(b)
