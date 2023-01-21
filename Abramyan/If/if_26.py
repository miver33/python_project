x: float = float(input("enter the number "))

if x < 0:
    result: float = -x
else:
    if 0 < x and x < 2:
        result = x ** 2
    else:
        result = 4

print(result)
