import random

# List of words to choose from
words = ['python', 'hangman', 'challenge', 'programming', 'developer']

# Choose a random word
word = random.choice(words)
guessed_letters = []
tries = 6
display = ['_' for _ in word]

print("Welcome to Hangman!")
print(' '.join(display))

while tries > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
        print("Correct!")
    else:
        tries -= 1
        print(f"Wrong! Tries left: {tries}")

    print(' '.join(display))

if '_' not in display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)
