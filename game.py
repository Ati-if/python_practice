import random

options = ("rock" , "paper" , "scissor")
player = None
computer = random.choice(options)

while player not in options:
  player = input("Enter a choice (rock , paper , scissor)").lower()

  computer = random.choice(options)


print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
  print("It's a tie!")

elif player ==  "rock" and computer == "paper":
  print("Computer wins!")

elif player == "rock" and computer == "scissor":
  print("Player wins")

elif player == player == "scissor" and computer == "paper":
  print("Player wins")

elif player == "scissor" and computer == "rock":
  print("Computer wins") 