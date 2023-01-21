a: int = int(input("введите первое число "))

is_a_correct: bool = a % 2 == 0 and 9 < a < 100

print(f"a чётное двузначное {is_a_correct}" )