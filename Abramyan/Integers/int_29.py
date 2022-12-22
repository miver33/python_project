a: int = int(input("enter a "))
b: int = int(input("enter b "))
c: int = int(input("enter c "))

rectangle_area: int = a * b
square_area: int = c * c
number_of_square: int = (a // c) * (b // c)

print(f"number of squares = {number_of_square}")
