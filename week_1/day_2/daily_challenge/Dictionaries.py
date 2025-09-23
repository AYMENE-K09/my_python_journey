user_word = input("enter a word: ")
word_dict = {}

for index, letter in enumerate(user_word):
    if letter not in word_dict:
        word_dict[letter] = []
    word_dict[letter].append(index)

print(word_dict)