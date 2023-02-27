names: list[str] = []
name: str = input("enter the name ")
while name != "Q":
    names.append(name)
    name = input("enter the name ")

i: int = 0
while i < len(names):
    print(f"Привет, {names[i]}")
    i = i + 1
