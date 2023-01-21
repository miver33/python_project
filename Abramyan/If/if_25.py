x: int = int(input("enter the number "))

if x < -2 or x > 2:
    result: int = 2 * x
else:
    result: int = -3 * x

print(result)