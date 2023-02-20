number: int = int(input("введите число "))
base: int = int(input("введите основание "))

while base < 2 or base > 10:
    print("вы ввели неверное основание")
    base: int = int(input("введите основание заново "))

result_str: str = ""
while number != 0:
    result_str = result_str + str(number % base)
    number = number // base

print(result_str[::-1])
