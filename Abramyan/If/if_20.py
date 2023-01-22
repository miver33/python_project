a: float = float(input("введите первое число "))
b: float = float(input("введите второе число "))
c: float = float(input("введите третьей число "))

b_bigger_than_a: float = b - a
a_bigger_than_a: float = a - b
c_bigger_than_a: float = c - a
a_bigger_than_a: float = a - c


if a < b < c:
    print(f"ближайшая точка b = {b_bigger_than_a}")
elif c < b < a:
    print(f"ближайшая точка b = {a_bigger_than_a}")
elif a < c < b:
    print(f"ближайшая точка c = {c_bigger_than_a}")
elif b < c < a:
    print(f"ближайшая точка c = {a_bigger_than_a}")
