n: int = int(input("enter n "))
k: int = 0
summon: int = 0

while summon + k <= n:
    summon = summon + k
    k = k + 1
if summon + k > 0:
    k = k - 1

print(k , "сумма равна", summon)
