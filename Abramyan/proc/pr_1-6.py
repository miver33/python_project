def cube_of_number(number: float) -> float:
    return number ** 3


def get_average(num_1: float, num_2: float) -> float:
    return (num_1 + num_2) / 2


def get_mean(num_1: float, num_2: float) -> float:
    return (num_1 * num_2) ** 0.5


def get_P_of_triangle(side: float) -> float:
    return side * 3


def get_S_of_triangle(side: float) -> float:
    square: float = (side ** 2) * (3 ** 0.5) / 4
    return square


def get_P_of_rectangle(x1: float, y1:float, x2: float, y2:float) -> float:
    a: float = abs(x2 - x1)
    b: float = abs(y2 - y1)
    return a * 2 + b * 2


def get_S_of_rectangle(x1: float, y1:float, x2: float, y2:float) -> float:
    a: float = abs(x2 - x1)
    b: float = abs(y2 - y1)
    return a * b


b: float = float(input("enter the b "))
print(cube_of_number(b))
print(get_average(7, 10))
mean: float = get_mean(10, 50)
print(mean)
