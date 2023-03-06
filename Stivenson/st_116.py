def get_divisors(number: int) -> list[int]:
    divisors: list[int] = []

    i: int = 1
    while i < number:
        if number % i == 0:
            divisors.append(i)

        i = i + 1

    return divisors


def summ_of_numbers(numbers: list[int]) -> int:
    sum_: int = 0
    i: int = 0
    while i < len(numbers):
        sum_ = sum_ + numbers[i]
        i = i + 1

    return sum_


# def is_perfect_number(number: int) -> bool:
#     divisors: list[int] = get_divisors(number)
#     if summ_of_numbers(divisors) == number:
#         return True
#     else:
#         return False

def is_perfect_number(number: int) -> bool:
    divisors: list[int] = get_divisors(number)
    return summ_of_numbers(divisors) == number


def main():
    i: int = 1
    while i < 10_000:
        if is_perfect_number(i):
            print(i)
        i += 1


main()
