a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))
c: int = int(input("введите третьей число "))

if a < b and a < c or a < c < b:
    print(a)
elif b < a < c or b < c < a:
    print(b)
elif c < a < b or c < b < a:
    print(c)
# капец она мне голову немного поломала 