x1: int = int(input("введите первое число "))
y1: int = int(input("введите второе число "))
x2: int = int(input("введите третье число "))
y2: int = int(input("введите четвёртое число "))

x1_is_even: bool = x1 % 2 == 0
y1_is_even: bool = y1 % 2 == 0
x2_is_even: bool = x2 % 2 == 0
y2_is_even: bool = y2 % 2 == 0

if ((x1_is_even and y1_is_even) or (not x1_is_even and not y1_is_even)) \
        == ((x2_is_even and y2_is_even) or (not x2_is_even and y2_is_even)):
    print("имеют одинаковый цвет")
else:
    print("имеют разные цвета")