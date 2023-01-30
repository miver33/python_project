n: int = int(input("enter n "))

three_power: int = 1
while three_power < n:
    three_power = three_power * 3

if three_power == n:
    print(True)
else:
    print(False)
