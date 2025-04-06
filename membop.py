word = "APPLE"

letter = input("Guess a letter in the secret word")

if letter in word:
   print(f"{letter} is in the secret word")
else:
   print(f"{letter} is not in the secret word")









grades = {"Sandy" : "A",
          "Spongebob" : "A+",
          "Mark" : "B",
          "Sandy" : "A"}

student = input("Enter the name of the student")

if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} has not been found")  