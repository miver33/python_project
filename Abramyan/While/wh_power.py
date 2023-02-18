base: float = float(input("введите основание "))
exp: int = int(input("введите показатель степени "))

prod: float = 1
i: int = 1
while i <= exp:
    prod = prod * base

    i = i + 1

print(prod)