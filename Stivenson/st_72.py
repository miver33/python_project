start_number: int = 0

while start_number < 100:
    start_number = start_number + 1
    if start_number % 3 == 0 and start_number % 5 == 0:
        print("Fizz-Buzz")
    elif start_number % 3 == 0:
        print("Fizz")
    elif start_number % 5 == 0:
        print("Buzz")
    else:
        print(start_number)
