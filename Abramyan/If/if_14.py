a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))
c: int = int(input("введите третьей число "))

if a < b < c:
    print(a,c)
elif a < c < b:
    print(a,b)
elif b < a < c:
    print(b,c)
elif b < c < a:
    print(b, a)
elif c < a < b:
    print(c,b)
elif c < b < a:
    print(c,a)

    