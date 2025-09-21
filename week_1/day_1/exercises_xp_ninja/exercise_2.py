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