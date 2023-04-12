import json

with open("questions.json",'r') as file:
    content = file.read()
data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, answers in enumerate(question["Answers"]):
        print(index+1, "-", answers)
    user_choice = int(input("Enter the correct answer"))
    if user_choice == question["Correct_answer"]:
        print("Correct")
    else:
        print("wrong answer")
