numbers: list[int] = []
number: str = input("enter the number ")
while number != "":
    numbers.append(int(number))
    number: str = input("enter the number ")

negatives: list[int] = []
zeroes_numbers: list[int] = []
positives: list[int] = []
i: int = 0
while i < len(numbers):
    current_number: int = numbers[i]
    if current_number < 0:
        negatives.append(current_number)
    elif current_number == 0:
        zeroes_numbers.append(current_number)
    else:
        positives.append(current_number)

    i = i + 1


print(numbers)
print(negatives, zeroes_numbers, positives)
