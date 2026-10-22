print("--- Mnini Quiz Game---")
quiz_question = [
    {
        "question" : "which of the following is a programing language: ",
        "options" : ["A. Python" , "B. Jave" , "c. C++" ,"D. HTML"],
        "answer" : "A"
    },
    {
        "question": "python kis type ki langrage hai? ",
        "options" : ["A. Complied" , "B. Interpreted", "C. Machine", "D. Assembly"],
         "answer": "B"
    }
]

score = 0.0
for q in quiz_question:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    user_answer = input("Enter your answer (A/B/C/D)").strip().upper()
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Sahi jawab {q['answer']} tha. \n")
print(f"Game Over! Aapka total score: {score}")
