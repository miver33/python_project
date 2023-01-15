a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))
c: int = int(input("введите третьей число "))

is_a_and_b_and_c_positive: bool = (a > 0) and (b > 0) and (c > 0)
is_a_or_b_or_c_positive: bool = (a > 0) or (b > 0) or (c > 0)


print(f"все числа положительные {is_a_and_b_and_c_positive}")
print(f"хотя бы одно из чисел положительное {is_a_or_b_or_c_positive}")

#bool 14-15 не понял как сделать