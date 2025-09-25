
# exercise_2-----------------------------
'''
active = True
last_lenght = 0
print("enter the long sentence that you can without the char 'A'")
print("enter quit if you wanna quit the game")
while active:
    user_sentence = input("enter the sentence: ")
    for each in user_sentence:
        if 'A' not in user_sentence and last_lenght < len(user_sentence):
            last_lenght = len(user_sentence)
            print("New score")
    
    if 'A' in user_sentence:
        print("you have to write sentence without 'A'")

    elif user_sentence == "quit":
        print("Good Bye")
        active = False
'''

 #exercise 3------------------------------

import re
paragraph = "is is is an acronym for  and is commonly used in electronic communication to express amusement or laughter. While it originated as an initialism for genuine laughter, its usage has broadened to convey mild amusement, irony, or even to soften a statement. The capitalization can also indicate a stronger reaction, with uppercase LOL signifying more intense amusement than lowercase "

unique_words = []
words = paragraph.split()
sentences = re.split(r'[.]', paragraph)

for word in words:
    if word not in unique_words:
        unique_words.append(word)

non_unique_words = len(words) - len(unique_words) 


print(f"the number of characters is:{len(paragraph)}") #characters
print(f"the number of sentences is: {len(sentences)}") #sentences
print(f"the number fo words is: {len(words)}") #words
print(f"the number of unique words is: {len(unique_words)}") #unique words
print(f"the number of non-unique words is: {non_unique_words}")
print(f"the average word per sentence is: {round(len(words) / len(sentences), 2)}")