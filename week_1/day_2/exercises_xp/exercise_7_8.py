
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
