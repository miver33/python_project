number: int = int(input("enter the number "))

sum_of_numbers: int = 0
amount_of_numbers: int = 0
while number != 0:
    sum_of_numbers = sum_of_numbers + number
    amount_of_numbers = amount_of_numbers + 1
    number: int = int(input("enter the number "))


if amount_of_numbers == 0:
    print("error")
else:
    average: float = sum_of_numbers / amount_of_numbers
    print(average)




