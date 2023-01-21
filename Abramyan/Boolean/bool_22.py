number: int = int(input("введите число "))

a: int = number // 100
b: int = (number - a * 100) // 10
c: int = number % 10

is_numbers_have_correct_sequence: bool = a < b and b < c or a > b and b > c

print(f"цифры возрастают или убывают {is_numbers_have_correct_sequence}")