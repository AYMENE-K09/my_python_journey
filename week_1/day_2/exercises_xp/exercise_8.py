data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


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