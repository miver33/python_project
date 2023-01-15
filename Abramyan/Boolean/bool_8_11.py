a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))

is_a_and_b_odd: bool = (a and b) % 2 == 1
is_a_or_b_odd: bool = (a or b) % 2 == 1
# тут вроде бы нужно исключающее или, мы его не проходили
is_a_than_b_odd: bool = (a % 2 == 1) == (b % 2 == 1)


print(f"a и b нечётные: {is_a_and_b_odd}")
print(f"a или b нечётные: {is_a_or_b_odd}")
print(f"a и b имеют одинаковую чётность: {is_a_than_b_odd}")
