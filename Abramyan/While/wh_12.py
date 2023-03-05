number: int = int(input("enter the number "))

k: int = 1
summ_of_numbers: int = 0

while summ_of_numbers < number:
    summ_of_numbers = summ_of_numbers + k
    k = k + 1

if summ_of_numbers > number:
    summ_of_numbers = summ_of_numbers - k
    k = k - 1

print(summ_of_numbers, k)