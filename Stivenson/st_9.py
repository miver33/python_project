PROC = 0.04

num: float = float(input("введите число"))

first_year: float = num + num * PROC
second_year: float = first_year * PROC + first_year
third_year: float = second_year * PROC + second_year

print(f"first year = {first_year}")
print(f"second year = {second_year}")
print(f"fird year = {third_year}")
