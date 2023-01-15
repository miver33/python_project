a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))
c: int = int(input("введите третье число "))

is_inequality_1_true: bool = a < b < c
is_inequality_2_true: bool = a < b < c or c < b < a

print(f"равенство a<b<c справедливо: {is_inequality_1_true}")
print(f"число b находится между числами a и c: {is_inequality_2_true}")