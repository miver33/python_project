LOWER: int = 0
UPPER: int = 100

celcium: int = LOWER
print("|celcium    | fahrenheit|   kelvin  | ")
while celcium <= UPPER:
    fahrenheit: float = celcium * (9 / 5) + 32
    kelvin: float = celcium + 273.15
    print(f"|{celcium:^10.3f} | {fahrenheit:^10.3f}| {kelvin:^10.3f}|")

    celcium = celcium + 10
