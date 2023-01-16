a: int = int(input("enter first number "))
b: int = int(input("enter second number "))
c: int = int(input("enter third number "))

positives: int = 0
negatives: int = 0
zeroes: int = 0

if a > 0:
    positives += 1
elif a == 0:
    zeroes += 1
else:
    negatives += 1

if b > 0:
    positives += 1
elif b == 0:
    zeroes += 1
else:
    negatives += 1

if c > 0:
    positives += 1
elif c == 0:
    zeroes += 1
else:
    negatives += 1


print(positives)
print(negatives)
print(zeroes)