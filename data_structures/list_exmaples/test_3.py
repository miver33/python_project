numbers: list[float] = []
user_input: str = input("enter the number ")
while user_input != "Q":
    numbers.append(float(user_input))
    user_input = input("enter the number ")

i: int = 0
summ: float = 0
while i < len(numbers):
    summ = summ + numbers[i]
    i = i + 1

if len(numbers) == 0:
    print("error")
else:
    everage: float = summ / len(numbers)
    print(everage)
