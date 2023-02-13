START_PRICE: float = 4.95
FINAL_PRICE: float = 24.95
DISCOUNT: float = 0.6


old_price: float = START_PRICE
print("| old  |  new |")
while old_price <= FINAL_PRICE:
    new_price: float = old_price * (1 - DISCOUNT)
    print(f"|{old_price:5.2f} | {new_price:5.2f}|")

    old_price = old_price + 5.0
