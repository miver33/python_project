words: list[str] = []
word: str = input("enter the word ")
while word != "":
    words.append(word)
    word = input("enter the word ")

print(words)

#создать списоу только с уникальными
unique_words: list[str] = []


# Вывести список с уникальными словами
