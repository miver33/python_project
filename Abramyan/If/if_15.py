a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))
c: int = int(input("введите третьей число "))

if a < b < c:
    print(b + c)
elif a < c < b:
    print(c + b)
elif b < a < c:
    print(a + c)
elif b < c < a:
    print(c + a)
elif c < a < b:
    print(a + b)
elif c < b < a:
    print(b + a)
