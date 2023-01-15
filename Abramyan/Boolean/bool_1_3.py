a: int = int(input("введите число "))

is_a_positive: bool = a > 0
is_a_odd: bool = a % 2 == 1 # проверка на нечетность
is_a_even: bool = a % 2 == 0 # проверка на четность

print(f"a положительное: {is_a_positive}")
print(f"a а нечетное {is_a_odd}")
print(f"a чётное {is_a_even}")

