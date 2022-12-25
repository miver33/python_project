number: int = int(input("enter number of seconds: "))

m: int = int(number // 60)
h: int = int(number // 60 // 60)
last_second_of_minutes: int = (number % 60)
last_second_of_hour: int = number % 3600
minutes_from_hour: int = m % 60


print(f"minutes = {m}")
print(f"hours = {h}")
print(f"секунды с последней минуты {last_second_of_minutes}")
print(f"секунды с последнего часа {last_second_of_hour}")
print(f"минуты с последнего часа {minutes_from_hour}")