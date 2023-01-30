name: str = input("enter the name ")

while name != "":  # заголовок цикла
    print(f"hello {name}")  # начало тела цикла

    name: str = input("enter the name ")  # конец тела цикла

print("end")
