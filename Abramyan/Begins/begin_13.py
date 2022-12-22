PI = 3.14

r1: float = float(input("enter r1"))
r2: float = float(input("enter r2"))

s1: float = PI * (r1 ** 2)
s2: float = PI * (r2 ** 2)
s3: float = s1 - s2

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")
