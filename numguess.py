import random

lowest_num = 10
highest_num = 50

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f"Guess a number between {lowest_num} and {highest_num}")
print("Number Guessing Game")

while is_running:
    guess = input("Enter your guess (or type 'exit' to quit): ")

    if guess.lower() == "exit":
        print("Exiting the game...")
        break 

    if guess.isdigit():
        guess = int(guess)
        
        if guess < lowest_num or guess > highest_num:
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {answer}")
            break
    else:
        print("Invalid input. Please enter a number.") 