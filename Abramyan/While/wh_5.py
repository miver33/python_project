n: int = int(input("enter n "))

counter: int = 0
while n > 1:
    counter = counter + 1

    n = n // 2

print(counter)