# циклы используются для повторения участка кода
# while - цикл с предусловием (выполняется, пока некоторое условие истинно)
number: int = int(input("введите число "))

i: int = 1 # счётчик
while i <= number: # проверка условий
    print("привет")

    i = i + 1 # шаг счётчика

print("end")