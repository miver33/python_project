# range - тип диапозона (целочисленный)в python - коллекция

from_0_to_100: range = range(101)
print(list(from_0_to_100))

for i in from_0_to_100:
    print(i)


from_0_to_100: range = range(101)
from_333_to_1000: range = range(333, 1001)
from_n5_to_p5: range = range(-5, 6)
even_from_0_to_100: range = range(0, 101, 2)
print(list(even_from_0_to_100))
from_100_to_0: range = range(100, -1, -1)
print(list(from_100_to_0))
