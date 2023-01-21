number: int = int(input("enter the number "))

if number > 0 and number % 2 == 0:
    print(f"{number} положительное чётное")
elif number > 0 and number % 2 == 1:
    print(f"{number} положительное нечётное")
elif number < 0 and number % 2 == 0:
    print(f"{number} отрицательное чётное")
elif number < 0 and number % 2 == 1:
    print(f"{number} отрицательное нечётное")
else:
    print("это нулевое число")