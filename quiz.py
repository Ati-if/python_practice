questions = ("How many elements are there in the periodic table?",
             "Which animal lays the largest eggs?",
             "How many bones does the human body have?")

options = (("A. 118", "B. 119", "C. 120", "D. 1"),
           ("A. Whale", "B. Elephant", "C. Lion", "D. Ostrich"),
           ("A. 206", "B. 207", "C. 208", "D. 209"))

answers = ("A", "D", "A")
guesses = []
score = 0

for question_num in range(len(questions)):
    print("-------------------")
    print(questions[question_num])

    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"answers{question_num} is the correct answer")
        question_num += 1


        print("answers: " , end=" ")
        for answer in answers:
            print(answer, end=" ")
        print()

        print("guesses: " , end=" ")
        for guess in guesses:
            print(guess, end=" ")
        print()
        print(score / len(questions) * 100 )
        print(f"Your score is:{score}%")