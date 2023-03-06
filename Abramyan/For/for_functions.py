def summ_of_list(numbers: list[int]) -> int:
    sum_: int = 0
    for number in numbers:
        sum_ += number
    return sum_


def find_max(numbers: list[int]) -> int:
    max_n: int = numbers[0]
    for number in numbers:
        if number > max_n:
            max_n = number
    return max_n
