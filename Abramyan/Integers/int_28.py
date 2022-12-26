day_of_year: int = int(input("enter day of year "))
day_of_week: int = int(input("enter day of week"))

result: int = (day_of_year + day_of_week) % 7

print(f"в {day_of_year} будет {result} день недели")