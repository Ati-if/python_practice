import random

# Categories with words and hints
word_bank = {
    'Animals': [
        ('elephant', 'The largest land animal.'),
        ('giraffe', 'Has a very long neck.'),
        ('kangaroo', 'A marsupial that jumps.'),
        ('penguin', 'A bird that swims instead of flies.')
    ],
    'Food': [
        ('pizza', 'A popular cheesy Italian dish.'),
        ('sushi', 'Japanese dish with rice and fish.'),
        ('hamburger', 'A sandwich with beef patty.'),
        ('spaghetti', 'A long, thin pasta.')
    ],
    'Countries': [
        ('brazil', 'Famous for football and the Amazon rainforest.'),
        ('canada', 'Known for maple syrup and hockey.'),
        ('japan', 'Land of the rising sun.'),
        ('egypt', 'Home of the pyramids.')
    ]
}

# Hangman stages
hangman_pics = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    category = random.choice(list(word_bank.keys()))
    word, hint = random.choice(word_bank[category])
    return category, word, hint

def play_game():
    category, word, hint = choose_word()
    guessed_letters = []
    tries = 6
    display = ['_' for _ in word]

    print("Welcome to Hangman!")
    print(f"Category: {category}")
    print(f"Hint: {hint}")

    while tries > 0 and '_' in display:
        print(hangman_pics[6 - tries])
        print('Word:', ' '.join(display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
            print("Correct!")
        else:
            tries -= 1
            print("Incorrect!")

    print(hangman_pics[6 - tries])
    if '_' not in display:
        print("🎉 You guessed the word:", word)
    else:
        print("😵 Game Over! The word was:", word)

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

main()
