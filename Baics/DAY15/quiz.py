# To conduct a mini quizz
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 5", "B. 8", "C. 10", "D. 15"],
        "answer": "B"
    }
]
score = 0
for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print("\nQuiz Completed!")
print("Your final score:", score, "/", len(quiz))
