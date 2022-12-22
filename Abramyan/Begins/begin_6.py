print("введите сторону a")
side_a: float = float(input())
print("введите сторону b")
side_b: float = float(input())
print("введите сторону c")
side_c: float = float(input())

S: float = 2 * ((side_a * side_b) + (side_b * side_c) + (side_a * side_c))
V: float = side_a * side_b * side_c

print(f"площадь {S}")
print(f"Объём {V}")
