# функция int - переводит какой-либо объект в целое число
print(int(2.9356))

a_from_decimal:int = int("32") # по умолчанию int воспринимает строку как десятичное число
b_from_binary:int = int("1101101101", base=10)
с_from_hex: int = int("AB9F", base=16)

number:int = 179
binary_number: str = bin(179) # bin - двоичная
oct_number: str = oct(179) # oct - восьмиричная
hex_number: str = hex(179) # hex - шестнадцатиричная

print("end")
print(hex_number)