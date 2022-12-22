number: int = int(input("enter three-digit number: "))

hundreds: int = number // 100
dozens: int = ((number - hundreds * 100) // 10)
units: int = number % 10
sum_of_numbers: int = hundreds + dozens + units
prod_of_numbers: int = hundreds * dozens * units
flip_number: int = (dozens * 100) + (hundreds * 10) + units
flip_number_2: int = (hundreds * 100) + (units * 10) + dozens

print(hundreds)
print(dozens)
print(units)
print(f"sum of numbers = {sum_of_numbers}")
print(f"prod of numbers = {prod_of_numbers}")
print(units)
print(dozens)
print(hundreds)
print(dozens, units, hundreds)
print(f"flip number = {flip_number}")
print(f" flip number 2 = {flip_number_2}")