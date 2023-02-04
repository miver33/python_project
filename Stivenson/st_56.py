num: float = float(input("enter the number"))

if num < 3 * (10 ** 9):
    print("это радиоволны")
elif num >= 3 * (10 ** 9) and num < 3 * (10 ** 12):
    print("это микроволны")
elif num >= 3 * (10 ** 12) and num < 4.3 * (10 ** 14):
    print("это инфракрасное излучение")
elif num >= 4.3 * (10 ** 14) and num < 7.5 * (10 ** 14):
    print("это видимое излучение")
elif num >= 7.5 * (10 ** 14) and num < 3 * (10 ** 17):
    print("это ультрафиолетовое излучение")
elif num >= 3 * (10 ** 17) and num < 3 * (10 ** 19):
    print("это рентгеновское излучение")
elif num >= 3 * (10 ** 19):
    print("это гамма-излучение")
