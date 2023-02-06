x1: int = int(input("введите исходный x "))
y1: int = int(input("введите исходный y "))
x2: int = int(input("введите конечный x "))
y2: int = int(input("введите конечный y "))
if x1 == x2 and y1 == y2:
    print("ферзь не двигается")
elif (x1 == x2 or y1 == y2) or (abs(x1 - x2) == abs(y1 - y2)):
    print("ферзь будет двигаться")
else:
    print("ферзь не будет двигаться")