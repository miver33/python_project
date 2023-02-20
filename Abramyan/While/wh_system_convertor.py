number: int = int(input("введите число "))
base: int = int(input("введите основание "))

if base < 2 or base > 10:
    print("error")
else:
    result_str: str = ""
    while number != 0:
        result_str = result_str + str(number % base)
        number = number // base

    print(result_str[::-1])



