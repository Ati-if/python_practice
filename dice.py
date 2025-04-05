import random

# ASCII art for dice faces
dice_faces = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ),
    2: (
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"
    )
}

def roll_dice(num_dice=1):
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(rolls):
    # Print all dice side by side
    for i in range(5):
        print("  ".join(dice_faces[roll][i] for roll in rolls))

def main():
    print("🎲 Welcome to the Dice Roller with Pictures!")
    
    while True:
        try:
            num = int(input("How many dice do you want to roll? (1 or 2): "))
            if num not in [1, 2]:
                print("Please choose either 1 or 2.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        rolls = roll_dice(num)
        print("\nYou rolled:")
        print_dice(rolls)

        again = input("\nRoll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()