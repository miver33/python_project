a: int = int(input("enter positive a: "))
b: int = int(input("enter positive b: "))

number_of_segments: int = a // b
empty_space: int = a % b

print(f"number of segments = {number_of_segments}")
print(f"empty space = {empty_space}")
