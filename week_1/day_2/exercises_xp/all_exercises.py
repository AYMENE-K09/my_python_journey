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

# exercise_3----------------------

brand = {
    'name': 'Zara',
    'creation_date' : 1975,
    'creator_name' : 'Amancio Ortega Gaona' ,
    'type_of_clothes' : ['men', 'women', 'children', 'home' ],
    'international_competitors' : ['Gap', 'H&M', 'Benetton'],
    'number_stores' : 700,
    'major_color' : {
        'France': 'blue', 
        'Spain': 'red', 
        'US': 'pink ' 'green'
    }
}

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update({'number_stores': 2})
print("Zara clients are:")
for value in brand.get('type_of_clothes'):
    print(value, end=" / ")
brand.update({'country_creation' : 'Spain'})

for key in brand.keys():
    if key == 'international_competitors':
        print(f"\n{key} is in the dictionary brand")

brand.get('international_competitors').append('Desigual')

brand.pop('creation_date')
print(brand.get('international_competitors')[3])
print(brand['major_color']['US'])
print(brand)
i = 0
for key in brand.keys():
    i +=1
else:
    print(f"the number of keys is: {i}")

brand.update(more_on_zara)

print(brand.get('number_stores'))




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


#----------------------exercise_7------------------------------

import random

def get_random_temp(season):
    seasons = ['WINTER', 'AUTUMN', 'SPRING', 'SUMMER']
    if season in seasons:
        print(f"we are in {season} season")
        if season == 'WINTER':
            return float(random.randint(-10, 16))
        elif season == 'AUTUMN':
            return float(random.randint(16, 23))
        elif season == 'SPRING':
            return float(random.randint(23, 32))
        elif season == 'SUMMER':
            return float(random.randint(32, 40))

def main():
    temp = get_random_temp(input("enter a season: ").upper())
   
    print(f"The temperature right now is {temp} degrees Celsius")
    if 0 > temp:
        print("Brr, that's freezing! Wear some extra layers tody")

    elif 0 < temp < 16:
        print("Quite chilly! Don't forget your coat")

    elif 16 < temp < 23:
        print("Drink hot tea before leaving")

    elif 24 < temp < 32:
        print("It is a nice day to walk")

    else:
        print("It is hot outside drik more water")

main()

#-----------------------exercise_8--------------------------

data = [ {"question": "What is Baby Yoda's real name?", "answer": "Grogu"} , { "question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"} , {"question": "What year did the first Star Wars movie come out?","answer": "1977"} , { "question": "Who built C-3PO?","answer": "Anakin Skywalker" } , {"question": "Anakin Skywalker grew up to be who?","answer": "Darth Vader"} , {"question": "What species is Chewbacca?","answer": "Wookiee"}]


def ask_user():
    correct_answer = 0
    wrong_answer = 0
    wrong_answers = []
    for item in data:
        print(item['question'])
        user_input = input("enter your answer: ")
        if user_input == item['answer']:
            correct_answer += 1
        else:
            wrong_answer += 1
            wrong_answers.append(item['question'])
    
    print(f"you have {correct_answer} correct answers")
    print("---------------")
    print(f"you have {wrong_answer} wrong answers")
    print("---------------")
    print("your wrong answers:")
    print(" ")
    for question in wrong_answers:
        print(question)
        print("---------------")
    
    if wrong_answer > 3:
        print("you have to replay!!!")

    else:
        print("you are a real fun of star wars!!!")
ask_user()
