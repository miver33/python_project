a: int = int(input("введите число "))

is_a_correct: bool = a % 2 == 1 and 99 < a < 1000

print(f"a нечётное трёхзначное {is_a_correct}" )