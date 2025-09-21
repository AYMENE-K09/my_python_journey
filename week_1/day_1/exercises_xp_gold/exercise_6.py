import random
the_right_number = random.randint(1, 9)
active = True
win_attempt = 0
lost_attempt = 0
print("chose a random number between (1 and 9)")
print("Write quit if you wanna quit the game")
while active:
    user_number = input("enter a number: ")
    
    if user_number == the_right_number:
        print("YOU WON!!!")
        win_attempt += 1
    
    elif user_number == "quit":
        print(f"You won {win_attempt} times")
        print(f"You lost {lost_attempt} times")
        active = False

    elif user_number != the_right_number:
        print("Good Luck Next Time!")
        lost_attempt += 1