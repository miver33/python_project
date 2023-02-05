n: int = int(input("enter n "))
k: int = 0
s: int = 2

while k ** s < n:
    k ** s
    k = k + 1
if k ** s > n:
    k = k - 1

print(k)