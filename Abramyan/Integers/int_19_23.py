number: int = int(input("enter number of seconds: "))

m: int = int(number // 60)
h = int(number // 60 // 60)

print(f"minutes = {m}")
print(f"hours = {h}")
