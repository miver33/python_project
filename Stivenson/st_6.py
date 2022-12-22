TIPS = 0.18
TAX = 0.03

offer: float = float(input("введите стоимость заказа"))

sum_of_tips: float = offer * TIPS
sum_of_tax: float = offer * TAX
sum_of_offer: float = sum_of_tax + sum_of_tips + offer

print(f"Чаевые={sum_of_tips:.2f}")
print(f"Налог={sum_of_tax:.2f}")
print(f"Итого: {sum_of_offer:.2f}")
# Как сделать только 2 знака после запятой?
