x1: int = int(input("введите исходный x "))
y1: int = int(input("введите исходный y "))
x2: int = int(input("введите конечный x "))
y2: int = int(input("введите конечный y "))


if x1 == x2 and y1 == y2:
    print("конь не двигается")
elif abs(x1 - x2) + abs(y1 - y2) == 3 and (x1 != x2 and y1 != y2):
    print("конь будет двигаться")
else:
    print("конь не будет двигаться")
