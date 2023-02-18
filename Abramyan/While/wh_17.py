n: int = int(input("enter the number "))

while n >= 1:
    digit: int = n % 10
    print(digit)
    n: int = n // 10
