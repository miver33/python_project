# Пользователь вводит список чисел, нужно вывести сумму ср знач чисел наибольшее, наименьшее, , произведение,  в нём

def input_int_list() -> list[int]:
    result: list[int] = []
    number: str = input("enter the number ")
    while number != "":
        result.append(int(number))
        number = input("enter the number ")
    return result


def summ_of_list(numbers: list[int]) -> int:
    result: int = 0
    i: int = 0
    while i < len(numbers):
        result = result + numbers[i]
        i = i + 1
    return result


def get_average(numbers: list[int]) -> float:
    return summ_of_list(numbers) / len(numbers)


def prod_list(numbers: list[int]) -> int:
    result: int = 1
    i: int = 0
    while i < len(numbers):
        result *= numbers[i]
        i += 1
    return result


def get_max(numbers: list[int]) -> int:
    max_: int = numbers[0]
    i: int = 0
    while i < len(numbers):
        if numbers[i] > max_:
            max_ = numbers[i]
        i = i + 1
    return max_


def get_min(numbers: list[int]) -> int:
    min_: int = numbers[0]
    i: int = 0
    while i < len(numbers):
        if numbers[i] < min_:
            min_ = numbers[i]
        i = i + 1
    return min_


numbers: list[int] = input_int_list()
print(numbers)

summ: int = summ_of_list(numbers)

print(summ)
prod_of_list: int = prod_list(numbers)
print(prod_of_list)
print(get_max(numbers))
print(get_min(numbers))
