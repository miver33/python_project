number: int = int(input("enter four-digit number: "))

num1: int = (number // 100)
num2: int = num1 % 10
num3: int = number // 1000
num4: int = num3 % 10

print("Цифра в сотне: ", num2)
print("цифра в тысяче", num4)