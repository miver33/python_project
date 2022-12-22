print("введите сторону a")
side_a: float = float(input())
print("введите сторону b")
side_b: float = float(input())

s: float = side_a * side_b
p: float = (2 * (side_b + side_a))

print(f"площадь {s}")
print(f"периметр {p}")
