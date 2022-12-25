PRICE = 3.49

amount_of_bread: int = int(input("enter amount of bread "))

price_with_discount: float = PRICE - PRICE * 0.6
price_of_all: float = amount_of_bread * price_with_discount


print("цена буханки хлеба $ =", PRICE)
print("цена со скидкой $ = ", "%.2f" % price_with_discount)
print("итоговая цена $ =", "%.2f" % price_of_all)
