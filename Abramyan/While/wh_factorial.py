# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 1! = 1
# 0! = 0

number: int = int(input("enter the number "))

if number >= 0:
    i: int = 1
    factorial: int = 1
    while i <= number:
        factorial = factorial * i

        i = i + 1

    print(f"{number}! = {factorial}")
else:
    print("error")
