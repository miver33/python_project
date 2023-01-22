x: float = float(input("введите первую координату "))
y: float = float(input("введите вторую координату "))

if x > 0 and y > 0:
    print("точка находится в 1 четверти")
elif x < 0 and y > 0:
    print("точка находится в 2 четверти")
elif x < 0 and y < 0:
    print("точка находится в 3 четверти")
elif x > 0 and y < 0:
    print("точка находится в 4 четверти")

