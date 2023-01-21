a: float = float(input("enter first number "))
b: float = float(input("enter second number "))

if a < b:
    print(a , b)
elif a == b:
    print(0 , 0)
else:
    print(a  , b + a)