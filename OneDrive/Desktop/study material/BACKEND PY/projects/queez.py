questions = [
    {
        "prompt": "what is the capital of france",
        "option": ["A. Paris","B. Londan","C. Berlin","D. Madrid"],
        "Answer": "A"
    }
    ,
    {
        "prompt": "what language is primarily spoken in brazil",
        "option": ["A. Spanish","B. Portugues","C. English","D. French"],
        "Answer": "B"
    }
    ,
    {
        "prompt": "what is the smallest prime no",
        "option": ["A. 1","B. 2","C. 3","D. 5"],
        "Answer": "B"
    }
    ,
    {
        "prompt": "what wrote, to kill a Mockingbird",
        "option": ["A. Harper lee","B. Mark twain","C. J.K rowling","D. Ernest Homingway"],
        "Answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["option"]:
            print(option)

        answers = input("Enter your answer (A,B,C,D): ")
        if answers == question["answers"]:
            print("Correct, Horray!!\n")
            score += 1
        else:
            print("WRONG ANSWER.....LOOSER!!! The correct answer was", question["answer"],"\n" )
    
    print(f"You got {score} out of {len(questions)} questions correct. ")
run_quiz(questions)