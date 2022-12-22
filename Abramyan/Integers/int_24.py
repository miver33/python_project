day_of_year: int = int(input("enter day of year "))

day_of_week: int = day_of_year % 7

print(f"в {day_of_year} будет {day_of_week} день недели")