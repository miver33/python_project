# Коллекция - набор данных, расматриваемых вместе
# str - пример коллекции (набор символов или подстрок), упорядоченная коллекция

# list - упорядоченный набор данных определенного типа
# list можно динамически менять

# Способы создания пустого списка
empty_list_1: list = list()
print(empty_list_1)
empty_list_2: list = []
print(empty_list_2)

students: list[str] = []
students.append("Фёдор")
print(students)
students.append("Антон")
students.append("Никита")  # список не гарантирует уникальности
students.append("Никита")
students.append("Никита")
students.append("Никита")
students.append("Никита")
print(students)


list_3: list = [1, 2, 3, "AVC", "GJHK"]

students_2: list[str] = ["Сергей", "Иван", "Егор"]
print("Сергей" in students_2)
print("Сергей" not in students_2)
print(students_2)

# Получение данных из списка
ivan: str = students_2[1]
print(ivan)
# len(коллекция) - функция, вычисляющая длинну коллекции
print(len(students_2))

test: str = "test string" # str тоже упорядоченная коллекция, но она не может измениться
print(test[3])
print(len(test))
print(test[len(test) - 1])

list_4 = [1, 2, 3, 4]
print(4 in list_4)
print(7 in list_4)
