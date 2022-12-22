print("введите переменную а")
a: str = input()
print("ведите переменную b")
b: str = input()

temp: str = a
a = b
b = temp

print(f"переменная а:{a}")
print(f"переменная b:{b}")
