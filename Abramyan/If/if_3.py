a: int = int(input("введите первое число "))

if a > 0:
    a = a + 1
else:
    if a == 0:
        a = 10
    else:
        a = a - 2

print(a)