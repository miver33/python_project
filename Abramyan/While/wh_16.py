TOTAL_DAY: int = 200
first_day: float = 10.0
percent: float = float(input("введите число от 1 до 50 "))
percent_1: float = percent / 100
days: int = 0

while first_day < TOTAL_DAY:
    first_day = first_day + (first_day * percent_1)
    days = days + 1

print("всего дней", days)
print("сумарный пробег", round(first_day, 2))