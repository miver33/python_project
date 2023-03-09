numbers: list[str] = []
number: int = int(input("enter the number "))
numbers.append(number)
average: float = 0
i: int = 0

while number != "":
    number: int = int(input("enter the number "))
    numbers.append(int(number))
   # average = (average + numbers[i]) // len(numbers)
   # i += 1

print(average)
print(numbers)
