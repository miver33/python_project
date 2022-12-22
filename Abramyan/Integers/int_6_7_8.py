number: int = int(input("enter two-digit number: "))

dozens: int = number // 10
units: int = number % 10
sum_of_digits: int = dozens + units
prod_of_digits: int = dozens * units
# 12 = 1 * 10 + 2 * 1
reversed_number: int = units * 10 + dozens * 1

print(dozens, units)
print(f"sum: {sum_of_digits}")
print(f"prod: {prod_of_digits}")
print(f"reversed = {reversed_number}")
