word = "APPLE"

letter = input("Guess a letter in the secret word")

if letter in word:
   print(f"{letter} is in the secret word")
else:
   print(f"{letter} is not in the secret word")