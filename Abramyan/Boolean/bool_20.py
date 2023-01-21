number: int = int(input("введите число "))

a: int = number // 100
b: int = (number - a * 100) // 10
c: int = number % 10

is_number_havent_same_numbers: bool = a != b != c and a != c

print(f"цифры не равны {is_number_havent_same_numbers}")