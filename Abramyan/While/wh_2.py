a: int = int(input("enter a "))
b: int = int(input("enter b "))

counter: int = 0
while a >= b:
    print(counter)

    a = a - b
    counter = counter + 1

print(counter)
