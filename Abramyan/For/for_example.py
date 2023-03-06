# for - цикл прохода по коллекции
list_example: list[int] = [1, 3, 4, 7, 10, 20]
for list_element in list_example: # после слова in указывается колекция, в переменную после слова for ПООЧЕРЕДНО будут сохраняться элементы указанной коллекции
    print(list_element)

summ_of_numbers: int = 0
for number in list_example:
    summ_of_numbers += number

print(summ_of_numbers)
