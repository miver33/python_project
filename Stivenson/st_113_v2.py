words: list[str] = []
word: str = input("enter the word ")
while word != "":
    words.append(word)
    word = input("enter the word ")

unique_words: list[str] = []
i: int = 0
while i < len(words):
    current_word: str = words[i]
    if current_word not in unique_words:
        unique_words.append(current_word)

    i = i + 1

print(words)
print(unique_words)
