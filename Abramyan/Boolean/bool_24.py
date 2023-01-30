#a != 0

a: int = int(input("введите первое число "))
b: int = int(input("введите второе число "))
c: int = int(input("введите третьей число "))

D = (b ** 2) - 4 * a * c

is_x_have_radicals: bool = D > 0

print(f"есть вещественные корни {is_x_have_radicals}")



# Что-то я не совсем понял как это сделать