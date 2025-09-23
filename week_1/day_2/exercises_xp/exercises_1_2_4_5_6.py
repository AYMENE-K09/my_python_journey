#  --------------exercise_1----------

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

New_dict = dict(zip(keys,values))
print(New_dict)

# exercise_2-----------

family = {}
names = []
ages = []
family_members_number = int(input("enter your family members number: "))

for i in range(family_members_number):
    user_names = input("enter the member name: ")
    user_ages = int(input("enter its age: "))

    names.append(user_names)
    ages.append(user_ages)
print(names)
print(ages)

family = dict(zip(names, ages))
print(family)

for key, value in family.items():
    if value < 3:
        print(f"for {key} the ticket if free")

    elif 3 < value < 12:
        print(f"for {key} the ticket costs $10")

    elif value > 12:
        print(f"for {key} the ticket is for $15")


# exercise_4-------------

def describe_city(city, country= "Morocco"):
    print(f"{city} is in {country}")

describe_city("Casablanca")

# exercise_5----------------

import random

def guessing_number(r_nmr= random.randint(1, 100), g_nmr = int(input("enter a number between 1 and 100: "))):
    
    if r_nmr == g_nmr:
        print(f"Correct!")
    else:
        print(f"Not Correct! \nyou entered: {g_nmr} \nthe correct answer is: {r_nmr}")

guessing_number()

# exercise_6--------------


def make_shirt(**kwargs):
    print(f"The size of shirt is '{kwargs['size']}' and the text is '{kwargs['text']}'")

make_shirt(size = 'Large', text = 'I love python')
make_shirt(size = 'Medium', text = 'I love python')
make_shirt(size = 'Small', text = 'I love ME')
