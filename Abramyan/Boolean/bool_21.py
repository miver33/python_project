number: int = int(input("введите число "))

a: int = number // 100
b: int = (number - a * 100) // 10
c: int = number % 10

is_numbers_have_sequence: bool = a < b and b < c

print(f"цифры последовательны {is_numbers_have_sequence}")