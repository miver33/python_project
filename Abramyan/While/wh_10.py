n: int = int(input("enter n "))
k: int = 1

while 3 ** k < n:
    k = k + 1

if 3 ** k >= n:
    k = k - 1

print(k)