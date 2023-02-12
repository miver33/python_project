number_of_user: int = int(input("enter the number "))
sum_of_numbers: int = 0
amount_of_numbers: int = 0

while number_of_user != 0:
    sum_of_numbers = sum_of_numbers + number_of_user
    amount_of_numbers = amount_of_numbers + 1
    number_of_user: int = int(input("enter the number "))
    average: int = sum_of_numbers // amount_of_numbers

if number_of_user == 0 and amount_of_numbers == 0:
    print("error")
else: print(average)



