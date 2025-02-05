# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
#tell the user their score
import random

trivia_questions = {
    "What is the correct file extension for Python files?": ".py",
    "Which keyword is used to define a function in Python?": "def",
    "How do you insert comments in Python code?": "#",
    "What data type is the result of: 3 / 2 in Python?": "float",
    "Which built-in function is used to get the length of a list in Python?": "len()",
    "What is the output of: print(type('Hello'))?": "<class 'str'>",
    "Which keyword is used to create a loop that iterates over a sequence?": "for",
    "What is the correct syntax to create a dictionary in Python?": "{'key': 'value'}",
    "What does the 'break' statement do in Python loops?": "Exits the loop immediately",
    "Which operator is used for exponentiation in Python?": "**"
}

def python_trivia_game():
    questions_list = list(trivia_questions.keys())
    total_questions = 5
    score = 0
        
    selected_questions = random.sample(questions_list, total_questions)
    print(selected_questions,"\n")
    
    for index, question in enumerate(selected_questions):
        print(f"{index+1}. {question}")
        user_answer = input("Enter your answer: ").lower().strip()
        correct_answer = trivia_questions[question]
        if user_answer == correct_answer.lower():
            print("Correct !")
        else:
            print("Wrong !!")    
python_trivia_game()