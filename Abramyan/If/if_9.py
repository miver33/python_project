a: float = float(input("enter first number "))
b: float = float(input("enter second number "))

if a < b:
    pass
elif a > b:
    tmp: float = a
    a = b
    b = tmp
else:
    a = 0
    b = 0

print(a, b)