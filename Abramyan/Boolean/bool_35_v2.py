x1: int = int(input("введите первое число "))
y1: int = int(input("введите второе число "))
x2: int = int(input("введите третье число "))
y2: int = int(input("введите четвёртое число "))

first_cell_is_white: bool = (x1 + y1) % 2 == 1
second_cell_is_white: bool = (x2 + y2) % 2 == 1

if first_cell_is_white == second_cell_is_white:
    print("клетки имеют одинаковый цвет")
else:
    print("клетки имеют разный цвет")