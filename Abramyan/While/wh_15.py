END_MONEY: float = 1100
start_money: float = 1000
percent: float = float(input("введите число от 0 до 25 "))
months: int = 0
percent_1: float = percent / 100

while start_money < END_MONEY:
    start_money = start_money + start_money * percent_1
    months = months + 1


print("месяцы", months)
print("итоговая сумма", start_money)
