
# exercise 2

for i in range(1, 20):
    print(i)

print("----------------------------------")
numbers = list(range(1, 21))
for index in range(len(numbers)):
    if index % 2 == 0:
        print(numbers[index])

# exercise 3

name = "aymene"
active = True

while active:
    user_name = input("what is your name: ")
    if name == user_name:
        print("Great!!!")
        active = False
    
# exercise 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("enter your name: ")
if user_name in names:
    print(names.index(user_name))

# exercise 5

user_number_1 = int(input("enter the first number: "))
user_number_2 = int(input("enter the second number: "))
user_number_3 = int(input("enter the third number: "))

user_numbers = [user_number_1, user_number_2, user_number_3]
print(f"{max(user_numbers)} is the great number")

# exercise 6

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