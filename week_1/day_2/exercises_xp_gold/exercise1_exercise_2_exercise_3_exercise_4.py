
birthdays = {
    'Issam' : "2000/01/01",
    'Anwar' : "2001/02/02",
    'Iman'  : "2002/03/03",
    'Siham' : "2003/04/04",
    'Karim' : "2004/05/05"
}

print("Welcome!!!\nYou can look up the birthdays of the list")

user_name = input("enter a person's name: ")

print(f"It is {birthdays[user_name]} Happy birthday {user_name}")

#-------------------------exercise_2-----------------

birthdays = {
    'Issam' : "2000/01/01",
    'Anwar' : "2001/02/02",
    'Iman'  : "2002/03/03",
    'Siham' : "2003/04/04",
    'Karim' : "2004/05/05"
}

for key, value in birthdays.items():
    print(f"{key} : {value}")

print("Welcome!!!\nYou can look up the birthdays of the list")

user_name = input("enter a person's name: ")

if user_name in birthdays:
    print(f"It is {birthdays[user_name]} Happy birthday {user_name}")

else:
    print(f"Sorry, we don't have the birthday information for {user_name}")

#---------------------exercise_3-------------------

def my_function(X):
    result = X + (X * 11) + (X * 111) + (X * 1111)
    return f"{result} ({X} + {X}{X} + {X}{X}{X} + {X}{X}{X}{X})"

print(my_function(4))

#---------------------exercise_4--------------------

import random

counter_list = []
def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    active = True
    counter = 0
    
    while active:
        set_1 = (throw_dice(), throw_dice())
        print(set_1)
        counter += 1
        if set_1[0] == set_1[1]:
            active = False
            counter_list.append(counter)

def the_main_fct():
    for x in range(100):
        throw_until_doubles()

    total_throws = sum(counter_list)
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {round(total_throws / 100 , 2)}")

the_main_fct()