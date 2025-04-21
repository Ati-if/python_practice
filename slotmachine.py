import random



def spin_row():
  symbols = ['🍒', '🍋', '🍉']
    
  
  row = [random.choice(symbols) for _ in range(3)]
  return row 
  

def print_row(row):
  print("************")
  print("|".join(row))
  print("************")

def get_payout(row , bet):
  if row[0] == row[1] == row[2]:
    if row[0] == '🍒':
      return 2 * bet
    elif row[0] == '🍋':
      return 4 * bet
    elif row[0] == '🍉':
      return 5 * bet
  return 0

def main():
  balance = 100

  print("************************")
  print("Welcome to Python Slot")
  print("Symbols : 🍒 🍋 🍉")
  print("************************")
  

  while balance > 0:
    print(f"Current balance: ${balance}")

    bet = input("Enter your bet amount:") 
    
    if not bet.isdigit():
      print("Please enter a valid number")
      continue


    bet = int(bet)  
    if bet > balance:
      print("Insufficient Funds")
      continue

    if bet <= 0:
      print("Your bet must be greater than zero")
      continue


    balance -= bet     
    row = spin_row()
    print("Spinning....\n")
    print_row(row)

    payout = get_payout(row , bet)
    if payout > 0:
        print(f"You won ${payout}!")
    else:
        print("Sorry, you didn't win.")

    balance += payout

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
      break
  
  print("****************")
  print("Thanks for playing!")
  print("****************")
if __name__ == "__main__":
  main()