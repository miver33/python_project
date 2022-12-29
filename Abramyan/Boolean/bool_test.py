# Bool - логический (булевый) тип данных. Используется для представления логических значений
# Bool может принимать только 2 значения True или False
is_rainy: bool = True
# Python операции сравнения всегда возвращают тип bool
# 1. операция == - Равно
# 2. != - неравно
# 3. > - больше
# 4. >=  -больше ИЛИ равно
# 5. < - меньше
# 6. <= - меньше ИЛИ равно
number: int = int(input("enter the number "))

is_five_greater_than_number: bool = 5 > number
print(is_five_greater_than_number)

# Логические операции Python
# 1. Отрицание not
inversion: bool = not is_five_greater_than_number
print(inversion)
# 2. Конъюнкция and
is_five_greater_than_number_and_is_rainy: bool = is_rainy and is_five_greater_than_number
print(is_five_greater_than_number_and_is_rainy)
# 3. Дизъюнкция or
is_five_greater_than_number_or_is_rainy: bool = is_rainy or is_five_greater_than_number
print(is_five_greater_than_number_or_is_rainy)
# 4. Эквиваленция ==
# odd - чётный
is_five_greater_than_number_equal_is_rainy: bool = is_rainy == is_five_greater_than_number
print(is_five_greater_than_number_equal_is_rainy)
# 5. Импликация a -> b = (not a) or b
is_five_greater_than_number_then_is_rainy: bool = not is_five_greater_than_number or is_rainy
print(is_five_greater_than_number_then_is_rainy)