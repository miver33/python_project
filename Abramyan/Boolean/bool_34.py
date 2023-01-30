x: int = int(input("введите первое число "))
y: int = int(input("введите второе число "))

x_is_even: bool = x % 2 == 0
y_is_even: bool = y % 2 == 0
if x_is_even and not y_is_even or not x_is_even and y_is_even:
    print("белая")
else:
    print("чёрная")

