from random import randint

numbers: list[int] = []
for i in range(6):
    run_num: int = randint(1, 50)
    numbers.append(run_num)
    if run_num == run_num:
        numbers.remove(run_num)
        run_num: int = randint(1, 50)
        numbers.append(run_num)


numbers = sorted(numbers)
print(numbers)
# не знаю как правильно сделать рандом без повторения. Сделал костыльно, но вроде работает