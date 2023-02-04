num: int = int(input("enter the number "))

if num % 2 == 0:
    s: str = "чётное"
else:
    s: str = "нечётное"

if num >= 1 and num <= 9:
    m: str = "однозначное число"
elif num > 9 and num < 100:
    m: str = "двузначное число"
elif num > 99 and num < 1000:
    m: str = "трёхзначное число"

print(s , m)
