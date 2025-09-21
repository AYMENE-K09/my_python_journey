import re
paragraph = "is is is an acronym for  and is commonly used in electronic communication to express amusement or laughter. While it originated as an initialism for genuine laughter, its usage has broadened to convey mild amusement, irony, or even to soften a statement. The capitalization can also indicate a stronger reaction, with uppercase LOL signifying more intense amusement than lowercase "

unique_words = []
words = paragraph.split()
sentences = re.split(r'[.]', paragraph)

for word in words:
    if word not in unique_words:
        unique_words.append(word)


print(f"the number of characters is:{len(paragraph)}") #characters
print(f"the number of sentences is: {len(sentences)}") #sentences
print(f"the number fo words is: {len(words)}") #words
print(f"the number of unique word is: {len(unique_words)}") #unique words