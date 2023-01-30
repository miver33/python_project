a: float = float(input("введите первое число "))
b: float = float(input("введите второе число "))
c: float = float(input("введите третьей число "))

a_b: float = abs(a - b)
a_c: float = abs(a - c)

if a_b > a_c:
    print(f"c({c}): {a_c}")
else:
    print(f"b({b}): {a_b}")

