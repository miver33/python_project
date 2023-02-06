x1: int = int(input("введите исходный x "))
y1: int = int(input("введите исходный y "))
x2: int = int(input("введите конечный x "))
y2: int = int(input("введите конечный y "))

if x1 == x2 and y1 == y2:
    print("фигура не двигается")
elif (x1 - 1 <= x2 <= x1 + 1) and (y1 - 1 <= y2 <= y1 + 1):
    print("король сможет сходить")
else:
    print("король не может ходить")

