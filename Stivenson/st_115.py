def get_divisors(number: int) -> list[int]:
    divisors: list[int] = []

    i: int = 1
    while i < number:
        if number % i == 0:
            divisors.append(i)

        i = i + 1

    return divisors


list_of_numbers = get_divisors(63)
print(list_of_numbers)
