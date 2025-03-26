import random

low = 10
high = 100
guesses = 0

options = ["heads", "tails"]
options = random.choice(options)
print(options)
number = random.randint(low, high)

print(f"Guess a number between {low} and {high}")