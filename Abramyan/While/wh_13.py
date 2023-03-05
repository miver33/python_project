number: int = int(input("enter the number "))

k: int = 2
summ_of_numbers: float = 1

while summ_of_numbers < number:
    summ_of_numbers = summ_of_numbers + (1 / k)
    k = k + 1

print(f"{summ_of_numbers:.4f}, {k}")
