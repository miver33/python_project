from random import randint


def create_random_numbers(count: int) -> list[int]:
    numbers: list[int] = []
    for i in range(count): # выполнится ровно count раз
        ran_num: int = randint(-5, 5)
        numbers.append(ran_num)
    return numbers


def get_jagged_elements_WHILE(numbers: list[int]) -> list[int]:
    jagged: list[int] = []
    i: int = 1
    while i < len(numbers) - 1:
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            jagged.append(numbers[i])
        i += 1
    return jagged


def get_jagged_elements(numbers: list[int]) -> list[int]:
    jagged: list[int] = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            jagged.append(numbers[i])
    return jagged


rndm_nums: list[int] = create_random_numbers(25)
print(rndm_nums)
print(get_jagged_elements_WHILE(rndm_nums))
print(get_jagged_elements(rndm_nums))
